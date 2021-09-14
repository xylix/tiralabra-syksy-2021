import logging
import pickle
from time import time
from typing import Dict, List


START_DICT: Dict[str, int] = {chr(i): i for i in range(128)}
MAX_DICT = 16000


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

    output: List[int] = []
    dictionary = START_DICT.copy()
    s = ""

    # Operations per second related code
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

        # Possible future optimization: reset dict after n misses in a row (could be a tell that the data has different sections)
        if s + ch in dictionary:
            s = s + ch
        else:
            output.append(dictionary[s])
            # If we are encoding as python integers, the only limit could be how big of a dict can fit into ram
            # Also the dictionary needs to stay some percentage of the size of the input
            if len(dictionary) < MAX_DICT:
                dictionary[s + ch] = len(dictionary)
            s = ch
    output.append(dictionary[s])
    logging.debug(f"dict: {dictionary}")
    return pickle.dumps(output, protocol=4)


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
    input_data: List[int] = pickle.loads(raw_data)

    def translate(code: int) -> str:
        # logging.debug(f"translating code {code}, length of dict: {len(dictionary)}")
        return reverse_dict[code]

    output: List[str] = []
    dictionary = START_DICT.copy()
    reverse_dict: Dict[int, str] = {value: key for (key, value) in dictionary.items()}
    # Handle the first entry separately
    prevcode = input_data[0]
    output.append(translate(prevcode))

    # Operations per second related code
    last_i = 0
    last_print = 0
    for i, currcode in enumerate(input_data[1:]):
        if time() - last_print >= 0.5:
            logging.debug(f"operations per second: {i - last_i}")
            logging.debug(f"progress: {i / len(input_data)}")
            last_print = time()
            last_i = i

        if currcode < len(dictionary):
            entry = translate(currcode)
        else:
            # An sCsCs form was encountered, and we need to infer the entry
            # This is an oddity caused by the fact that the decoders dict is
            # always one symbol behind the encoders dict.
            x = translate(prevcode)
            entry = x + x[0]

        # logging.debug(f"currcode's decoded value: {repr(entry)}")
        output.append(entry)
        ch = entry[0]
        if len(dictionary) < MAX_DICT:
            reverse_dict[len(dictionary)] = translate(prevcode) + ch
            dictionary[translate(prevcode) + ch] = len(dictionary)
        # logging.debug(
        #     f"added translation {repr(translate(prevcode) + ch)}: {len(dictionary)}"
        # )
        prevcode = currcode

    return bytes("".join(output), encoding="ascii")
