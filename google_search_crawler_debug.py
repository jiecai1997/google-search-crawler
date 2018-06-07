# Google Search Package: https://breakingcode.wordpress.com/2010/06/29/google-search-python/
# Scrapely Package: https://github.com/scrapy/scrapely
# https://www.analyticsvidhya.com/blog/2015/10/beginner-guide-web-scraping-beautiful-soup-python/
# https://stackoverflow.com/questions/3898574/google-search-using-python-script

#import packages
import urllib2
from googlesearch.googlesearch import GoogleSearch
from bs4 import BeautifulSoup, UnicodeDammit
import csv
import time
import re

#search query
#query = 'Global Dental Model Industry'

# initialize dictionary to store search results
# rows: Name, *user defined columns*, URL
collected_items = []
countries = [
'China',
'United States',
'U.S.',
'Japan',
'Germany',
'Korea',
'India',
'Italy',
'United Kingdom',
'U.K.',
'France',
'Mexico',
'Brazil',
'Indonesia',
'Russia',
'Canada',
'Spain',
'Turkey',
'Switzerland',
'Thailand',
'Ireland',
'Australia',
'Argentina',
'Poland',
'Netherlands']
regions = [
'North America',
'Asia',
'EU',
'Europe'
]
i = 0

# ask user for query
query = raw_input("Search Query: ")

# ask user how many websites to scrape
try:
    n = int(raw_input("# of Websites to Scrape: "))
except ValueError:
    print "Enter Valid # of Websites"
    sys.exit()
if n <1:
    print "Needs to be positive"

UNIXtime = int(time.time())
filename = query.replace(" ","_").lower()+"_"+str(n)+"_"+str(UNIXtime)


for j, result in enumerate(GoogleSearch().search(query,n).results):
    j+=1
    url = result.url.encode("utf-8").strip()
    req = urllib2.Request(url)
    try:
        response = urllib2.urlopen(req)
    except urllib2.HTTPError as e:
        print "Scraping URL # " + str(j) + "--" + str(e.code) +" Request Error"
        #print 'The server couldn\'t fulfill the request.'
        #print 'Error code: ', e.code
        pass
    except urllib2.URLError as e:
        print "Scraping URL # " + str(j) + "--Server Error"
        #print 'We failed to reach a server.'
        #print 'Reason: ', e.reason
        pass
    else:
        item = {}
        soup = BeautifulSoup(response, "html.parser")
        if soup.title == None or soup.title.string == None:
            print "boy bye"
        else:
            title = soup.title.string.encode("utf-8").strip()
            text = soup.get_text().encode("utf-8").strip().lower()
            item["Name"] = title
            item["URL"] = url
            for country in countries:
                #print "# of",country,len(soup.find_all(string=country))
                item[country] = len(re.findall(country.lower()+'\D*', text.strip().lower()))
            for region in regions:
                #print "# of",region,len(soup.find_all(string=region))
                item[region] = len(re.findall(region.lower()+'\D*', text.strip().lower()))
            collected_items.append(item)
            print "Scraping URL # " +  str(j) + "--Success"
            print url
            print title
            i+=1
    print

print ("Finished Scraping!")
print ("Scrape Success Rate " + str(round(float(i)/j*100,2)) + "%")


print ("Writing Results to "+filename+".csv")

# write outcome to
field_names = [
"Name",
'China',
'United States',
'U.S.',
'Japan',
'Germany',
'Korea',
'India',
'Italy',
'United Kingdom',
'U.K.',
'France',
'Mexico',
'Brazil',
'Indonesia',
'Russia',
'Canada',
'Spain',
'Turkey',
'Switzerland',
'Thailand',
'Ireland',
'Australia',
'Argentina',
'Poland',
'Netherlands',
'North America',
'Asia',
'EU',
'Europe',
"URL"]

with open(filename+".csv", "w") as f:
    writer = csv.DictWriter(f, field_names)

    # Write a header row
    writer.writerow({x: x for x in field_names})

    # write items
    for row in collected_items:
        writer.writerow(row)
f.close()

print("Done!")


'''
_________________________
Interesting but Not Using
_________________________

# google API key
key = "AIzaSyCBIy_NbwGWUWxBpVO5uhLFziDVVl-pWy4"

# Scraper... Google Search with ML Queries
from scrapely import Scraper
s = Scraper()

url1 = 'https://www.ibisworld.com/industry-trends/market-research-reports/healthcare-social-assistance/ambulatory-health-care-services/dentists.html'
data = {
'name': 'Dentists - US Market Research Report',
'author': 'IBISWorld',
'url': 'https://www.ibisworld.com/industry-trends/market-research-reports/healthcare-social-assistance/ambulatory-health-care-services/dentists.html'
}
s.train(url1, data)
'''
