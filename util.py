# Neal Haonan Chen
# University of Virginia
# hc4pa@virginia.edu

import re
import requests
def search(url,log):
    """
    a single search function
    :param url: [str] url to search
    :param log: [list] a list to save the error logs
    :return: [str, int] raw html text, html return code
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115         Safari/537.36'}
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.text, response.status_code
    except requests.exceptions.Timeout as errto:
        log.append(url)
        print(errto)
    except requests.exceptions.TooManyRedirects as errt:
        log.append(url)
        print(errt)
    except requests.exceptions.HTTPError as err:
        print(err)
    except requests.exceptions.RequestException as errr:
        print(errr)
    return "", "404"

def save_text(outputFile, savedDict):
    for key, values in savedDict.items():
        file = open(outputFile+"_"+key.split("/")[-1]+".txt","w")
        file.write(values)

def list_eliminate_duplicate(input_list):
    """
    a simple function to remove duplicate from the list
    :param input_list: [list] input list
    :return: [list] a list without duplicates
    """
    news_ids = []
    for id in input_list:
        if id not in news_ids:
            news_ids.append(id)
    return  news_ids

def consoleLog(mode, url, count, total, m3c = 0, m3p = 0, m2i = 0, m2t = 0):
    if mode == 1:
        print("Fetching:" + url + " Completed:" + str(count) + "/" + str(total))
    if mode == 3:
        print("Fetching:" + url + " Completed Urls:" + str(count) + "/" + str(total) + " Completed Pages:" + str(m3c) + "/" + str(m3p))
    if mode == 2:
        print("Fetching:" + url + " Completed Urls:" + str(count) + "/" + str(total) + " Completed Pages:" + str(m2i) + "/" + str(m2t))


def lookForPatterns(string,regexp):
    """
    use regular expression to search strings
    :param string: [str] input string to search
    :param regexp: [str] regular expression
    :return: list: [list] list of results
    """
    zhPattern = re.compile(regexp)
    matches_c = re.findall(zhPattern, str(string))
    ret = []
    print(str(len(matches_c))+" matches found")
    for item in matches_c:
        ret.append(item)
    return ret