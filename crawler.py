import requests
from bs4 import BeautifulSoup


class Crawler:
    def __init__(self):
        self.response = None

    def _get_exchange_rate_response(self, end_point: str):
        self.response = requests.get(end_point)

    def _parse_usd_spot_buying_rate(self) -> float:
        soup = BeautifulSoup(self.response.text, "html.parser")
        usd_spot_buying_td = (
            soup.find("table")
            .find("tbody")
            .find_all("tr")[0]
            .select(".rate-content-sight")[0]
        )
        usd_spot_buying_rate = round(float(usd_spot_buying_td.get_text("td")), 2)
        return usd_spot_buying_rate
