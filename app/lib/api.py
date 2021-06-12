import os
import requests
from requests.api import post

class ApiRequest(object):
    GET_SIM = '/sim'
    POST_REPORT = '/report'

    def __init__(self):
        self.api_url = os.getenv('API_URL')
        if not self.api_url: raise Exception('API_URL env not set.')

    def get_sim(self):
        return requests.get(self.api_url + ApiRequest.GET_SIM, headers={'Content-Type': 'application/json'})

    def send_report(self, report):
        return requests.post(self.api_url + ApiRequest.GET_SIM, data=report, headers={'Content-Type': 'application/json'}).status_code

def get_next_sim():
    return ApiRequest().get_sim()

def send_report(spell_name, caster_level, report):
    ApiRequest().send_report({'spellName': spell_name, 'casterLevel': caster_level, 'reportData': report})