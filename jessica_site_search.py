############jessica_site_search.py############

import os
import re
import random
import urllib.parse

def download_search_result(
	search_term,
	search_site,
	search_curl_file,
	re_search_curl_first_line,
	re_search_result_url,
	):
	###
	search_option = {
	"search_term": urllib.parse.quote(urllib.parse.unquote(search_term)),
	"search_site": urllib.parse.quote(urllib.parse.unquote(search_site))
	}
	####
	curl_file = open(search_curl_file).read()
	#####
	search_dict = re.search(re_search_curl_first_line,
		curl_file).groupdict()
	search_text = re.search(re_search_curl_first_line,
		curl_file).group()
	######
	#print(search_dict)
	#print(search_text)
	search_replaced = search_text
	######
	for k in search_dict:
		search_replaced = re.sub(
			re.escape(search_dict[k]), 
			search_option[k], 
			search_replaced)
	###
	#print(search_replaced)
	curl_file_replaced = re.sub(\
		re.escape(search_text),
		search_replaced,
		curl_file)
	###
	temp_file = "%f.html"%(random.random())
	curl_file_replaced += " -o %s"%(temp_file)
	os.system(curl_file_replaced)
	search_result_html = open(temp_file).read()
	os.system('rm %s'%(temp_file))
	return  [m.groupdict() 
	for m in 
	re.finditer(re_search_result_url, search_result_html)]

############jessica_site_search.py############
