
__author__ = "Polim0rf"
__version__ = '0.0.1'
__released__ = "22/08/2018"

from virustotal import Virustotal
import webbrowser
import sys
import os
import hasher

#Cert for the .exe file to work with requests
os.environ["REQUESTS_CA_BUNDLE"] = "C:\Python27\Lib\site-packages\certifi\cacert.pem"

#Initializes variables
hash_func = None
file_name = None
    
#Get and print a list of files dropped into MadCat
file_path = sys.argv[1:]
for p in file_path:
	path = p
	print("\nFile to be processed:" + "\n" + p)

file_content = hasher.get_file_content(path)
print("\nFile content:"  + "\n" + file_content)
checksum = hasher.get_file_hash(file_content)
print("\nFile hash SHA256:" + "\n" + checksum)

virustotal = Virustotal()
get_report = virustotal.rscReport(checksum)
#print(get_report)

vt_link = get_report['permalink']
print("\nOpening Virustotal report: " + "\n" + vt_link)
webbrowser.open_new_tab(vt_link)

#print result['permalink']
#print result['headers']['Host']

print("")
input('Press ENTER to exit...')


