import os

def generate_folder():
    if not os.path.exists("lib/img/"):
        os.makedirs("lib/img/")
    if not os.path.exists("lib/csv/"):
        os.makedirs("lib/csv/")