#!/usr/bin/env python3

import urllib.request as request
import json

# Microsoft's 0365 IP list in JSON format URL.
# Does require the clientrequestid
url = 'https://endpoints.office.com/endpoints/worldwide?clientrequestid=b10c5ed1-bad1-445f-b386-b919946339a7'

# Weekly file for Azure DevOps can be found under here:
# https://learn.microsoft.com/en-us/azure/devops/pipelines/agents/hosted?view=azure-devops&tabs=yaml

# Grab the JSON and load in to list named data.
# Each item in data - ie data[n] is of type dict.
# Each item in dictionary data[n] is type list.  So for IP addresses we can
# refer to data[n]['ips'] where 'ips' is the key name
# Microsoft use for IP addresses.
with request.urlopen(url) as response:
    if response.getcode() == 200:
        source = response.read()
        data = json.loads(source)
    else:
        print('Oh dear, could not read Microsoft JSON')


# Define a couple of empty lists for results
all_ips = []
all_ips_unique = []


# Work through each element of list 'data'.  IP addresses not present in every
# element so necessary to check key 'ips' exists.
# Within loop i['ips'] defines a list of IP addresses within a given section
# in the Microsoft JSON data.  Create list of all IP addresses,
# including duplicates, listed by Microsoft.
for i in data:
    if 'ips' in i:
        all_ips = all_ips + i['ips']

# Dedup and sort
all_ips_unique = list(set(all_ips))
all_ips_unique.sort()


# We really only need to distinguish ipv4 and ipv6 here.
for i in all_ips_unique:
    if '.' in i:
        print('ipv4:  {}'.format(i))
    elif ':' in i:
        print('ipv6:  {}'.format(i))
    else:
        print('What is this:  {}'.format(i))
