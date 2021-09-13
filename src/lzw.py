import logging
from time import time
from sys import getsizeof
from typing import Dict

from src.utils.binary import number_to_binary


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

    output = []
    dictionary = START_DICT.copy()
    s = ""
    dict_full = False

    last_i = 0
    last_print = 0
    for i, ch in enumerate(data):
        if time() - last_print >= 0.5:
            logging.debug(f"operations per second: {i - last_i}")
            logging.debug(f"progress: {i / len(data)}")
            last_print = time()
            last_i = i
        # logging.debug(f"character at index {i}: {repr(ch)}")
        # logging.debug(f"s+ch ({repr(s+ch)}) in dict: {dictionary.get(s+ch)}")

        if s + ch in dictionary:
            s = s + ch
        else:
            output.append(dictionary[s])
            if not dict_full and len(dictionary) < 256:
                dictionary[s + ch] = number_to_binary(len(dictionary))
                dict_full = True
            s = ch
    output.append(dictionary[s])
    logging.debug(f"dict: {dictionary}")
    logging.debug(f"Compression ratio: { getsizeof(output) / getsizeof(input_data) }")
    return b"".join(output)


def decompress(raw_data: bytes) -> bytes:
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

    # TODO: just use the binary data here
    # input_data: str = pickle.loads(raw_data)

    def translate(code: int) -> str:
        return list(dictionary.keys())[int(code)]

    output: list[str] = []
    dictionary = START_DICT.copy()
    # Handle the first entry separately
    prevcode = int(raw_data[0])
    output.append(translate(prevcode))
    for i, currcode in enumerate(raw_data[1:]):
        logging.debug(f"currcode at index {i}: {currcode}")
        entry = translate(int(currcode))
        logging.debug(f"currcode's decoded value: {repr(entry)}")
        output.append(entry)
        ch = entry[0]
        if len(dictionary) < 256:
            dictionary[translate(prevcode) + ch] = number_to_binary(
                len(dictionary.items())
            )
        logging.debug(
            f"added translation {translate(prevcode) + ch}: {len(dictionary.items())}"
        )
        prevcode = int(currcode)

    return bytes("".join(output), encoding="ascii")
