from bs4 import BeautifulSoup
import requests


"""
:return dict with minimal keys:
    title
    price
    description
"""
def fetchData( query = "", location = "", radius = 0 ) -> list:
    session = requests.Session()

    domain = "https://www.ebay-kleinanzeigen.de/"
    URL = domain + "s-" + query.replace( " ", "-" ) + "/k0"
    print(f"{URL=}")

    r = session.get( URL, headers = {
        'referer': domain,
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7',
    },
                     timeout = 10,
                     cookies = {
                     } )


    site = BeautifulSoup( r.text, 'html.parser' )

    results = []

    for item in site.find_all( "li", {"class": "lazyload-item"} ):
        title = item.find( "a", {"class": "ellipsis"} )
        url = domain + title['href']
        try:
            img_src = item.find( "div", {"class": "srpimagebox"} )['data-imgsrcretina'].split(" ")[0]
        except:
            img_src = "https://upload.wikimedia.org/wikipedia/commons/d/d1/Image_not_available.png"
        description = item.find( "p", {"class": "aditem-main--middle--description"} ).text
        price = item.find( "p", {"class": "aditem-main--middle--price-shipping--price"} ).text.strip()
        results.append({
            'title': title.text,
            'img': img_src,
            'description': description,
            'price': price,
            'priceUnit': "EUR",
            'provider': "eBay Kleinanzeigen",
            'url': url,
            'color': "#91B53D"
        })

    return results

