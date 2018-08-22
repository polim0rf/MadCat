import hashlib
 
def get_file_content(filename):
	with open(filename, 'rb') as fd:
		return fd.read()

def get_file_hash(file_content):
	hash_func = 'sha256'

	hash_func = getattr(hashlib, hash_func)

	checksum = hash_func(file_content).hexdigest()

	return checksum 
