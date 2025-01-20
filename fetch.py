from json import loads
from requests import get
from argparse import Namespace as ArgParsed, ArgumentParser
import logging

logger = logging.getLogger(__name__)

def fetch_data(id: str) -> dict:
    if id.startswith("http"):
        logger.debug(f"Fetching data from URL {id}")
        return loads(get(id).text)
    logger.info(f"Fetching data for ID {id}")
    return loads(get(f"https://api.wooting.io/public/wootility/profiles?code={id}").text)

def argparser() -> ArgParsed:
    logger.debug("Parsing arguments")
    parser = ArgumentParser(prog="wootility-parser-fetcher", description="Parse Wooting profiles from Wootility Fetcher")
    parser.add_argument("id", help="The ID of the profile you want to fetch, obtain it by pressing share profile in Wootility", type=str)
    return parser.parse_args()

def main():
    args = argparser()
    data = fetch_data(args.id)
    logger.debug(f"Fetched data: {data}")
    print(data)

if __name__ == "__main__":
    main()
