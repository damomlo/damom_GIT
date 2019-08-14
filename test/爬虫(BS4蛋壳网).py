import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
from urllib import request
import time

from bs4 import BeautifulSoup
import requests
import re
import random
data=[]
data_error=[]
def get_html(i):
	a = random.randint(0,10)
	print(a)
	time.sleep(a)
	print('正在爬取第%i页数据'%(i))
	url = 'https://www.dankegongyu.com/room/cd?search_text=&page='+str(i)
	response = requests.get(url)
	soup = BeautifulSoup(response.text,'lxml')
	data_1 = soup.find_all('div',class_='r_lbx_cena')
	data_2 = soup.find_all('div',class_='r_lbx_cenb')
	data_3 = soup.find_all('div',class_='r_lbx_moneya')

	result_a = []
	result_c = []
	for data in data_1:
		element_1 = re.findall('\S+',data.get_text())
		result_a.append(element_1)
	for i in range(0,len(result_a)):
		if i%2 == 0:
			result_c.append(result_a[i])

	result_b = []
	for x,y in zip(data_2,data_3):
		element_2=re.findall('\S+',x.get_text().replace('|',''))+re.findall('\d+',y.get_text())
		result_b.append(element_2)

	result=[]
	for x,y in zip(result_c,result_b):
		for z in y:
			x.append(z)
		result.append(x)
	return result

def wirte_to_file():
	for i in range(0,60):
		result=get_html(i)
		for j in result:
			data.append(j)
	df=pd.DataFrame(data)
	df.to_csv('1111.csv',mode='a',index=False)

wirte_to_file()