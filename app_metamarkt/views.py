from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
from app_metamarkt.marketplace_clients import quoka, ebay_kleinanzeigen


def index(request):
    return render(request, "app_metamarkt/index.html")


def search(request):
    if request.method == "GET":
        search_phrase = request.GET.get('q', None)
        if search_phrase:
            results = []
        #     results = [
        #         {
        #                 'title': 'BMW M4',
        #                 'description': '''
        #                 I'm selling this BMW because I drive it not that often.
        #                 ''',
        #                 'price': 30000,
        #                 'priceUnit': 'EUR',
        #                 'zipCode': 80939,
        #                 'date': "08.10.2022",
        #                 'views': 232,
        #                 'provider': "Mobile.de",
        #                 'url': "https://suchen.mobile.de/fahrzeuge/details.html?id=356164356"
        #         },
        #         {
        #             'title': 'BMW M3',
        #             'description': '''
        #             This great BMW in Alpine white has never disappointed me.
        #             ''',
        #             'price': 66000,
        #             'priceUnit': 'EUR',
        #             'zipCode': 85764,
        #             'date': "03.11.2022",
        #             'views': 115,
        #             'provider': "ebay-kleinanzeigen",
        #             'url': "https://www.ebay-kleinanzeigen.de/s-anzeige/bmw-m3-f80-competition/2276986346-216-6479"
        #         },
        #         {
        #             'title': 'BMW M3',
        #             'description': '''
        #             This great BMW in Alpine white has never disappointed me.
        #             ''',
        #             'price': 66000,
        #             'priceUnit': 'EUR',
        #             'zipCode': 85764,
        #             'date': "03.11.2022",
        #             'views': 115,
        #             'provider': "ebay-kleinanzeigen",
        #             'url': "https://www.ebay-kleinanzeigen.de/s-anzeige/bmw-m3-f80-competition/2276986346-216-6479"
        #         }]
            results = ebay_kleinanzeigen.fetchData(search_phrase)
            results.extend(quoka.fetch(search_phrase))
        else:
            results = None
        return render(request, "app_metamarkt/search.html", {"results": results})


