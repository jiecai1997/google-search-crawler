# Google Search Package: https://breakingcode.wordpress.com/2010/06/29/google-search-python/
# Scrapely Package: https://github.com/scrapy/scrapely
# https://www.analyticsvidhya.com/blog/2015/10/beginner-guide-web-scraping-beautiful-soup-python/
# https://stackoverflow.com/questions/3898574/google-search-using-python-script

#imports
import urllib2
from bs4 import BeautifulSoup
from googlesearch.googlesearch import GoogleSearch
import csv
from scrapely import Scraper
from bs4 import UnicodeDammit
from collections import Counter
import re
import time
s = Scraper()


query = raw_input("Search Query: ")
try:
    n = int(raw_input("# of Websites to Scrape: "))
except ValueError:
    print "Enter Valid # of Websites"
    sys.exit()
'''
UNIXtime = int(time.time())
filename = query.replace(" ","_").lower()+"_"+str(n)+"_"+str(UNIXtime)
print filename
'''
# initialize dictionary to store search results
# rows: Name, Author, Description, Url
collected_items = []
countries = [
'China',
'United States',
'Japan',
'Germany',
'Korea',
'India',
'Italy',
'United Kingdom',
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
'Europe'
]

for j, result in enumerate(GoogleSearch().search(query,n).results):
    j+=1
    #print "URL #"+str(j)
    title = result.title
    url = result.url
    #print result.title
    #print result.url

    #url = "http://www.dentistrytoday.com/news/industrynews/item/2372-chinese-dental-industry-primed-for-growth"
    req = urllib2.Request(url)
    try:
        response = urllib2.urlopen(req)
    except urllib2.HTTPError as e:
        print "Scraping URL # " + str(j) + " --" + str(e.code) + " Request Error"
        #print 'The server couldn\'t fulfill the request.'
        #print 'Error code: ', e.code
        pass
    except urllib2.URLError as e:
        print "Scraping URL # " + str(j) + " --Server Error"
        #print 'We failed to reach a server.'
        #print 'Reason: ', e.reason
        pass
    else:
        soup = BeautifulSoup(response, "html.parser")
        '''
        if soup.title == None or soup.title.string == None:
            print "Scraping URL # " + str(j) + " --Encode Error"
            pass
        '''
        item = {}
        #collected_items.append({"URL":url, "name": title})
        item["Name"] = title
        item["URL"] = url
        print "Scraping URL # " + str(j) + " --Success"
        text = soup.get_text().strip().lower()
        #text = "ChiNA china"
        #print text
        print len(re.findall('banana\D*', text.strip().lower()))

        '''
        for country in countries:
            print "# of",country, response.read.count(country)
            #print "# of",country,len(soup.find_all(te=lambda text: text and country in text))
            #item[country] = len(soup.find_all(string=country))
        for region in regions:
            print "# of",country, response.read.count(region)
            #print "# of",region,len(soup.find_all(string=region))
            #item[region] = len(soup.find_all(string=region))
        collected_items.append(item)
        '''


# write outcome to
field_names = [
"Name",
'China',
'United States',
'Japan',
'Germany',
'Korea',
'India',
'Italy',
'United Kingdom',
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
'Europe',
"URL"]

'''
with open(filename+".csv", "w") as f:
    writer = csv.DictWriter(f, field_names)

    # Write a header row
    writer.writerow({x: x for x in field_names})

    # write items
    #for row in collected_items:
        #writer.writerow(row)
f.close()
'''

print ("Finished Scraping!")
#print ("Scrape Success Rate " + str(round(float(i)/j*100,2)) + "%")
