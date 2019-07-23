# webbr #

webbr is a simple tool that helps you retrieve http status codes for list of websites, take website screenshots with Chrome

### How to ###
#### Install ####

`pip install -r requirements.txt`

#### Run ####
`python webbr.py`

Source and destination files should be in following format `[title].xlsx`

Table header must be `input_urls`. Example:

| input_urls      | X           | Z  |
| ------------- |:-------------:| -----:|
| http://example.com    | -| - |
| https://example2.com   |  -   |  -  |

URLs must start with `http://` or `https://`

### Features ###

* Select Excel file with the list of URLs
* Return HTTP status codes (https://en.wikipedia.org/wiki/List_of_HTTP_status_codes)
* Return IP address
* Write output to specified Excel file
* Take website screenshots with Chrome and store in 'screenshots' directory: [1] For all websites [2] Only for errors [3] None
* Screenshots fuinctionality is based on headless Chrome, images will be taken in the background and thus consume less resources

### Useful for ###

* Vulnerability scanning - identify websites/domains that are available from a list
* Penetration testing - identify IP addresses for domains that you can use for infrastructure testing
* Troubleshooting website issues in batch
* Creating domain lists

### Comments ###

webbr is under development. Any feedback is more than welcome!