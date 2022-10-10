import requests


def saving_book_illustration(url):
    """save the image of the book in the folder img

    Args:
        url (string): Contains the source of the image of the Book.
    """
    response = requests.get(url)
    picture = url.split("/")

    with open("img/" + picture[-1], "wb") as fichier_csv:
        fichier_csv.write(response.content)
