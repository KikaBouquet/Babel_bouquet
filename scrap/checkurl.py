import requests
import json
import os
from bs4 import BeautifulSoup

dataset = []
F_URL = "url"
F_STATUS = "statut_code"
F_HTML = "content"
F_TITLE = "title"
F_H1 = "h1"
F_H2 = "h2"


def get(url):
    """
    récupère le requests.get d'un url
    """
    user_agent_text = ""  # mettre le user-agent correspondant à son navigateur
    headerdict = {"User-Agent": user_agent_text}
    r = requests.get(url, headers=headerdict)
    r.raise_for_status
    return r


def displayurl(r, is_verbose=False):
    """
    affichage 
    """
    print(r)
    print(f"il y a {len(r.text)} octets")
    # print(r.text)

    if is_verbose:
        print(r.status_code)
        print(r.headers["content-type"])
        for key, value in r.headers.items():
            print(f"{key} : {value}")


def write_to_dict(r, is_verbose=False):
    """
    récupère le texte, le statut et les <meta> d'une url
    retourne un dict
    """
    text = r.text
    meta_dict = search_meta_by_bs4(text)
    meta_dict.update({F_URL: r.url, F_STATUS: r.status_code})
    global dataset
    dataset.append(meta_dict)


def search_meta_by_bs4(text):
    """
    trouve <title> et les <meta> dont les proproétés sont og:title, og:description, og:image
    retourne tout dans un dict
    """
    soup = BeautifulSoup(text, "lxml")
    title = soup.title.string
    image_og = soup.find("meta", property="og:image")
    title_og = soup.find("meta", property="og:title")
    description_og = soup.find("meta", property="og:description")
    title_og = soup.find("meta", property="og:title")
    meta_dict = dict()
    if title:
        meta_dict[F_TITLE] = title
    if title_og:
        meta_dict["title_og"] = title_og["content"]
    if description_og:
        meta_dict["description_og"] = description_og["content"]
    if image_og:
        meta_dict["image_og"] = image_og["content"]

    # fin de matinée
    d = soup.find_all("h1")
    if d:
        meta_dict[F_H1] = []
        for h1 in d:
            meta_dict[F_H1].append(h1.text)
            print(f"--> h1 {h1.text}")
    d = soup.find_all("h2")
    if d:
        meta_dict[F_H2] = []
        for h2 in d:
            meta_dict[F_H2].append(h2.text)
            print(f"---> h2 {h2.text}")

    # fin du matinée
            
    return meta_dict


"""
def search_title_by_bs4(text):
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
"""

""" 
def search_title(text):  
    to_return = begin = end = 0
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
    """
    pour un liste d'url
    exécute display url et write_to_dict si les urls sont ok
    """
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


"""
A AJOUTER
def search_meta(text):
    ''' recherche les éléments méta: Title, description, url, url_image dans un fichier html avec Beautifulsoup4:
     renvoie un dictionnaire: dict_meta  '''
    dict_meta = {}
    ''' problème d'encodage é ou è 
    https://outils-javascript.aliasdmc.fr/encodage-caracteres-accentues/encode-caractere-00E9-html-css-js-autre.html
     '''
    text = text.replace("Ã©", "é")
    text = text.replace("â", "'")
    soup = BeautifulSoup(text, "lxml")
    tit = soup.find("meta", property="og:title")
    if not tit:
        title = soup.title.string
    else:
        title = tit["content"]

    descr = soup.find("meta", property="og:description")
    description = descr["content"] if descr else ""

    ur = soup.find("meta", property="og:url")
    url = ur["content"] if ur else ""

    im = soup.find("meta", property="og:image")
    image = im["content"] if im else ""

    dict_meta = {F_DESCRIPTION: description,
                 F_IMAGE: image, F_URL: url, F_TITLE: title}
    return dict_meta
    """


if __name__ == "__main__":

    urls = ["https://google.fr", "https://midilibre.fr", "https://thetimes.co.uk", "https://www.20minutes.fr/", "https://www.lemonde.fr", "https://www.youtube.com/?hl=fr&gl=FR",
                    "https://www.ouest-france.fr", "https://www.python.org/"]
    get_urls(urls, False)
    print(len(dataset))
    print(__file__)
    filedir = (os.path.abspath(__file__))
    print(filedir)
    basedir = (os.path.dirname(filedir))
    print(basedir)
    dataset_dir = {"count": len(dataset), "dataset": dataset}
    filename = basedir + "/checkurl.json"

    # with permet d'éviter de faire close("test.json"... etc)
    with open(filename, "w", encoding="utf8") as f:
        json.dump(dataset_dir, f)  # prend un objet python et un handle de fichier et écrit dedant
        print(f"{filename} : SUCCESS")
