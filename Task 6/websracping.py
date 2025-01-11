import requests
from bs4 import BeautifulSoup
import csv

# URL of the e-commerce page (example: Amazon search results page for a product)
url = 'https://www.amazon.in/s?k=laptops'  # Replace with the actual URL of the website you want to scrape

# Send an HTTP request to the URL
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
response = requests.get(url, headers=headers)

# Parse the HTML content of the page
soup = BeautifulSoup(response.content, 'html.parser')

# Extract product names, prices, and ratings
products = soup.find_all('div', {'class': 's-main-slot s-result-list s-search-results sg-row'})  # Amazon product container class

product_data = []

for product in products:
    try:
        # Extract product name
        name = product.find('span', {'class': 'a-text-normal'}).text
        
        # Extract product price
        price = product.find('span', {'class': 'a-price-whole'})
        if price:
            price = price.text
        else:
            price = "Not Available"
        
        # Extract product rating
        rating = product.find('span', {'class': 'a-icon-alt'})
        if rating:
            rating = rating.text
        else:
            rating = "No Rating"
        
        # Append the extracted data to the list
        product_data.append([name, price, rating])
    except AttributeError:
        continue

# Save the data to a CSV file
filename = 'products.csv'
with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['Product Name', 'Price', 'Rating'])
    csv_writer.writerows(product_data)

print(f"Data has been written to {filename}")
