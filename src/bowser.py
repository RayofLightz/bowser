import argparse
import site_scan
import config
import os
import time
#setup cmd args
parser = argparse.ArgumentParser(description="A tool to identify and track md5 sums of third party javascript on a website")
parser.add_argument('url', metavar='url', type=str,help="the url of the site to scan")
args = parser.parse_args()


#setup the whitelist
print("Starting Bowser")
whitelist = config.load_whitelist(os.environ["HOME"]+ "/.bowser_whitelist")
scanner = site_scan.Site_Scanner(args.url,whitelist)
start = time.time()
scanner.site_check()
end = time.time()
print("Took " + str(((end-start)*100)) + " Seconds to scan") 
