import requests
import json
import os
from bs4 import BeautifulSoup

dataset = []
F_URL = "url"
F_STATUS = "statut_code"
F_HTML = "content"
F_TITLE = "title"


def get(url):
    user_agent_text = ""  # mettre le user-agent correspondant à son navigateur
    headerdict = {"User-Agent": user_agent_text}
    r = requests.get(url, headers=headerdict)
    r.raise_for_status
    return r


def displayurl(r, is_verbose=False):
    print(r)
    print(f"il y a {len(r.text)} octets")
    # print(r.text)

    if is_verbose:
        print(r.status_code)
        print(r.headers["content-type"])
        for key, value in r.headers.items():
            print(f"{key} : {value}")


def write_to_dict(r, is_verbose=False):
    text = r.text[:5000]
    title = search_title(text)
    dict = {F_URL: r.url, F_STATUS: r.status_code, F_TITLE: title, F_HTML: text}
    global dataset
    dataset.append(dict)


def search_title_by_bs4(text):
    """
    le retour du texte acceptera les accents et les char spéciaux
    utilisation de beautifulSoup4
    """
    soup = BeautifulSoup(text, "lxml")
    
    # a revoir
    d1 = soup.find_all('h1')
    d2 = soup.find_all('h2')
    if d1 != "":
        for h1 in d1:
            print(f"-->{h1}")
    if d2 != "":
        for h2 in d2:
            print(f"---->{h2}")
    # a revoir

    return soup.title.string


def search_title(text):
    return search_title_by_bs4(text)
    
    # ne pas utiliser cette suite de code

    """ to_return = begin = end = 0
    begin = text.find('<title>')
    if begin != -1:
        begin += len("<title>")
        end = text[begin:].find("</title>")
        if end != -1:
            end += begin 
            to_return = text[begin:end]
    print(f"le title est {begin}, {end}, {to_return}")

    return to_return
    """


# pas la peine de faire un test unitaire puisqu'on a deja la gestion des
# erreurs avec le try/except
def get_urls(arglist, is_verbose=False):

    for a in arglist:
        try:
            r = get(a)
        except Exception as e:
            print(f"erreur de requette vers {a}")
            print(str(e))
            r = None

        if r:
            displayurl(r, is_verbose)
            write_to_dict(r, is_verbose)


if __name__ == "__main__":

    urls = ["https://google.fr", "https://lemonde.fr", "https://facebook.com"]
    get_urls(urls, False)
    print(len(dataset))
    print(__file__)
    filedir = (os.path.abspath(__file__))
    print(filedir)
    basedir = (os.path.dirname(filedir))
    print(basedir)

    filename = basedir + "/checkurl.json"

    # with permet d'éviter de faire close("test.json"... etc)
    with open(filename, "w", encoding="utf8") as f:
        json.dump(dataset, f)  # prend un objet python et un handle de fichier et écrit dedant
