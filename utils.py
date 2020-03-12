from enum import Enum
from urllib2 import urlopen
from json import loads, dumps

class Results(Enum):
    SAFE = 0
    MALWARE = 1
    MALICIOUS = 2

def extract_url(link):
    return '/'.join(link.split('/')[:3])   

def getDomainInfo(domain):
    req_url = 'https://www.whoisxmlapi.com/whoisserver/WhoisService?apiKey=at_t4xZWgxz4TeHPanzqBRRZVgcnSmmw&domainName=' + domain + '&outputFormat=JSON'
    unicode_data = urlopen(req_url).read().decode('utf8')
    data_dict = loads(unicode_data)
    print('---------------DOMAIN DETAILS---------------')
    print(dumps(data_dict, indent = 4, sort_keys=True))
    print('---------------DOMAIN DETAILS ENDED---------------')

    return data_dict
