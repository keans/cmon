from cmon.models import BaseCall, CallType
from cmon.utils import parse_timestamp, split_cols


class EstablishedCall(BaseCall):
    """
    established call
    """
    def __init__(
        self, timestamp, connection_id, subsidiary, used_number
    ):
        BaseCall.__init__(
            self, timestamp, CallType.CONNECT, connection_id
        )
        self.subsidiary = subsidiary
        self.used_number = used_number

    @staticmethod
    def create_from(s):
        """
        timestamp;CONNECT;ConnectionID;Subsidiary;number;
        """
        # split string into columns
        cols = split_cols(s, required_cols=6)

        return EstablishedCall(
            timestamp=parse_timestamp(cols[0]),
            connection_id=cols[2],
            subsidiary=cols[3],
            used_number=cols[4]
        )
