import socket
import threading
import queue
import logging

from cmon.models import CALL_TYPES_MAPPING


# prepare logger
log = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)


class ListenerThread(threading.Thread):
    """
    thread to listen for incoming data on the socket
    """
    def __init__(self, sock, q):
        threading.Thread.__init__(self)
        self.daemon = True

        self._sock = sock
        self._q = q
        self._event = threading.Event()

    def run(self):
        """
        start listener thread
        """
        log.debug("starting producer (listener)...")
        buffer = ""
        while not self._event.is_set():
            # read data from socket
            try:
                data = self._sock.recv(1024).decode("ascii")

            except OSError:
                data = ""

            if not data:
                # no data (=socket closed)
                log.debug("no data => shutting down")
                self.shutdown()

            else:
                log.debug(f"received data: '{data}'")

            # add data to buffer
            buffer += data

            # identify complete lines that can be parsed
            while "\n" in buffer:
                # get first line of buffer and and keep rest in the buffer
                line, buffer = buffer.split("\n", 1)

                # put received line to queue
                log.debug(f"putting '{line}' to the queue")
                self._q.put(line)

        log.debug("stopping listener")

    def shutdown(self):
        """
        shutdown the listener thread
        """
        self._sock.close()
        self._event.set()
        self._q.put(None)


class CallMonitor:
    """
    FritzBox call monitor class
    """
    def __init__(
        self, hostname="fritz.box", port=1012,
    ):
        self._hostname = hostname
        self._port = port

        self._sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._q = queue.Queue()
        self._listeners = []
        self.listener_thread = None

    def add_listener(self, listener):
        """
        add listener to the call monitor
        => listeners will be called on event
        """
        self._listeners.append(listener)

    def start(self):
        """
        start the call monitor
        """
        try:
            # connect socket
            log.debug(f"connection to {self._hostname}:{self._port}...")
            self._sock.connect((self._hostname, self._port))

            # start listener thread
            self.listener_thread = ListenerThread(self._sock, self._q)
            self.listener_thread.start()

            while True:
                # get linen from queue
                line = self._q.get()
                if line is None:
                    # final None to end loop
                    break

                # get command from line at second position
                cmd = line.split(";")[1]
                log.debug(f"got '{line}' from queue -> {cmd}")

                # create corresponding call type class from command in line
                call_type = CALL_TYPES_MAPPING.get(cmd).create_from(line)
                if call_type is None:
                    # unknown call type
                    log.error(f"Could not identify call type from '{line}'!")

                else:
                    # valid call type
                    if len(self._listeners) > 0:
                        # one or more listeners found
                        for listener in self._listeners:
                            # call listener
                            log.debug(
                                f"Passing '{call_type}' to '{listener}'."
                            )
                            listener(call_type)
                            log.debug(f"callback to '{listener}' completed.")

                    else:
                        # no listeners
                        log.debug("No listeners found.")

        except KeyboardInterrupt:
            # Ctrl + C
            pass

        finally:
            # shutdown
            self.shutdown()

    def shutdown(self):
        """
        shutdown the call monitor
        """
        log.debug("starting shutdown...")

        if self.listener_thread is not None:
            # shutdown listener thread
            self.listener_thread.shutdown()
            self.listener_thread.join()

        log.debug("shutdown done.")
