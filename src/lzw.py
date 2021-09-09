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


def compress(input_data) -> str:
    """
    Creates a compressed file named {filename}.lzw
    """
    output = []
    dictionary = START_DICT.copy()
    s = ""
    for i, ch in enumerate(input_data):
        logging.debug(f"character at index {i}: {ch}")
        logging.debug(f"s+ch ({s+ch}) in dict: {dictionary.get(s+ch)}")

        if dictionary.get(s + ch):
            s = s + ch
        else:
            # FIXME: This generates an extra comma at the end of the out file
            output.append(str(dictionary[s]))
            # TODO: this might be incorrect
            dictionary[s + ch] = len(dictionary.items())
            s = ch
    logging.debug(f"dict: {dictionary}")
    return ",".join(output)


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


def decompress(input_data: str) -> str:
    """
    extracts and .lzw file into {filename}.out
    """
    output = ""
    dictionary = START_DICT.copy()
    splat = input_data.split(",")
    prevcode = splat[0]
    for i, currcode in enumerate(splat):
        logging.debug(f"currcode at index {i}: {currcode}")
        entry = list(dictionary.keys())[int(currcode)]
        output += entry
        ch = entry[0]
        dictionary[prevcode + ch] = len(dictionary.items())
        prevcode = currcode

    return output


def main(
    filename: str,
    archive: bool = True,
    extract: bool = False,
    debug: bool = True,
    write_to_file: bool = False,
):
    if archive and extract:
        raise ValueError("Either archive or extract, not both")
    if debug:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.WARNING)
        # logging.debug(f"Argument List: {sys.argv}")
        if archive or extract:
            with open(filename, "r") as f:
                if archive:
                    output = compress(f.read())
                    outf_name = f"{filename}.lzw"
                else:
                    output = decompress(f.read())
                    outf_name = f"{filename}.out"
        else:
            raise ValueError("No operation specified")
    if write_to_file:
        with open(outf_name, "w") as outf:
            outf.write(output)
    logging.debug(f"Created output: `{output}`")


if __name__ == "__main__":
    typer.run(main)
