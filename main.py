import os
import data_visualization
import extract_data_from_pdf
import webscraping
from flask_app import app

if __name__ == '__main__':
    if not os.path.exists('images'):
        os.makedirs('images')
    webscraping.web_scraping()
    extract_data_from_pdf.get_data()
    data_visualization.visualize()
    app.run(host="0.0.0.0", port=5002)




