import requests
from selectorlib import Extractor
from edisubot.sql import SQL

def scrape():
    "Ottieni tutti gli avvisi dal sito"

    HEADERS = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Cookie': 'cconsent={"version":1,"categories":{"necessary":{"wanted":true},"analytics":{"wanted":true},"social":{"wanted":true}},"services":["ganalytics","smartadserver","youtube"]}',
        'If-Modified-Since': 'Sat, 29 Oct 2022 09:05:49 GMT',
        'If-None-Match': '"1667034349-0"',
        'Referer': 'https://www.edisu.piemonte.it/it/notizie/scadenze',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"'
    }

    URL = "https://www.edisu.piemonte.it/it/notizie/avvisi"

    # Create an Extractor by reading from the YAML file
    e = Extractor.from_yaml_file('edisubot/selectors/avvisi.yml')

    r = requests.get(URL, headers = HEADERS)

    # Pass the HTML of the page and create 
    return e.extract(r.text)

def fetch():
    avvisi = scrape()
    sql = SQL('avvisi_edisu.db')
    sql.execute("")

    
