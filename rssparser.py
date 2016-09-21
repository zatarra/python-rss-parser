import requests
import re

class RSSParser(object):
  
  items_regex         = re.compile('<item.*?>(.*?)<\/item>', re.S)
  details_title_regex = re.compile('<title.*?>(.*?)<\/title>', re.S)
  details_link_regex  = re.compile('<link.*?>(.*?)<\/link>', re.S)
  details_date_regex  = re.compile('<pubDate>(.*?)<\/pubDate>', re.S)
 
  def parse(self, url):
    ''' Very basic RSS parser. Reads an RSS feed and extracts all the items ( Title, Link, pubDate ) '''
    items = []
    response = requests.get(url).text
    tmpItems = self.items_regex.findall(response)
    for i in tmpItems:
      items.append({"title": self.details_title_regex.search(i).group(1), "link": self.details_link_regex.search(i).group(1), "date": self.details_date_regex.search(i).group(1)})
    return items

if __name__ == "__main__":
  import sys, json
  try:
    if len(sys.argv) > 1:
      print json.dumps(RSSParser().parse(sys.argv[1]))
  except Exception as e:
    print "Error parsing the feed you provided: %s" % e.message
    sys.exit(1)
