import json
import os

SUPPORTED_GPUS = ["3060", "3060Ti", "3070", "3080"]
BASE_URL = "https://www.ebay-kleinanzeigen.de/"

def main():
    args = parse_args()

    #UI not implemented yet
    if args.ui == True:
        print("UI not implemented yet. Please use cli options.")
        return

    #User entered incorrect GPU
    for el in args.gpus:
        if el not in SUPPORTED_GPUS:
            print("You entered an unsupported GPU Type. Here is a list of supported values") 
            print(SUPPORTED_GPUS)
            #return
    
    data = args.gpus

    for el in data:
        scrape(el, args.pages, args.zip_code, args.radius)
        el = []




def parse_args():
    import argparse

    parser = argparse.ArgumentParser(description='Ebay Kleinanzeigen GPU Deal Finder', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-u', '--ui', action="store_true", help='Choose the configuration using a user interface instead of cli options. (Recommended for manual usage and beginners)')
    parser.add_argument('-g', '--gpus', nargs="+", default=SUPPORTED_GPUS, help='The GPU models you want to include in your search. Default is all supported models.')
    parser.add_argument('-p', "--pages", default=10, type=int, help='The number of pages to search in. One page contains x items.')
    parser.add_argument('-o', "--outfile", nargs="?", type=argparse.FileType("w"), default=os.path.join(os.getcwd(), "outfile.ext"), help='The path for the output file.')
    parser.add_argument('-z', '--zip-code', default=None, type=int, nargs=1, help='Specify a zip code to search in. Default is all of Germany.')
    parser.add_argument('-r', '--radius', default=None, type=int, help='Specify a search radius.')

    args = parser.parse_args()
    print(args)
    return args

def scrape(gpu, pages, zip_code, radius):
    import mechanicalsoup
    
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