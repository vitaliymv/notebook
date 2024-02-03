import sqlite3
from sqlite3 import Error

from notebook.settings import DATABASES


def get_products_from_database():
    try:
        conn = sqlite3.connect(DATABASES['default']['NAME'])
        select_query = (f"SELECT "
                        f"p.name AS 'Product name', "
                        f"m.name AS 'Manufacturer', "
                        f"p.price AS 'Price', "
                        f"u.username AS 'Seller username' "
                        f"FROM core_product p "
                        f"JOIN core_manufacturer m ON p.manufacturer_id = m.id "
                        f"JOIN auth_user u ON p.seller_id = u.id ")
        cursor = conn.cursor()
        cursor.execute(select_query)
        products = cursor.fetchall()
        print(products)
        cursor.close()
        conn.close()
    except Error as e:
        print(f"The error {e} occurred")

