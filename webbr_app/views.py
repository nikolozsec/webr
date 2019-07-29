import os
import platform
import socket
from datetime import datetime

import pandas as pd
import requests
import tldextract
from flask import Flask, json, render_template, request
from pandas import ExcelFile, ExcelWriter
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from . import app

app.debug = True
app.run()
app.run(debug = True)

@app.route("/")
def home():
	return render_template("home.html")

@app.route('/url-check',methods=['POST'])
def urlCheck():
	# Read input from page
	_url = request.form['inputUrl']

	# validate the received values
	if _url:
		# Get IP from domain
		try:
			ip = socket.gethostbyname(_url)

		except socket.error as error:
			ip = "error"

		print(str(ip))

	else:
		return json.dumps({'html':'<span>Enter the required fields</span>'})

	# Get IP from domain
	try:
		ip = socket.gethostbyname(_url)

	# If error, write error in excel
	except socket.error as error:
		ip = "error"	

	print(str(ip))