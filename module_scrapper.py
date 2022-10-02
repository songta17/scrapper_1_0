from bs4 import BeautifulSoup
import requests

def extract_data(host, url):
  page = requests.get(host + url)
  soup = BeautifulSoup(page.content, 'html.parser')
  result = []

  # product_page_url
  result.append(host + url)

  # universal_product_code
  product_information = soup.find_all("td")

  # print(product_information[0].string)
  result.append(product_information[0].string)

  # title
  result.append(soup.find('h1').string)

  # price_including_tax
  result.append(product_information[3].string)

  # price_excluding_tax
  result.append(product_information[2].string)

  # number_available
  result.append(product_information[5].string)

  # product_description
  result.append([soup.select("article > p")[0].string])

  # category
  result.append(product_information[1].string)

  # review_rating
  review_first_element = soup.find(class_="star-rating").attrs['class']
  if "Five" in review_first_element:
    result.append(5)
  elif "Four" in review_first_element:
    result.append(4)
  elif "Three" in review_first_element:
    result.append(3)
  elif "Two" in review_first_element:
    result.append(2)
  else:
    result.append(1)

  # image_url
  img_link = soup.find("img").attrs['src']
  image_url = host + img_link[6:len(img_link)]
  result.append(image_url)

  return result
