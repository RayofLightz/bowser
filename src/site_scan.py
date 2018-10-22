import requests as r
import re
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import checksum
import csv_tool
class Site_Scanner(object):
    def __init__(self,url,whitelist):
        self.url = url
        self.main_html = r.get(self.url)
        self.url_parsed = urlparse(self.url)
        self.whitelist = whitelist
        self.csv_recorder = csv_tool.Csv_tool("Output.csv")

    def get_autocorrected(self,url):
        ref_link = self.url
        a = urlparse(url)
        if a.scheme == '':
            url = "https:" + url
        if a.netloc == '':
            return None
             
        return r.get(url,headers={'referer':ref_link})

    def scan_html(self):
        soup = BeautifulSoup(self.main_html.text,'html.parser')
        regex = re.compile(r'^.*\.(?=[^.]+\.[^.]+$)')
        for link in soup.find_all('script'):
            b = urlparse(link.get('src'))
            if b.netloc in self.whitelist:
                #checks the domain against the whitelist
                continue
            if self.url_parsed.netloc == re.sub(regex,'',str(b.netloc)):
                #removes subdomain and the checks the domain against that of the original host
                continue
            if b.netloc == b'':
                continue
            else:
                yield link.get('src')


    def scan_js(self,link_list):
        ref_link = self.url
        # the following regexs find urls and remove text inside of multi and single line comments
        comment_remove = re.compile(r"(/\*([^*]|[\r\n]|(\*+([^*/]|[\r\n])))*\*+/)|[^:|^](//.*)")
        regex = re.compile(r'(http|ftp|https)://([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?')
        for link in link_list:
            b = self.get_autocorrected(link)
            if b == None:
                continue
            c = re.sub(comment_remove,"",b.text) 
            a = list(re.finditer(regex,c))
            for match in a:
                yield match.group(0)
    def check_sum_js(self,link):
        a = self.get_autocorrected(link)
        hash_value = checksum.check_sum(a.text)
        return hash_value

    def check_sum_js_list(self,link_list):
        for link in link_list:
            hashed_file = self.check_sum_js(link)
            yield_value = [link, hashed_file]
            self.csv_recorder.record_csv(yield_value)

    def check_is_js(self,url):
        b = urlparse(url)
        if re.search(r'\.js',b.path) != None:
            return True
        else:
            # A simple regex to test if something is javascript
            try:
                c = self.get_autocorrected(url)
                regex = r"[(\(\))({};)]"
                if re.findall(regex,c.text) != []:
                    return True
            except r.exceptions.ConnectionError:
                pass
        return False

    def check_is_js_list(self,link_list):
        for link in link_list:
            if self.check_is_js(link) == True:
                yield link

    def site_check(self):
        print("Starting scan")
        a = list(self.scan_html())
        b = list(self.scan_js(a))
        c = list(self.check_is_js_list(b))
        print("Generating checksums")
        self.check_sum_js_list(a)
        self.check_sum_js_list(c)

if __name__ == '__main__':
    import pprint
    # this domain has no thirdparty js
    test_scanner = Site_Scanner("https://blockads.fivefilters.org/?pihole",[])
    pp = pprint.PrettyPrinter(indent=4)
    b = test_scanner.site_check()
    pp.pprint(b)
