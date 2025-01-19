from json import loads
from requests import get
from argparse import Namespace as ArgParsed, ArgumentParser

def fetch_data(id: str) -> dict:
    if id.startswith("http"):
        return loads(get(id).text)
    return loads(get(f"https://api.wooting.io/public/wootility/profiles?code={id}").text)

def argparser() -> ArgParsed:
    parser = ArgumentParser(prog="wootility-parser-fetcher", description="Parse Wooting profiles from Wootility Fetcher")
    parser.add_argument("id", help="The ID of the profile you want to fetch, obtain it by pressing share profile in Wootility", type=str)
    return parser.parse_args()

def main():
    args = argparser()
    data = fetch_data(args.id)
    print(data)

if __name__ == "__main__":
    main()
