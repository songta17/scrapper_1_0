from module_csv import create_csv, add_csv
from module_scrapper import extract_product, extract_products, extract_categories

# product_url = "catalogue/sapiens-a-brief-history-of-humankind_996/index.html"

# # Scrapping product data
# print("Data product Start!")
# # SCRAPING DATA
# product_data = extract_product_data(product_url)
# add_csv(product_data)
# print("Data product extracted!")


# print("Data products Start!")
# # Scrapping products of a category
# url_pagination = "catalogue/category/books/mystery_3/page-1.html"
# urls_category = extract_products_data(url_pagination)

# for url in urls_category:
#     product_data = extract_product_data(url)
#     add_csv(product_data)
# print("Data products extracted!")

print("Data categories Start!")
categories = extract_categories()

for categorie in categories:
    # generate the csv with data result
    create_csv(categorie)
    products = extract_products(categorie)
    for product_link in products:
        product = extract_product(product_link)
        add_csv(product, categorie)
print("Data categeries extracted!")
