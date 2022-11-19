from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic


def index(request):
    return render(request, "app_metamarkt/index.html")


def search(request):
    if request.method == "GET":
        search_phrase = request.GET.get('q', None)
        if search_phrase:
            results = [{
                        'title': 'Akkordeon Hohner Morino IV N',
                        'description': '''Akkordeon wie neu mit Original-Koffer und gepolsterte Riemen
                                        Grifftechnik Piano
                                        Basstechnik Standardbass
                                        Klangtechnik Cassotto
                                        Stimmplattenqualitaet TAM
                                        Stimmung 16' 8' 8' 4'
                                        Farbe schwarz
                                        Diskanttasten 41
                                        Diskantchoere IV
                                        Bassknoepfe 120
                                        Basschoere V
                                        Gewicht 11,9 kg
                                        Register Diskant 11
                                        Register Bass 5
                                        Tonumfang F - a

                                            Abmessungen 19 x 49 cm
                                            
                                            Da Privatverkauf keine Garantie und Rücknahme.''',
                        'price': 2900,
                        'priceUnit': 'EUR',
                        'zipCode': 80939,
                        'date': "08.10.2022",
                        'views': 232
            },
                {
                    'title': 'Akkordeon Hohner Concerto 1 rot, guter Zustand mit Koffer',
                    'description': '''Dieses Akkordeon wurde leider sehr wenig gespielt und stand lange Zeit in der Wohnzimmer Ecke meiner Eltern. Es hat 26 Diskanttasten und 48 Bassknöpfe. Mit einem Gewicht von 4,7 Kilogramm ist es äußerst beliebt bei Anfängern und fortgeschrittenen Spielern. Bis auf eine leichte Delle (siehe Foto) hat es kaum Gebrauchsspuren, nichts ist ausgeleiert oder gar zerschlissen. Der Koffer hat deutlichere Gebrauchsspuren, lässt sich aber noch sauber öffnen und schließen (keine Schlüssel vorhanden). Interessenten sind herzlich eingeladen, das Instrument in Ruhe probezuspielen.
In unserem Hauhalt gibt es keine Tiere, wir sind Nichtraucher. Verkauf erfolgt von privat, keine Garantie oder Rücknahme. Ich möchte das Instrument nicht verschicken, daher bitte ich um Abholung in Oberschleißheim. Und weil es viele Interessenten ignorieren wiederhole ich es nochmal: KEIN VERSAND - NUR ABHOLUNG''',
                    'price': 299,
                    'priceUnit': 'EUR',
                    'zipCode': 85764,
                    'date': "03.11.2022",
                    'views': 115
                }]
        else:
            results = None
        return render(request, "app_metamarkt/search.html", {"results": results})


