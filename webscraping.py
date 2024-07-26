import requests
from bs4 import BeautifulSoup
import json


def web_scraping():
    # URL of the webpage
    url = 'https://www.india.gov.in/my-government/whos-who/council-ministers'

    # Send an HTTP GET request to the URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all tables with the class 'views-view-grid cols-2'
        tables = soup.find_all('table', class_='views-view-grid cols-2')

        # Initialize list to hold data
        all_data = []

        # Check if any tables were found
        if tables:
            for table in tables:
                # Extract all rows from the current table
                rows = table.find_all('tr')

                for row in rows:
                    # Extract all columns (td) in the current row
                    cols = row.find_all('td')

                    # Extract data from each <td>
                    for col in cols:
                        # Extract image URL
                        image_div = col.find('div', class_='views-field views-field-field-image')
                        image_url = image_div.find('img')['src'] if image_div and image_div.find('img') else None

                        # Extract name
                        name_div = col.find('div', class_='views-field views-field-title')
                        name = name_div.get_text(strip=True) if name_div else None

                        # Extract ministries
                        ministries_div = col.find('div', class_='views-field views-field-field-ministries')
                        ministries = ministries_div.get_text(strip=True) if ministries_div else None

                        # Add data to list
                        if name and image_url and ministries:
                            all_data.append({
                                'name': name,
                                'image_url': image_url,
                                'ministries': ministries
                            })

            # Write data to a JSON file
            with open('data.json', 'w') as f:
                json.dump(all_data, f, indent=4)

            print("Data successfully written to data.json")
        else:
            print("No tables with class 'views-view-grid cols-2' found.")
    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
