# general-scraper
a general web scraper that will make my furture research work easier.
It supports the following five methods
1.Single layer scraping: given a list of urls and do regular scrapings, saved as raw htmls.

2.Multiple layer scraping: find the desired urls from raw html text using RE, then use fetched urls to do regular
scrapings, saved as raw htmls.
3.Scrape with page numbers: given a list of urls with multiple pages. scrape every page using a given list of pages as suffix
4.Scrape with Yandex search: find the desired urls from yandex search engines using keyword search. 
-Rquires Yandex account; package dependencies: six, xml
5.Scrape with boilerpipe: given a list of urls and do regular scrapings with text extraction, saved as plain text
