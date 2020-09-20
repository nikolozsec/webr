# webR #

webR is a simple tool that helps you retrieve http status codes for list of websites, take website screenshots with Chrome Driver.

You need to have a Google Chrome browser installed and executable of ChromeDriver which matches yourr browser version.

Get Chrome Driver from: https://sites.google.com/a/chromium.org/chromedriver/downloads

### Install ####

`pip install -r requirements.txt`

### Features ###

* Select Excel file with the list of URLs
* Return HTTP status codes (https://en.wikipedia.org/wiki/List_of_HTTP_status_codes)
* Return IP address
* Write output to Excel file
* Option to take website screenshots with Chrome and store in 'screenshots' directory
* Screenshots functionality is based on headless Chrome, images will be taken in the background and thus consume less resources

### Useful for ###

* Vulnerability scanning - identify websites/domains that are available from a list
* Penetration testing - identify IP addresses for domains that you can use for infrastructure testing
* Troubleshooting website issues in batch
* Creating domain lists

### Run ###

Put desired URLs in domains.xlsx under input_urls column.

`python webr.py`

### Comments ###

webR is under development. Any feedback is more than welcome!
