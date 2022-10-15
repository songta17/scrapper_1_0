from module_csv import create_csv, add_csv
from module_scrapper import extract_product_datas, extract_link_products, extract_name_categories
from module_img import saving_book_illustration
from module_folder import generate_folder
from module_benchmark import start_time, end_time


class Run:
    """Running the application to extract all products details from all categories books
    """

      
    def launch_scrapper():
        """Run the script to begin the scrapping
        """
        start = start_time()
        # generate folder for img and csv
        generate_folder()

        name_categories = extract_name_categories()
        
        for name_category in name_categories:
            # generate the category csv
            create_csv(name_category)
            products_links = extract_link_products(name_category)
            for product_link in products_links:
                # extract data from a product link
                product_datas = extract_product_datas(product_link)
                # add the data informations about a product
                add_csv(product_datas, name_category)
                # saving the picture
                saving_book_illustration(product_datas[-1])

        print("All products of each gategories extracted!")
        end_time(start)
          