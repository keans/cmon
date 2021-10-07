from cmon.models import BaseCall, CallType
from cmon.utils import parse_timestamp, split_cols


class OutgoingCall(BaseCall):
    """
    outgoing call
    """
    def __init__(
        self, timestamp, connection_id, subsidiary,
        used_number, called_number, device
    ):
        BaseCall.__init__(
            self, timestamp, CallType.CALL, connection_id
        )
        self.subsidiary = subsidiary
        self.used_number = used_number
        self.called_number = called_number
        self.device = device

    @staticmethod
    def create_from(s):
        """
        timestamp;CALL;ConnectionID;Subsidiary;UsedNumber;CalledNumber;
        """
        # split string into columns
        cols = split_cols(s, required_cols=8)

        return OutgoingCall(
            timestamp=parse_timestamp(cols[0]),
            connection_id=cols[2],
            subsidiary=cols[3],
            used_number=cols[4],
            called_number=cols[5],
            device=cols[6]
        )
