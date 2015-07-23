URL = r"http://onlinerechner.haude.at/bmf/brutto-netto-rechner-2013/json/2015/{gross}/Brutto/jaehrlich/0.00/0.00/Angestellter/0/false/0/0/steiermark/keine/0/false/false/true/74667770"


def run():
    import urllib
    import json

    with open("data.txt", "w") as fp:
        for gross in range(1000, 500000, 1000):
            r = urllib.urlopen(URL.format(gross=gross))
            netto = json.loads(r.read())['Netto_DN']['Jahr']
            tax = abs(100.0 - netto / gross * 100.0)
            data = "{gross};{netto};{tax:.2f}".format(gross=gross, netto=netto, tax=tax)
            print data
            fp.write(data + '\n')

if __name__ == "__main__":
    run()