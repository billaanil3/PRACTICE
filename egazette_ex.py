import urllib2
from selenium import webdriver
from selenium.common import exceptions
from time import sleep
from bs4 import BeautifulSoup

# from scrapper_exceptions import PageNotFoundError
# from link_object import LinkObject

def run(url, ministry):
    try:
        browser = webdriver.Chrome()
        # url == "http://apegazette.cgg.gov.in/":
        browser.get(url)
        username_box = browser.find_element_by_id('extraordinary').click()
        xpath = '//*[@id="extraordinary"]'
        browser.find_element_by_xpath(xpath).click()
        print "Getting first data ", username_box
        html_source = browser.page_source
        soup = BeautifulSoup(html_source, 'lxml')
        all_table = soup.find_all('table')
        target_list = []
        target_table = all_table[1]
        target_table_body = target_table.find('tbody')
        rows = target_table_body.find_all('tr')
        # print rows
        rows = list(rows)
        print len(rows)
        if len(rows) > 1:
            for row in range(0, len(rows)):
                cols = rows[row].find_all('td')
                element_dictionary = dict()
                target_content = cols[1].text
                print target_content
                element_dictionary["target_content"] = target_content
                z = (cols[-1].find('a')).get_attribute_list('onclick')
                y = ''.join(z)
                pdf_file = y.replace('"', "").replace("openDocument('", "").replace("')", "")
                # z = cols[-1]
                # str = ''.join(z)
                tag_name = "a"
                # link = browser.find_elements_by_tag_name(tag_name)[0].click()
                link = browser.find_elements_by_tag_name('a')[0].click()
                print ".....................................", link
                print (browser.window_handles)
                # sleep(2)

                if len(browser.window_handles) > 0:
                    link = browser.find_elements_by_tag_name(tag_name)[0].click()
                    # print link
                    print  browser.window_handles
                browser.switch_to_window(browser.window_handles[0])
                # target_url = browser.current_url
                target_url = url + pdf_file
                print "Target Url---------------", target_url
                element_dictionary["target_url"] = target_url
                print element_dictionary
                # browser.close()
                browser.switch_to_window(browser.window_handles[0])
                target_list.append(element_dictionary)
        browser.quit()
        # all_link = LinkObject(target_list, ministry)
        # return all_link

    except urllib2.HTTPError:
        raise PageNotFoundError(url, url + " not found.")
    except exceptions.NoSuchElementException(exceptions):
        print str(exceptions)
        browser.quit()
    except Exception as ex:
        template = "An exception of type {0} occured. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        print message
        browser.quit()

#
if __name__=="__main__":
    run("http://apegazette.cgg.gov.in/","Ministry of Commerce")