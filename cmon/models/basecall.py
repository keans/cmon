import abc


class BaseCall(abc.ABC):
    """
    abstract base class from which all
    other call classes are derived
    """
    def __init__(self, timestamp, call_type, connection_id):
        self.timestamp = timestamp
        self.call_type = call_type
        self.connection_id = connection_id

    @staticmethod
    @abc.abstractmethod
    def create_from(s):
        """
        create call from string
        """
        pass

    def __repr__(self):
        attrs = [f"{k}={v}" for k, v in self.__dict__.items()]
        return (
            f"<{self.__class__.__name__}("
            f"{', '.join([attr for attr in attrs])}>"
        )
