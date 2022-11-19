import requests
from parsel import Selector


session = requests.Session()

def fetch(search_phrase):
    ret = []

    # webdriver = Chrome()
    url = "https://www.quoka.de/alle-rubriken/kleinanzeigen.html"
    payload = {
        "search1": search_phrase
    }
    # response = webdriver.request('POST', url, data=payload)

    # ret = response
    # ret = webdriver.find_element(by=By.XPATH, value='//*[@id="ResultListData"]/ul/li')

    response = requests.post(url, data=payload)
    sel = Selector(response.text)
    rows = sel.xpath('//*[@id="ResultListData"]/ul/li').getall()

    for row in rows:
        sel1 = Selector(row)
        img = sel1.xpath('//li/div/a/img/@data-src').getall()
        title = sel1.xpath('//li/div[2]/a//text()').getall()
        description = sel1.xpath('//li/div[2]/div//text()').getall()
        price = sel1.xpath('//li/div[3]/p[1]//text()').getall()
        price = price[0] if len(price) > 0 else ''
        postalCode = sel1.xpath('//li/div[3]/p[2]//span[contains(@class, "postal-code")]//text()').getall()
        date = sel1.xpath('//li/div[4]//text()').getall()
        ret.append({"img": img,
                    "title": title,
                    "description": description,
                    "price": price,
                    "zipCode": postalCode,
                    "date": date,
                    })

    # session = HTMLSession()
    # result_page = session.post(url, data=payload)
    #
    # for row in result_page.html.xpath('//*[@id="ResultListData"]/ul/li'):
    #     ret.append(row.getall())

    return ret

