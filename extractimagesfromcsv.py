import csv
from PIL import Image
import requests
import os

# Define the CSV file path and the column containing image URLs
csv_file_path = 'products_export_1.csv'
image_column_name = 'Image Src'

# Define the output directory where the images will be saved
output_directory = 'output_images/'

# Create the output directory if it doesn't exist
os.makedirs(output_directory, exist_ok=True)

# Function to download and save images from URLs
def download_images_from_csv(csv_path, image_column, output_dir):
    with open(csv_path, 'r', newline='') as csvfile:
        csvreader = csv.DictReader(csvfile)
        for row in csvreader:
            try:
                # Get the image URL from the CSV cell
                image_url = row[image_column]
                
                # Generate a unique filename for each image (you can use a unique identifier from the CSV)
                image_filename = f"{row['Title']}.jpg"  #
                
                # Download the image from the URL
                response = requests.get(image_url)
                
                if response.status_code == 200:
                    # Save the image to the output directory
                    with open(os.path.join(output_dir, image_filename), 'wb') as image_file:
                        image_file.write(response.content)
                    print(f"Saved {image_filename}")
                else:
                    print(f"Failed to download {image_url}")
            except Exception as e:
                print(f"Error processing row: {str(e)}")

download_images_from_csv(csv_file_path, image_column_name, output_directory)
