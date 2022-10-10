import csv

PRODUCT_PAGE_HEADERS = [
  "product_page_url", 
  "universal_product_code", 
  "title", 
  "price_including_tax", 
  "price_excluding_tax", 
  "number_available", 
  "product_description", 
  "category", 
  "review_rating", 
  "image_url"]


def create_csv():
    """Generate the CSV containing data extracted on the product page.

    Args:
      data (list): It contains all data of a product
    """
    # Create/open a csv to insert headers and data
    with open('data_books.csv', 'w') as fichier_csv:
        writer = csv.writer(fichier_csv, delimiter=',')
        writer.writerow(PRODUCT_PAGE_HEADERS)


def add_csv(data):
    """Add datas extracted in the existing csv.

    Args:
      data (list): It contains all data of a product
    """
    with open('data_books.csv', 'a') as fichier_csv:
        writer = csv.writer(fichier_csv, delimiter=',')
        writer.writerow(data)