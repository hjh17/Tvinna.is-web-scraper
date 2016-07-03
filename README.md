# Tvinna.is notifier


A Python web scraping tool that checks for new job positions at [Tvinna.is](www.tvinna.is) every five minutes and notifies you via email.

## requirements

 1. Gmail account.
 2. Receiving email address, can be the same as the Gmail address.


## usage
1. Install dependencies.
2. Change the values on `gmail_from_address`, `gmail_password` and `receiving_email` in `scraper.py`
3. Turn on [Less secure apps](https://www.google.com/settings/security/lesssecureapps) from google settings.
4. Run `python scraper.py` and keep it running.
