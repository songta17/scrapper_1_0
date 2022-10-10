from bs4 import BeautifulSoup
import requests


def extract_product_data(host, url):
    """Extract data from product page
    Get the source code of the url product page and
    extract product data with Soup.

    Args:
        host (string): url protocol with the url domain
        url (string): url path

    Returns:
        list: Returns a list containing the product data extracted with Soup
    """

    # Generate the page with the url
    page = requests.get(host + url)
    soup = BeautifulSoup(page.content, "html.parser")

    # Create an empty product data list
    product_data = []

    # Concatenate and add the product_page_url to the product data list
    product_data.append(host + url)

    # Parse the data from Production Information section
    product_information = soup.find_all("td")

    # Add the universal_product_code to the product data list
    product_data.append(product_information[0].string)

    # Add the title of the product
    product_data.append(soup.find("h1").string)

    # Add the price_including_tax
    product_data.append(product_information[3].string)

    # Add the price_excluding_tax
    product_data.append(product_information[2].string)

    # Add the number_available
    product_data.append(product_information[5].string)

    # Add the product_description
    product_data.append([soup.select("article > p")[0].string])

    # Add the category
    product_data.append(product_information[1].string)

    # Extract and add the review_rating (number of star of the product)
    review_first_element = soup.find(class_="star-rating").attrs["class"]
    if "Five" in review_first_element:
        product_data.append(5)
    elif "Four" in review_first_element:
        product_data.append(4)
    elif "Three" in review_first_element:
        product_data.append(3)
    elif "Two" in review_first_element:
        product_data.append(2)
    else:
        product_data.append(1)

    # Extract, generate and add the image_url
    img_link = soup.find("img").attrs['src']
    image_url = host + img_link[6:len(img_link)]
    product_data.append(image_url)

    return product_data