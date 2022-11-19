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
    # print(f"{r.text=}")


    site = BeautifulSoup( r.text, 'html.parser' )

    results = []

    for item in site.find_all( "li", {"class": "lazyload-item"} ):
        # l = site.find_all( "li", {"class": "lazyload-item"} )
        # print("l[0].html")
        # print(l[0].html)
        # print("l[0].text")
        # print(l[0].text)
        # print("l[0].getText")
        # print(l[0].getText)
        # print(f"{l[0].article.getText=}")

        print()
        print()
        print(str(item.select("div")))

        # item_parsed = BeautifulSoup( str(item.article), 'html.parser' )
        # parsed = BeautifulSoup( item.html, 'html.parser' )

        title = item.find( "a", {"class": "ellipsis"} )
        img_source = item.find( "div", {"class": "srpimagebox"} )['data-imgsrc']
        results.append({
            'title': title.text,

        })


    print(results)

    return results

