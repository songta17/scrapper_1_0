from module_csv import create_csv, add_csv
from module_scrapper import extract_product, extract_products, extract_categories


class Run:
    """Running the application to extract all products details from all categories books
    """

      
    def runner():
        """Run the script to begin the scrapping
        """
        print("Data categories Start!")
        categories = extract_categories()

        for category in categories:
            # generate the category csv
            create_csv(category)
            print(category + ".csv created!")
            products = extract_products(category)
            for product_link in products:
                product = extract_product(product_link)
                add_csv(product, category)

        print("All products of each gategories extracted!")
