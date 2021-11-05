import json
import os
import argparse
import sys
import mechanicalsoup

SUPPORTED_GPUS = ["3060", "3060Ti", "3070", "3080"]
BASE_URL = "https://www.ebay-kleinanzeigen.de/"

def main():
    
    ### parse arguments ###    
    parser = argparse.ArgumentParser(description='Ebay Kleinanzeigen GPU Deal Finder', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-u', '--ui', action="store_true", help='Choose the configuration using a user interface instead of cli options. (Recommended for manual usage and beginners)')
    parser.add_argument('-g', '--gpus', nargs="+", default=SUPPORTED_GPUS, help='The GPU models you want to include in your search. Default is all supported models.')
    parser.add_argument('-p', "--pages", default=10, type=int, help='The number of pages to search in. One page contains x items.')
    parser.add_argument('-o', "--outfile", nargs="?", type=argparse.FileType("w"), default=os.path.join(os.getcwd(), "outfile.ext"), help='The path for the output file.')
    parser.add_argument('-z', '--zip-code', default=None, type=int, nargs=1, help='Specify a zip code to search in. Default is all of Germany.')
    parser.add_argument('-r', '--radius', default=None, type=int, help='Specify a search radius.')

    args = parser.parse_args()


    ### Handle input ###
    
    # UI not implemented yet
    if args.ui == True:
        print("UI not implemented yet. Please use cli options.")
        return

    #User entered incorrect GPU
    for el in args.gpus:
        if el not in SUPPORTED_GPUS:
            sys.exit("You entered an unsupported GPU Type. Here is a list of supported values:\n" + SUPPORTED_GPUS)
    
    pages = args.pages
    zip_code = args.zip_code
    radius = args.radius
    gpus = args.gpus


    ### Start scraping ###

    for gpu in gpus:
        browser = mechanicalsoup.StatefulBrowser(
            soup_config={'features': 'html5lib'},
            raise_on_404=True,
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"
        )

        browser.open(BASE_URL)
        #browser.select_form('#site-search-form')
        print(browser.page.find_all("form"))
        browser.close()


if __name__ == "__main__":
    main()