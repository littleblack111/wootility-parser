from fetch import fetch_data
from argparse import Namespace as ArgParsed, ArgumentParser
import logging
from sys import stdout

logging.basicConfig(level=logging.DEBUG, stream=stdout)
logger = logging.getLogger(__name__)

def argparser() -> ArgParsed:
    logger.debug("Parsing arguments")
    parser = ArgumentParser(prog="wootility-parser", description="Parse Wooting profiles from Wootility")
    parser.add_argument("id", help="The ID of the profile you want to fetch, obtain it by pressing share profile in Wootility", type=str)
    return parser.parse_args()

if __name__ == "__main__":
    args = argparser()
    profile = fetch_data(args.id)
