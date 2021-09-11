from enum import Enum
import logging
import pickle

import typer

from . import lzw
from . import huffmann


class Algorithm(Enum):
    lzw = "lzw"
    huffmann = "huffmann"


def main(
    filename: str,
    archive: bool = False,
    extract: bool = False,
    debug: bool = True,
    write_to_file: bool = False,
    compression_algorithm: Algorithm = Algorithm.huffmann,
):
    """
    LZW modules entry point
    """

    if compression_algorithm == Algorithm.lzw:
        module = lzw
    elif compression_algorithm == Algorithm.huffmann:
        module = huffmann
    else:
        raise Exception("Invalid module specified")

    if archive and extract:
        print("Either archive or extract, not both")
        return
    if debug:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.WARNING)
    # logging.debug(f"Argument List: {sys.argv}")
    if archive or extract:
        if archive and ".lzw" in filename:
            print("Do not archive already archived files")
            return

        if extract and ".lzw" not in filename:
            filename = filename + ".lzw"
        # TODO: does the encoding do anything when working with binary
        with open(filename, "rb") as file:
            if archive:
                output = module.compress(pickle.load(file))
                outf_name = f"{filename}.{compression_algorithm}"
            else:
                output = module.decompress(pickle.load(file))
                outf_name = f"{filename}.out"
    else:
        print("No operation specified")
        return
    if write_to_file:
        # TODO: figure out a more efficient storage format for the compressed output
        # maybe check https://docs.python.org/3/library/codecs.html
        with open(outf_name, "wb") as outf:
            pickle.dump(output, outf)
    logging.debug(f"Created output: `{output}`")


if __name__ == "__main__":
    typer.run(main)
