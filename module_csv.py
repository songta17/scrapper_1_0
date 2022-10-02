import csv

HEADERS = [
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

# Create a CSV file and insert data inside
def create_csv(line):
  with open('data_books.csv', 'w') as fichier_csv:
    writer = csv.writer(fichier_csv, delimiter=',')
    writer.writerow(HEADERS)
    writer.writerow(line)