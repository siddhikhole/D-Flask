from flask import Flask,render_template,request
import requests 
from bs4 import BeautifulSoup

app=Flask(__name__)

@app.route('/')
def index():
	return render_template('url.html')

@app.route('/url',methods=['POST','GET'])
def  url():
	if request.method=='POST':
		url=request.form['url']

		page = requests.get(url)
		data=page.text
		soup = BeautifulSoup(data)		
		name = soup.find()
		name_list=[]
		for name in name.find_all('a'):
			links = name.get('href')
			name_list.append(links)
		return render_template('ptrint.html',links=name_list) 		
	

if __name__ == '__main__':
	app.run()
