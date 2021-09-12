import logging
import struct
from typing import Dict


def number_to_binary(i: int) -> bytes:
    # TODO: for non-ascii data or anyway, we might want to use unsigned short instead.
    # docs at https://docs.python.org/3/library/struct.html#format-characters
    return struct.pack("B", i)


START_DICT: Dict[str, bytes] = {chr(i): number_to_binary(i) for i in range(128)}


def compress(input_data: bytes) -> bytes:
    # pylint: disable=invalid-name
    """
    Takes in an input string and returns a compressed version of it.

    Roughly implements the following pseudocode from https://www2.cs.duke.edu/csed/curious/compression/lzw.html

    string s;
    char ch;
    ...

    s = empty string;
    while (there is still data to be read)
    {
        ch = read a character;
        if (dictionary contains s+ch)
        {
            s = s+ch;
        }
        else
        {
            encode s to output file;
            add s+ch to dictionary;
            s = ch;
        }
    }
    encode s to output file;
    """
    # TODO: actually handle taking in byte data
    data = str(input_data, encoding="utf-8")

    output = bytes()
    dictionary = START_DICT.copy()
    s = ""

    for i, ch in enumerate(data):
        logging.debug(f"character at index {i}: {repr(ch)}")
        logging.debug(f"s+ch ({repr(s+ch)}) in dict: {dictionary.get(s+ch)}")

        if s + ch in dictionary:
            s = s + ch
        else:
            output += dictionary[s]
            if len(dictionary) < 256:
                dictionary[s + ch] = number_to_binary(len(dictionary))
            s = ch
    output += dictionary[s]
    logging.debug(f"dict: {dictionary}")
    return output


def decompress(input_data: str) -> bytes:
    # pylint: disable=invalid-name
    """
    extracts and .lzw file into {filename}.out

    Roughly implements the following pseudocode from https://www2.cs.duke.edu/csed/curious/compression/lzw.html

    string entry;
    char ch;
    int prevcode, currcode;
    ...

    prevcode = read in a code;
    decode/output prevcode;
    while (there is still data to read)
    {
        currcode = read in a code;
        entry = translation of currcode from dictionary;
        output entry;
        ch = first char of entry;
        add ((translation of prevcode)+ch) to dictionary;
        prevcode = currcode;
    }

    """

    def translate(code: int) -> str:
        return list(dictionary.keys())[int(code)]

    output: list[str] = []
    dictionary = START_DICT.copy()
    splat = input_data.split(",")
    # Handle the first entry separately
    prevcode = int(splat[0])
    output.append(translate(prevcode))
    for i, currcode in enumerate(splat[1:]):
        logging.debug(f"currcode at index {i}: {currcode}")
        entry = translate(int(currcode))
        logging.debug(f"currcode's decoded value: {repr(entry)}")
        output.append(entry)
        ch = entry[0]
        dictionary[translate(prevcode) + ch] = len(dictionary.items())
        logging.debug(
            f"added translation {translate(prevcode) + ch}: {len(dictionary.items())}"
        )
        prevcode = int(currcode)

    return bytes("".join(output), encoding="ascii")
