# Virustotal 

import requests
import json
#from pprint import pprint
#from pygments import highlight
#from pygments.lexers.data import JsonLexer
#from pygments.formatters.terminal import TerminalFormatter

class Virustotal():
	""" Virustotal API module """
	def __init__(self):
		self.host = "www.virustotal.com"
		self.base = "https://www.virustotal.com/vtapi/v2/"
		self.apikey = "3fc5164d7918597490c775590de3ce89bcd05d09c6a0323769314d1a65743e1c"

	def rscReport(self, rsc):
		""" Get latest report of resource """

		base = self.base + 'file/report'
		parameters = {"resource":rsc, "apikey":self.apikey}
		r = requests.post(base, data=parameters)
		#json_file = json.loads(r.text)
		#formatted_json = json.dumps(json_file, indent=4)
		#print(highlight(formatted_json, JsonLexer(), TerminalFormatter()))		
		resp = r.json()
		#formatted_json = json.dumps(json.loads(resp), indent=4)
		#colorful_json = highlight(unicode(formatted_json, 'UTF-8'), lexers.JsonLexer(), formatters.TerminalFormatter())
		#print(colorful_json)
		results = parse_resp(resp)
		return results

	def urlReport(self, rsc, scan=0):
		""" Get latest report URL scan report of resource """

		base = self.base + 'url/report'
		parameters = {"resource":rsc, "scan":scan, "apikey":self.apikey}
		r = requests.post(base, data=parameters)
		resp = r.json()
		results = parse_resp(resp)
		return results

	def scanURL(self, rsc):

		""" Send RSC/URL for scanning; Its encouraged to check for last scanusing urlReport()
		To submit batch rsc should be example.com\nexample2.com"""

		base = self.base + 'url/scan'
		parameters = {"url":rsc, "apikey":self.apikey}
		r = requests.post(base, data=parameters)
		resp = r.json()
		results = parse_resp(resp)
		return results

	def rscSubmit(self, rsc):

		""" Submit potential malicious file to virustotal for analyzing """
		base = self.base + 'file/scan'
		f = open(rsc, 'rb')
		parameters = {"apikey":self.apikey}
		r = requests.post(base, data=parameters, files={'file':f})
		resp = r.json()
		results = parse_resp(resp)
		return results


def parse_resp(resp):
	""" Parses the response from the requests.gets/posts()
	then returns the data back to the function """
	buf = {}
	for item in resp:
		buf[item] = resp[item]

	return buf


