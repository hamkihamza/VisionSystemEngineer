import pandas as pd
from fuzzywuzzy import fuzz

# Load the CSV file into a DataFrame
csv_file_path = 'wholesale_products_export_1.csv'
df = pd.read_csv(csv_file_path)

# Define a similarity threshold (adjust as needed)
similarity_threshold = 90  # Example: 90% similarity

# Create a list to store merged product data
merged_products = []

# Function to merge products
def merge_products(main_product, similar_product):
    # Create a new variant (empty product title) and append it to the main product
    variant = similar_product.copy()
    variant['Title'] = ''  # Set the product title to empty

    # Set the "Option1 Value" of the variant to its original "Body (HTML)"
    variant['Option1 Value'] = similar_product['Body (HTML)']

    main_product['Variants'].append(variant)

# Iterate through the products in the DataFrame
for idx, product in df.iterrows():
    # Extract the portion of the title before the first "-" character
    title_parts = product['Title'].split('-', 1)
    title_prefix = title_parts[0].strip() if len(title_parts) > 0 else product['Title'].strip()

    # Check if the title prefix is already part of a merged product
    is_merged = False
    for merged_product in merged_products:
        similarity = fuzz.ratio(title_prefix.lower(), merged_product['Title'].lower())
        if similarity >= similarity_threshold:
            merge_products(merged_product, product)
            is_merged = True
            break

    # If not merged, create a new merged product with a list of variants
    if not is_merged:
        merged_product = product.copy()
        merged_product['Title'] = title_prefix
        merged_product['Variants'] = [product.copy()]  # Initialize variants as a list

        # Set the "Option1 Value" of the variant to its original "Body (HTML)"
        for variant in merged_product['Variants']:
            variant['Option1 Value'] = variant['Body (HTML)']

        merged_products.append(merged_product)

# Create a new DataFrame from merged_products
merged_data = []
for merged_product in merged_products:
    merged_data.extend(merged_product['Variants'])

merged_df = pd.DataFrame(merged_data)

# Save the merged DataFrame to a new CSV file
merged_csv_file_path = 'merged_shopify_products.csv'
merged_df.to_csv(merged_csv_file_path, index=False)

print(f'Merged products saved to {merged_csv_file_path}')
