from module_csv import create_csv
from module_scrapper import extract_data

host = "http://books.toscrape.com/"
url = "catalogue/sapiens-a-brief-history-of-humankind_996/index.html"

# SCRAPING DATA
line = extract_data(host, url)

# generate the csv with data result
create_csv(line)