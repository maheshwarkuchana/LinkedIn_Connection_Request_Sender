from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
import Sending_Requests
import time
import os
import math

stop = set(stopwords.words('english'))

specifications = {"machine", "google", "learning", "computer", "vision", "image", "processing", "ai", "computing", "ml", "medical", "deepmind",
                  "data", "CEO", "CTO", "linkedin", "paytm", "visa", "amazon", "research", "flipkart", "quantum", "tesla", "facebook", "apple", "scientist", "analyst", "deep", "learning", "microsoft", "intel", "ibm", "accenture", "hp", "dell"}


def Relevant_Requests_Sorting(ul, all_items, n):
    tokenizer = RegexpTokenizer(r'\w+')
    empty = 0
    for item in all_items:
        li_id = item.get_attribute("id")
        each_li = ul.find_element_by_id(li_id)

        li_a = each_li.find_element_by_class_name(
            "discover-entity-type-card__link.ember-view")
        name = li_a.find_element_by_class_name(
            "discover-person-card__name.t-16.t-black.t-bold")
        occupation = li_a.find_element_by_class_name(
            "discover-person-card__occupation.t-14.t-black--light.t-normal")

        l = set({i for i in tokenizer.tokenize(
            (occupation.text).lower()) if i not in stop})
        if len(l) == 0:
            empty += 1
        if empty >= 10:
            return math.inf
        # print(l)
        if len(specifications.intersection(l)) > 1:
            n = Sending_Requests.Send_Request(
                each_li, n, name.text, occupation.text)

    return n


def My_Network(browser):
    no_of_requests_sent = 0
    network_url = "https://www.linkedin.com/mynetwork/"
    i = 0
    print("Initiating....")
    print("********************************************************************************")
    
    try:
        browser.get((network_url))
        time.sleep(3)
        while i!=20000:
            browser.execute_script("window.scrollTo(0,"+str(i)+")")
            i += 1000
            time.sleep(2)

            ul_class = browser.find_element_by_class_name(
                "js-discover-entity-list__pymk.discover-entity-list.ember-view")
            ul_id = ul_class.get_attribute("id")
            ul = browser.find_element_by_id(ul_id)
            all_items = ul.find_elements_by_tag_name("li")

        no_of_requests_sent = Relevant_Requests_Sorting(
            ul, all_items, no_of_requests_sent)
        print(str(no_of_requests_sent) +"out of "+ str(len(all_items)))
        My_Network(browser)
        if no_of_requests_sent == math.inf:
            browser.quit()
            print(
                "********************************************************************************")
            print("Total Number of Connection Requests sent are: ",
                    no_of_requests_sent)
            exit()

    except KeyboardInterrupt:
        print("Requests Sent: ", no_of_requests_sent)
        pass
