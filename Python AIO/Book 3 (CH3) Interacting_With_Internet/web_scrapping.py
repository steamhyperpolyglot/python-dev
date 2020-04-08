# Get request module from url library
from urllib import request
# In order to dump data to json file.
import json
# To import data to a CSV file
import csv
# This one has handy tools for scraping a web page.
from bs4 import BeautifulSoup

# Sample page for practice.
page_url = 'https://alansimpson.me/python/scrape_sample.html'

# Open that page.
rawpage = request.urlopen ( page_url )

# Make a BeautifulSoup object from the html [page]
soup = BeautifulSoup ( rawpage, 'html5lib' )

# Isolate the main content block.
content = soup.article

# Create an empty list for dictionary items.
links_list = [ ]

# Loop through all the links in the article.
for link in content.find_all ( 'a' ):
	# Try to get the href, image url, and text.
	try:
		url = link.get ( 'href' )
		img = link.img.get ( 'src' )
		text = link.span.text
		links_list.append ( { 'url': url, 'img': img, 'text': text } )
		
		# Save as a JSON FILE.
		# with open('links.json', 'w', encoding='utf-8') as links_file:
		# 	json.dump(links_list, links_file, ensure_ascii=False)
			
		# Save it to a CSV.
		with open('links.csv', 'w', newline='') as csv_out:
			csv_writer = csv.writer(csv_out)
			# Create the header row
			csv_writer.writerow(['url', 'img', 'text'])
			for row in links_list:
				csv_writer.writerow([str(row['url']), str(row['img']), str(row['text'])])
	# If the row is missing anything...
	except AttributeError:
		# ... skip it, don't blow up
		pass
