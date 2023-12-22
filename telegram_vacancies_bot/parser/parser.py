import requests
from bs4 import BeautifulSoup
import re


def parser(url: str, output_path: str) -> None:
    HEADERS = {
        "authority": "www.kith.com",
        "cache-control": "max-age=0",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36",
        "sec-fetch-dest": "document",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "sec-fetch-site": "same-origin",
        "sec-fetch-mode": "navigate",
        "sec-fetch-user": "?1",
        "accept-language": "en-US,en;q=0.9",
    }

    session = requests.session()
    response = session.get(url, headers=HEADERS)
    soup = BeautifulSoup(response.text, "html.parser")
    vacancy_description = soup.find_all(attrs={"data-qa": "vacancy-description"})[
        0
    ].text
    all_text = []
    for text in soup.find(attrs={"data-qa": "vacancy-description"}).find_all("p"):
        all_text.append(text.text)
    vacancy = " ".join(all_text)

    with open(output_path, "w") as file:
        file.writelines(vacancy)
