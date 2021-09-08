import logging
from typing import Dict
import typer


START_DICT: Dict[str, int] = {chr(i): i for i in range(128)}


""" Pseudocode from https://www2.cs.duke.edu/csed/curious/compression/lzw.html

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


def compress(filename):
    """
    Creates a compressed file named {filename}.lzw
    """
    output = ""
    # dictionary: Dict[str, str] = {}
    # TODO: build the beginning dictionary here from all the single characters in the file
    dictionary = START_DICT.copy()
    with open(filename, "r") as f:
        chars = f.read()
        s = ""
        for i, ch in enumerate(chars):
            logging.debug(f"character at index {i}: {ch}")
            logging.debug(f"s+ch ({s+ch}) in dict: {dictionary.get(s+ch)}")

            if dictionary.get(s + ch):
                s = s + ch
            else:
                # FIXME: This generates an extra comma at the end of the out file
                output += str(dictionary[s]) + ","
                # TODO: this might be incorrect
                dictionary[s + ch] = len(dictionary.items())
                s = ch
    logging.debug(f"output: {output}")
    logging.debug(f"dict: {dictionary}")
    with open(f"{filename}.lzw", "w") as outf:
        outf.write(output)

    # this is not necessary; dict can be built during decoding https://en.wikipedia.org/wiki/Lempel%E2%80%93Ziv%E2%80%93Welch#Decoding
    # with open(f"{filename}.lzwdict") as outdict:
    # outdict.write(dictionary)
    pass


""" Pseudocode from https://www2.cs.duke.edu/csed/curious/compression/lzw.html

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


def decompress(filename: str):
    """
    extracts and .lzw file into {filename}.out
    """
    output = ""
    dictionary = START_DICT.copy()
    with open(filename, "r") as f:
        chars = f.read()
        splat = chars.split(",")
        prevcode = splat[0]
        for i, currcode in enumerate(splat):
            logging.debug(f"currcode at index {i}: {currcode}")
            entry = list(dictionary.keys())[int(currcode)]
            output += entry
            ch = entry[0]
            dictionary[prevcode + ch] = len(dictionary.items())
            prevcode = currcode

            pass

    with open(f"{filename}.out", "w") as outf:
        outf.write(output)


def main(
    filename: str,
    archive: bool = True,
    extract: bool = False,
    debug: bool = True,
):
    if archive and extract:
        raise Exception("Either archive or extract, not both")
    if debug:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.WARNING)
    # logging.debug(f"Argument List: {sys.argv}")
    if archive:
        compress(filename)
    elif extract:
        decompress(filename)


if __name__ == "__main__":
    typer.run(main)
