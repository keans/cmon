from cmon.models import BaseCall, CallType
from cmon.utils import parse_timestamp, split_cols


class IncomingCall(BaseCall):
    """
    incoming call
    """
    def __init__(
        self, timestamp, connection_id, caller_number, callee_number, device
    ):
        BaseCall.__init__(
            self, timestamp, CallType.RING, connection_id
        )
        self.caller_number = caller_number
        self.callee_number = callee_number
        self.device = device

    @staticmethod
    def create_from(s):
        """
        timestamp;RING;ConnectionID;CallerNumber;CalleeNumber;
        """
        # split string into columns
        cols = split_cols(s, required_cols=7)

        return IncomingCall(
            timestamp=parse_timestamp(cols[0]),
            connection_id=cols[2],
            caller_number=cols[3],
            callee_number=cols[4],
            device=cols[5]
        )
