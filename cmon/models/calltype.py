from enum import Enum


class CallType(Enum):
    """
    call types enum
    """
    RING = 0
    CALL = 1
    CONNECT = 2
    DISCONNECT = 3
