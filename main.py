import requests
from bs4 import BeautifulSoup
from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

def scrape_data(search_query):
    product_names = []
    product_prices = []
    product_descriptions = []

    url = f"https://www.flipkart.com/search?q={search_query}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=1"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    # Find all the product names on the page
    names = soup.find_all("div", class_="_4rR01T")
    prices = soup.find_all("div", class_="_30jeq3 _1_WHN1")
    descriptions = soup.find_all("div", class_="fMghEO")

    # Extract and append the text of each product name, price, and description to respective lists
    for name, price, desc in zip(names, prices, descriptions):
        product_names.append(name.text)
        product_prices.append(price.text)
        product_descriptions.append(desc.text)

    # Return the scraped data as a dictionary
    scraped_data = {
        'product_names': product_names,
        'product_prices': product_prices,
        'product_descriptions': product_descriptions
    }

    return scraped_data

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the search query from the form
        search_query = request.form['search_query']

        # Call the scrape_data function to get data
        scraped_data = scrape_data(search_query)

        # Return the scraped data as JSON
        return jsonify(scraped_data)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

