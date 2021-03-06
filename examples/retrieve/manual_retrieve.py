# -*- coding: utf-8 -*-

""" standard """
import ConfigParser
import json
import sys

""" custom """
from threatconnect import ThreatConnect
from threatconnect.RequestObject import RequestObject

# configuration file
config_file = "tc.conf"

# retrieve configuration file
config = ConfigParser.RawConfigParser()
config.read(config_file)

try:
    api_access_id = config.get('threatconnect', 'api_access_id')
    api_secret_key = config.get('threatconnect', 'api_secret_key')
    api_default_org = config.get('threatconnect', 'api_default_org')
    api_base_url = config.get('threatconnect', 'api_base_url')
    api_result_limit = int(config.get('threatconnect', 'api_result_limit'))
except ConfigParser.NoOptionError:
    print('Could not retrieve configuration file.')
    sys.exit(1)

tc = ThreatConnect(api_access_id, api_secret_key, api_default_org, api_base_url)
tc.set_api_result_limit(api_result_limit)
tc.report_enable()

""" Toggle the Boolean to enable specific examples """
enable_example1 = False
enable_example2 = False

if enable_example1:
    #
    # build INDICATORS request object
    #
    ro = RequestObject()
    ro.set_http_method('GET')
    ro.set_owner('Example Community')
    ro.set_owner_allowed(True)
    ro.set_resource_pagination(True)
    ro.set_request_uri('/v2/indicators')

    #
    # retrieve and display the results
    #
    results = tc.api_request(ro)
    if results.headers['content-type'] == 'application/json':
        data = results.json()
        print(json.dumps(data, indent=4))

if enable_example2:
    #
    # build DOCUMENT DOWNLOAD request object
    #
    ro = RequestObject()
    ro.set_http_method('GET')
    ro.set_owner('Example Community')
    ro.set_owner_allowed(True)
    ro.set_resource_pagination(False)
    ro.set_request_uri('/v2/groups/documents/19/download')

    #
    # retrieve and display the results
    #
    results = tc.api_request(ro)
    if results.headers['content-type'] == 'application/octet-stream':
        file_contents = results.content
        print(file_contents)
