from module_csv import create_csv, add_csv
from module_scrapper import extract_product, extract_products, extract_categories
from module_img import saving_book_illustration

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
                # extract data from a product link
                product = extract_product(product_link)
                # add the data informations about a product
                add_csv(product, category)
                # saving the picture
                saving_book_illustration(product[-1])

        print("All products of each gategories extracted!")
