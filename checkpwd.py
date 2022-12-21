import requests #manually requests like browser
import hashlib
import sys

def request_api_data(query_char):
	url='https://api.pwnedpasswords.com/range/'+query_char
	res=requests.get(url, verify=False)
	if res.status_code != 200:
		raise RuntimeError(f'Error fetching: {res.stastus_code}, check the api and try again')
	return res

def get_pwd_leak_count(hashes,hash_checked):
	hashes= (line.split(':') for line in hashes.text.splitlines())
	for h,count in hashes:
		if h== hash_checked:
			return count
	return 0		#return: exits the loop

def pwned_api_check(password):	#hash function
	sha1password= hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
	f5_char, tail= sha1password[:5], sha1password[5:]
	response= request_api_data(f5_char)
	return get_pwd_leak_count(response,tail)

def main(args):
	for password in args:
		count= pwned_api_check(password)
		if count:
			print(f'{password} was found {count} times. Time to change it')
		else:
			print("you're good to go")
	return 'done!'

if __name__=='__main__':
	sys.exit(main(sys.argv[1:]))