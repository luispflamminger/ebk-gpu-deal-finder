import argparse
import mechanicalsoup
import json
import os

SUPPORTED_GPUS = ["3060", "3060Ti", "3070", "3080"]

def main():
    args = parse_args()

    if args.ui == True:
        print("UI not implemented yet. Please use cli options.")
        return




def parse_args():
    parser = argparse.ArgumentParser(description='Ebay Kleinanzeigen GPU Deal Finder', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-u', '--ui', action="store_true", help='Choose the configuration using a user interface instead of cli options. (Recommended for manual usage and beginners)')
    parser.add_argument('-g', '--gpus', nargs="+", default=SUPPORTED_GPUS, help='The GPU models you want to include in your search. Default is all supported models.')
    parser.add_argument('-p', "--pages", default=10, type=int, help='The number of pages to search in. One page contains x items.')
    parser.add_argument('-o', "--outfile", nargs="?", type=argparse.FileType("w"), default=os.getcwd(), help='The path for the output file.')
    parser.add_argument('-z', '--zip-code', default='', nargs=1, help='Specify a zip code to search in. Default is all of Germany.')
    parser.add_argument('-r', '--radius', default='', nargs=1, help='Specify a search radius.')

    args = parser.parse_args()
    return args

if __name__ == "__main__":
    main()