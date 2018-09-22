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
