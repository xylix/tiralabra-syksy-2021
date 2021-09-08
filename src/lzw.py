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

def compress():
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
def decompress():
    pass

def main():
    print("hello world")

if __name__ == "__main__":
    main()
