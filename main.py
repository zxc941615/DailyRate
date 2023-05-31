from crawler import Crawler
from dotenv import load_dotenv
import os

END_POINT = "https://rate.bot.com.tw/xrt?Lang=en-US"

if __name__ == "__main__":
    load_dotenv("./local.env")
    spider = Crawler()
    spider._get_exchange_rate_response(END_POINT)
    usd_rate = spider._parse_usd_spot_buying_rate()
    secret = os.getenv("NOTION_SECRET")
