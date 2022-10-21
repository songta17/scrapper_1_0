import requests


def saving_book_illustration(url, counter, title):
    """save the image of the book in the folder img

    Args:
        url (string): Contains the source of the image of the Book.
    """
    response = requests.get(url)
    
    with open("lib/img/" + str(counter) + "_" + title, "wb") as img:
        img.write(response.content)
