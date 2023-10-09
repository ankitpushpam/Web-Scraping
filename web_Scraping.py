import urllib.request
import urllib.parse
import urllib.error
import ssl
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as BS
import pandas as pd

# Function to scrape the total number of listings
def scrape_total_listings(url):
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()

    soup = BS(webpage, 'html.parser')
    print(soup.title)

    add = soup.findAll('small', attrs={'class': 'font-weight-bold'})

    total = int(add[0].get_text().split()[-2])
    print(total)

    return total

# Function to scrape the links to individual listings
def scrape_listing_links(base_url, total):
    links = []
    found = 0
    i = 1

    while found < total:
        url = base_url + str(i)
        req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urlopen(req).read()
        soup = BS(webpage, 'html.parser')
        listings = soup.find_all('h5', attrs={'class': 'card-title font-weight-bold listing-address mb-25'})

        for list in listings:
            links.append(list.a['href'])
        found += len(listings)
        i += 1

    return links

# Function to scrape individual listing details
def scrape_listing_details(links):
    Address = []
    Sold_Price = []
    Sold_Date = []
    House_Type = []
    Bathroom = []
    Kitchen = []
    Family_Room = []
    Fire_Place = []
    Flooring = []
    Laundry = []
    Pool = []
    Style = []
    Garage_Parking = []
    Beds = []
    Bath = []
    Sqft = []
    Sqft_Lot = []
    Year_Built = []

    for link in links:
        url = 'https://www.mlslistings.com' + link
        print(url)
        req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urlopen(req).read()
        soup = BS(webpage, 'html.parser')

        # Extract relevant information using BeautifulSoup

        # Append extracted information to respective lists

    data = pd.DataFrame({'Address': Address, 'Sold_Price': Sold_Price, 'Sold_Date': Sold_Date, 'House_Type': House_Type,
                         'Bathroom': Bathroom, 'Kitchen': Kitchen, 'Family_Room': Family_Room,
                         'Fire_Place': Fire_Place, 'Flooring': Flooring, 'Laundry': Laundry, 'Pool': Pool,
                         'Style': Style, 'Beds': Beds, 'Bath': Bath, 'Sqft': Sqft, 'Sqft_Lot': Sqft_Lot,
                         'Year_Built': Year_Built})

    return data

# Function to save data to an Excel file
def save_to_excel(data, excel_filename):
    writer = pd.ExcelWriter(excel_filename)
    data.to_excel(writer, 'data')
    writer.save()

# Main function to execute the scraping process
def main():
    base_url = "https://www.mlslistings.com/Search/Result/9fbbd96d-0150-4653-b8f2-8844f745ab31/"
    total_listings_url = base_url + "1"
    listing_data = None
    total = scrape_total_listings(total_listings_url)
    listing_links = scrape_listing_links(base_url, total)
    listing_data = scrape_listing_details(listing_links)

    excel_filename = 'Hayward_CA.xlsx'
    save_to_excel(listing_data, excel_filename)
    return listing_data if listing_data is not None else []

if __name__ == "__main__":
    listing_data = main()

