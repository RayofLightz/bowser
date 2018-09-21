import json

def load_whitelist(whitelist):
    white_list_file = open(whitelist,'r')
    domains = json.load(white_list_file)
    return domains["whitelist"]

if __name__ == '__main__':
    print(load_whitelist(".test"))
