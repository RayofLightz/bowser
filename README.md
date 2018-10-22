# Bowser
## A tool to generate md5 sums of all third party javascript on your site
Bowser is a python script that dynamically maps all the third party javascript on your website and then creates md5 check sums of each source with javascript. It then outputs this information into a csv file
## Setup
The setup.sh script will install all the python packages and create the whitelist file.
```
$ ./setup.sh
```
## Usage
```
(~/Bowser_dir/src)$ python3 bowser.py <target site>
```
## Whitelisting top level domains
To whitelist a domain that is directly included in the html you are searching open the json file located in ~/.bowser_whitelist
From there you can add to the whitelist array property.
## Pypy support
Bowser can be run with pypy3 to increase the speed of bowser. This can leverage 
a decent bump in speed (I got bowser to run twice as fast as the traditional Cpython runtime). However getting pypy to work requires some extra work.
First you have to install [pypy3.5](https://pypy.org/download.html).
Then using pypy run the pip-get script. Then once pip is working to install
packages run `pypy -m pip install requests beautifulsoup4` 
