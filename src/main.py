from enum import Enum
import logging
from pathlib import Path
import sys
from typing import Tuple

import typer

from . import lzw
from . import huffman


SUPPORTED_ARCHIVES = [".lzw", ".huffman"]
# TODO: add more supported input types, specifically UTF-8
FILETYPES_TO_ARCHIVE = [".txt"]


class Algorithm(Enum):
    "Supported encoding and decoding algorithms."
    LZW = "lzw"
    HUFFMAN = "huffman"
    COMBO = "combo"


def _determine_module_from_algo(algo: Algorithm):
    """ """
    if algo == Algorithm.LZW:
        return lzw
    elif algo == Algorithm.HUFFMAN:
        return huffman
    elif algo == Algorithm.COMBO:
        return None
    else:
        raise TypeError("Invalid algorithm specified")


def _determine_module_from_suffix(suffix: str):
    """Determine compression / decompression module to use from given suffix."""
    if suffix == ".lzw":
        return lzw
    elif suffix == ".huffman":
        return huffman
    else:
        return None


def _decompress(module, filename, input_data: bytes) -> Tuple[bytes, str]:
    output = module.decompress(input_data)
    outf_name = f"{filename}.out"

    print(
        f"Decompressed {len(input_data)} bytes to {len(output)} bytes, ratio: { len(output) / len(input_data) }"
    )
    return output, outf_name


def _compress(module, filename: str, input_data: bytes, combo: bool):
    if combo:
        output = huffman.compress(lzw.compress(input_data))
        outf_name = f"{filename}.lzw.huffman"
    else:
        output = module.compress(input_data)
        outf_name = f"{filename}.{module.ALGORITHM_NAME}"
    print(
        f"Compressed {len(input_data)} bytes to {len(output)} "
        f"bytes, ratio: { len(output) / len(input_data) }"
    )

    return output, outf_name


def _auto_operate(algo, filename: str) -> Tuple[bytes, str]:
    infile = Path(filename)
    # If we are using operation.AUTO we override from the parameter,
    # IF the infile has a suffix that corresponds to an algorithm
    module = _determine_module_from_suffix(
        infile.suffix
    ) or _determine_module_from_algo(algo)

    logging.debug(f"Suffix: `{infile.suffix}`")
    with open(infile, "rb") as file:
        input_data = file.read()

    if infile.suffix in SUPPORTED_ARCHIVES:
        return _decompress(module, filename, input_data)
    elif infile.suffix in FILETYPES_TO_ARCHIVE:
        return _compress(module, filename, input_data, algo == algo.COMBO)
    else:
        raise ValueError(f"Filetype of {filename} is not yet supported")


# The type ignores for enum params are necessary because typer has problems with enum default values
def main(
    filename: str,
    debug: bool = False,
    write_to_file: bool = False,
    algo: Algorithm = "huffman",  # type: ignore
):
    """
    LZW modules entry point
    """
    if debug:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.WARNING)

    logging.debug(f"Argument List: {sys.argv}")
    logging.debug(f"locals: {locals()}")

    output, outf_name = _auto_operate(algo, filename)

    if write_to_file:
        # TODO: figure out a more efficient storage format for the compressed output
        # maybe check https://docs.python.org/3/library/codecs.html
        with open(outf_name, "wb") as outf:
            outf.write(output)

    if len(output) < 16000:
        print(f"Created output: `{output}`")
    elif not write_to_file:
        print("Output quite long to print, please use --write-to-file")


if __name__ == "__main__":
    typer.run(main)
