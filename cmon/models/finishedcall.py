from cmon.models import BaseCall, CallType
from cmon.utils import parse_timestamp, split_cols


class FinishedCall(BaseCall):
    """
    finished call
    """
    def __init__(
        self, timestamp, connection_id, duration
    ):
        BaseCall.__init__(
            self, timestamp, CallType.DISCONNECT, connection_id
        )
        self.duration = duration

    @staticmethod
    def create_from(s):
        """
        timestamp;DISCONNECT;ConnectionID;durationInSeconds;
        """
        # split string into columns
        cols = split_cols(s, required_cols=5)

        return FinishedCall(
            timestamp=parse_timestamp(cols[0]),
            connection_id=cols[2],
            duration=cols[3]
        )
