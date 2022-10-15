from bs4 import BeautifulSoup
import requests
# from module_img import saving_book_illustration

HOST = "https://books.toscrape.com/"


def extract_product_datas(url):
    """Extract datas from product page
    Get the source code of the url product page and
    extract product data with Soup.

    Args:
        url (string): url path

    Returns:
        list: Returns a list containing the product data extracted with Soup
    """

    # Generate the page with the url
    page = requests.get(HOST + url)
    soup = BeautifulSoup(page.content, "html.parser")

    # Create an empty product data list
    product_datas = []

    # Concatenate and add the product_page_url to the product data list
    product_datas.append(HOST + url)

    # Parse the data from Production Information section
    product_information = soup.find_all("td")

    # Add the universal_product_code to the product data list
    product_datas.append(product_information[0].string)

    # Add the title of the product
    product_datas.append(soup.find("h1").string)

    # Add the price_including_tax
    product_datas.append(product_information[3].string)

    # Add the price_excluding_tax
    product_datas.append(product_information[2].string)

    # Add the number_available
    product_datas.append(product_information[5].string)

    # Add the product_description
    product_datas.append(soup.select("article > p")[0].string)

    # Add the category
    product_datas.append(product_information[1].string)

    # Extract and add the review_rating (number of star of the product)
    review_first_element = soup.find(class_="star-rating").attrs["class"]
    if "Five" in review_first_element:
        product_datas.append(5)
    elif "Four" in review_first_element:
        product_datas.append(4)
    elif "Three" in review_first_element:
        product_datas.append(3)
    elif "Two" in review_first_element:
        product_datas.append(2)
    else:
        product_datas.append(1)

    # Extract, generate and add the image_url
    img_link = soup.find("img").attrs['src']
    image_url = HOST + img_link[6:len(img_link)]
    product_datas.append(image_url)

    return product_datas


def get_link_products(name_category):
    """Extract all link of products from a category.

    Args:
        name_category (string): Contains the name of the category

    Returns:
        list: Returns a list containing the urls of all products of a category
    """
    # Generate the page of the category with the url
    url = HOST + "catalogue/category/books/" + name_category + "/index.html"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    # Create a list of products urls of the category
    products_urls = []

    multiple_page = soup.find(class_="current")
    if multiple_page is None:
        pagination = 1
    else:
        # Extract the number of page for this category
        pagination = int(soup.find(class_="current").string.strip()[-1])

    # Iterate through all pages
    for number in range(pagination):
        # Extract urls
        urls_category = soup.select("article > h3 > a")

        # print(urls_category)
        for item in urls_category:
            item_url = item.attrs['href']
            product_url = "catalogue" + item_url[8:len(item_url)]
            products_urls.append(product_url)

    return products_urls


def extract_name_categories():
    """Extract all name categories of books

    Returns:
        list: a list of all categories name
    """
    # Generate the page of the category with the url
    page = requests.get(HOST)
    soup = BeautifulSoup(page.content, "html.parser")

    # Create a list of categories
    name_categories = []

    # Extract all categories
    items = soup.select("aside > div > ul > li > ul > li > a")
    for x in items:
        item_url = x.attrs['href'].split("/")
        name_categories.append(item_url[-2])

    return name_categories
