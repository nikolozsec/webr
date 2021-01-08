# webr #

webr helps you retrieve HTTP status codes for list of URLs, take URL screenshots and analyze issues with websites.

### Features ###

* Return HTTP status codes (https://en.wikipedia.org/wiki/List_of_HTTP_status_codes) for the list of URLs
* Return IP address (Private/Public) for the list of URLs.
* Write output to Excel file
* Option to take website screenshots with Chrome and store in 'screenshots' directory
* Screenshots functionality is based on headless Chrome, images will be taken in the background and thus consume less resources

### NOTE:###

IP lookups will be conducted by your device, which might expose your IP address to the target URL/IP.

### Use Cases ###

* Threat hunting - identify IP addresses for domains that you can use for infrastructure testing
* Vulnerability scanning - identify live websites/domains 
* Penetration testing - identify IP addresses for domains that you can use for infrastructure testing
* Troubleshooting website issues in batch
* Creating domain lists

### Install ####

`pip install -r requirements.txt`

You need to have a Google Chrome browser installed and executable of ChromeDriver which matches your browser version.

Get Chrome Driver from: https://sites.google.com/a/chromium.org/chromedriver/downloads and put it in 'driver' folder.

Built for Python 3

### Run ###

* Put desired URLs in `domains.xlsx` under `input_urls` column.
* Run `python webr.py`
* Follow instructions
