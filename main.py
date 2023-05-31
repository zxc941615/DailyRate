from crawler import Crawler

END_POINT = "https://rate.bot.com.tw/xrt?Lang=en-US"

if __name__ == "__main__":
    spider = Crawler()
    spider._get_exchange_rate_response(END_POINT)
    usd_rate = spider._parse_usd_spot_buying_rate()
