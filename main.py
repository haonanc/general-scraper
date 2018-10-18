# Neal Haonan Chen
# University of Virginia
# hc4pa@virginia.edu
"""
A general purpose web crawler. It supports the following five methods
1.Single layer scraping: given a list of urls and do regular scrapings, saved as raw htmls.
2.Multiple layer scraping: find the desired urls from raw html text using RE, then use fetched urls to do regular
scrapings
3.Scrape with page numbers: given a list of urls with multiple pages. scrape every page using a given list of pages as suffix
4.Scrape with Yandex search: find the desired urls from yandex search engines using keyword search
5.Scrape with boilerpipe: given a list of urls and do regular scrapings with text extraction, saved as plain text
"""




import yandex_search
import util

def singleScrapeMain(urls, outputFileName, prefix = ""):
    """
    Scrape the raw htmls code from a given list of urls, save the results in a file
    :param urls: [list] list of urls you plan on scraping
    :param outputFileName: [str]output file name
    :param prefix: [str] an optional prefix for each url
    :return: void
    """
    log = []
    output = {}
    for counter,url in enumerate(urls):
        url = prefix + url
        util.consoleLog(1,url,counter + 1,len(urls))
        data, status = util.search(url, log)
        if status == 200:
            output[url] = data
    util.save_text(outputFileName, output)

def multiScrapeMain(initUrls,iterations,regexpList,outputFileName,prefixs = None, prefix_single = ""):
    """
    Use regular expression to fetch desired urls from raw htmls text, used fetched urls to scrape raw htmls
    again. Repeat for certain number of times. Then use the last set of urls to scrape and save the result in a file
    :param initUrls: [list] initial list of Urls
    :param iterations: [int] number of iterations
    :param regexpList: [list] list of regular expressions that you plan on using
    :param outputFileName: [str] output file name
    :param prefixs: [list] optional list of prefixs for iteration searching
    :param prefix_single: [str] optional prefix for the final scraping
    :return: void
    """
    if len(regexpList) != iterations or (prefixs != [] and len(prefixs) != iterations):
        print("Make sure you have a regular expression and a prefix for each iteration")
        return

    currIter = 0
    urls = initUrls
    log = []
    while currIter < iterations:
        print("Iteration: " + str(iterations))
        new_list = []
        regexp = regexpList[currIter]
        if prefixs != None:
            prefix = prefixs[currIter]
        else:
            prefix = ""
        for counter, url in enumerate(urls):
            url = prefix + url
            result, status = util.search(url,log)
            if status == 200:
                new_list += util.lookForPatterns(result,regexp)
            util.consoleLog(2,url,counter,len(urls),m2i=currIter,m2t=iterations)
        urls = new_list
        currIter -= 1
    singleScrapeMain(urls,outputFileName,prefix_single)

def pagesScrapeMain(urls,pages,outputFileName,prefix = ""):
    """
    Use to scrape websites that have multiple pages
    :param urls: [list] list of urls
    :param pages: [list] page information that will be used as a suffix during the scraping
    :param outputFileName: output file name
    :param prefix: an optional prefix
    :return: void
    """
    log = []
    output = {}
    for c_u, url in enumerate(urls):
        url = prefix + url
        for c_p, page in enumerate(pages):
            url_page = url + page
            result, status = util.search(url_page,log)
            util.consoleLog(3,url_page,c_u,len(urls),c_p,len(pages))
            if status == 200:
                output[url_page] = result
    util.save_text(outputFileName,output)

def yandexSearch(api_user,api_key,top_k_results,prefixs,suffixs,outputFileName):
    """
    a yandex search API. It requires a yandex account. The registeration is free and go to
    https://pypi.org/project/yandex-search/ for more details

    :param api_user: [str] your credentials username
    :param api_key: [str] your credentials api key
    :param top_k_results: [int] only keep top k results
    :param prefixs:[list] prefix for searches
    :param suffixs: [list] suffix for searches
    :param outputFileName: [str] output name
    :return: void
    """
    output = open(outputFileName  + ".txt", 'w')
    yandex = yandex_search.Yandex(api_user=api_user, api_key=api_key)
    for prefix in prefixs:
        for suffix in suffixs:
            output.write("=====" + prefix + suffix + "=====" + "\n")
            try:
                results = yandex.search(prefix+suffix).items
                for i in range(top_k_results):
                    output.write(str(results[i]['url']) + "\n")
            except:
                print("quest failed")

def boilerPipeScrape():
    return
    #TODO implmement the boilerpipe search function

if __name__ == "main":
    print()
