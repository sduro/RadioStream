import htmllib, formatter
import urllib, htmllib, formatter

class LinksExtractor(htmllib.HTMLParser):
    def __init__(self, formatter):
        htmllib.HTMLParser.__init__(self, formatter)
        self.links = []

    def start_a(self, attrs):
        if len(attrs) > 0 :
            for attr in attrs :
                if attr[0] == "href":
                    self.links.append(attr[1])

    def get_links(self):
        return self.links

def main():
    format = formatter.NullFormatter()
    htmlparser = LinksExtractor(format)
    data = urllib.urlopen("http://www.listenlive.eu/spain.html")
    htmlparser.feed(data.read())
    htmlparser.close()
    links = htmlparser.get_links()
    for urls in links:
        print urls
    
if __name__=='__main__':
    main()