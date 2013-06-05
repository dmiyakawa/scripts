#!/usr/bin/python
'''
An example showing the server version.

Created on 2013-06-05

@author: dmiyakawa
'''
from zabbix_api import ZabbixAPI
import config

zapi = ZabbixAPI(server=config.server,
                 path='',
                 log_level=0)
zapi.login(config.username, config.password)

print zapi.apiinfo.version({})
