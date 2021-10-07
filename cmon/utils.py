import datetime


def split_cols(s, required_cols):
    """
    split given string by ';' and ensure that
    required number of columns is there
    """
    cols = s.split(";")
    if len(cols) != required_cols:
        # invalid number of columns for call type
        raise ValueError(
            f"Invalid number of columns for string '{s}'! Abort."
        )

    return cols


def parse_timestamp(timestamp):
    """
    parses given timestamp
    """
    return datetime.datetime.strptime(
        timestamp, "%d.%m.%y %H:%M:%S"
    )
