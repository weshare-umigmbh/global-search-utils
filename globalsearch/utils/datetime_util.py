from typing import Union

from dateutil import parser


def iso_string_to_unix_timestamp(iso_string: str) -> Union[int, None]:
    if iso_string is None:
        return None
    return int(parser.parse(iso_string).timestamp()) * 1000
