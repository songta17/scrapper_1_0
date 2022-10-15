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


def create_csv(name_category):
    """Generate the CSV containing data extracted on the product page.

    Args:
      name_category (string): It contains all data of a product
    """ 
    # Path
    # path = os.path.join(parent_dir, directory)

    # Create/open a csv to insert headers and data
    with open("lib/csv/" + name_category + ".csv", "w") as fichier_csv:
        writer = csv.writer(fichier_csv, delimiter=",")
        writer.writerow(PRODUCT_PAGE_HEADERS)
    print(name_category + ".csv created!")


def add_csv(product_datas, name_category):
    """Add datas extracted in the existing csv.

    Args:
      product_datas (list): It contains a list of all data of a product
    """
    print(type(product_datas))
    with open("lib/csv/" + name_category + ".csv", "a") as fichier_csv:
        writer = csv.writer(fichier_csv, delimiter=",")
        writer.writerow(product_datas)