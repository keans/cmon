cmon
====

``cmon`` is a Python package to monitor incoming and outgoing calls that
are arriving at the FritzBox.


Module Installation
-------------------

The easiest way to install the ``cmon`` module is via ``pip``:

::

    pip install cmon


Prerequirements
---------------

In the first step, the TCP server on 1012 at the FritzBox must be enabled.
This can be done by using a DECT phone that is registered at the FritzBox.
Just call #96*5* and press the green button (call) to activate the service.

If you later want to deactivate it again, simply dial #96*4* and press
the green button (call).


Example
-------

::

    from cmon import CallMonitor

    # create an instance of the call monitor
    # (notice: the server and port are the default values and can be left out)
    cm = CallMonitor("fritz.box", 1012)

    # add a listener function, i.e., an arbitrary function that will
    # obtain a call event, here we simply use a lambda function to print
    # the incoming events
    cm.add_listener(lambda event: print(event))

    # start the monitor to listen for phone call events
    # it will run forever unless you press Ctrl + C
    cm.start()
