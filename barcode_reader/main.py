from barcode_reader_functions import *


def main():
    barcode_data = barcode_readin()
    if barcode_data:
        barcode_from_mysql(barcode_data)


# product_url = 'https://bevasarlas.tesco.hu/groceries/hu-HU/products'

if __name__ == "__main__":
    main()
