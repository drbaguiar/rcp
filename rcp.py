from bs4 import BeautifulSoup
import urllib2
import sys
import csv

if len(sys.argv) != 2:
    sys.exit('No URL provided.')

url = sys.argv[1]

response = urllib2.urlopen(url)

soup = BeautifulSoup(response, 'html.parser')

full_poll = soup.find("div", {"id": 'polling-data-full'})
rows = full_poll.find('table', {"class": 'data'})

data = []

for row in rows:
    cols = row.find_all('th')
    cols = [ele.text.strip() for ele in cols]
    data.append([ele for ele in cols if ele])

for row in rows:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    data.append([ele for ele in cols if ele])

data = filter(None, data)

with open("output.csv", "wb") as f:
    writer = csv.writer(f)
    writer.writerows(data)