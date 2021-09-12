import struct


def number_to_binary(i: int) -> bytes:
    # TODO: for non-ascii data or anyway, we might want to use unsigned short instead.
    # docs at https://docs.python.org/3/library/struct.html#format-characters
    return struct.pack("B", i)
