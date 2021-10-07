from .basecall import BaseCall
from .calltype import CallType
from .incomingcall import IncomingCall
from .outgoingcall import OutgoingCall
from .establishedcall import EstablishedCall
from .finishedcall import FinishedCall

# mapping of call types to corresponding classes
CALL_TYPES_MAPPING = {
    "RING": IncomingCall,
    "CALL": OutgoingCall,
    "CONNECT": EstablishedCall,
    "DISCONNECT": FinishedCall,
}
