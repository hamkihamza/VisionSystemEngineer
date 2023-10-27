import openpyxl
import requests
import re

# Shopify store credentials
SHOPIFY_API_KEY = ''
SHOPIFY_ACCESS_TOKEN = ''
SHOPIFY_STORE_URL = ''

SHOPIFY_PRODUCT_CREATE_URL = ""

headers = {
    'Content-Type': 'application/json',
    'X-Shopify-Access-Token': SHOPIFY_ACCESS_TOKEN,
}

def extract_tag_name(tag_text):
    # Split the tag text based on ":" and take all parts except the first one
    tag_parts = tag_text.split(":")
    if len(tag_parts) > 1:
        tag_name = ":".join(tag_parts[1:]).strip()
    else:
        tag_name = None
    return tag_name

def read_excel_file(file_path):
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active

    products = []
    active_tag = None  # Initialize active tag as None

    for row in sheet.iter_rows(min_row=2, values_only=True):
        sku, title, price, barcode, stock_unit = row[1:6]  # Assuming the columns are in order

        # Skip rows where the title is blank
        if not title:
            continue

        # Initialize tags as an empty list
        tags = []

        # Check if the row contains a new tag (e.g., "ZONE #: TagName")
        if title:
            tag_parts = title.strip().split(":")
            if len(tag_parts) > 1:
                active_tag = extract_tag_name(title)
            elif active_tag:
                # If there's an active tag, use it as the tag for the product
                tags = [active_tag]

        product = {
            "title": title,
            "body_html": stock_unit,  
            "vendor": "Greenland Food",  
            "product_type": re.sub(r'\d+', '', active_tag),  
            "tags": tags,  
            "variants": [
                {
                    "sku": sku or "",
                    "price": price or 0.00,
                    "barcode": barcode or '',
                    "inventory_management": None,
                    "inventory_quantity": 0,  # Set to 0 to not track inventory
                    "inventory_policy": "deny",  
                    "inventory_item_id": sku,  
                    "requires_shipping": True,  
                    "fulfillment_service": "manual",  
                }
            ],
        }
        products.append(product)

    return products
            

def create_shopify_products(products):
    for product in products:
        response = requests.post(
            SHOPIFY_PRODUCT_CREATE_URL,
            json={"product": product},
            headers=headers,
        )

        if response.status_code == 201:
            print(f"Product '{product['title']}' created successfully.")
        else:
            print(f"Failed to create product '{product['title']}': {response.status_code} - {response.text}")


if __name__ == "__main__":
    excel_file_path = "products.xlsx"  # Replace with your Excel file path
    products = read_excel_file(excel_file_path)
    create_shopify_products(products)

