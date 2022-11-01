from argparse import *
from Spider import Spider


parser = ArgumentParser(description="Web Spider")

parser.add_argument(
    "-i",
    "--input",
    dest="filename",
    required=True,
    help="input file containing the sites to be crawled",
    metavar="FILE",
)


args = parser.parse_args()

with open(args.filename,'r') as file:
	f = file.readlines()

for url in f:
    uon = Spider(url)
    uon.get_content()

