from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
import Sending_Requests
import time,os

stop = set(stopwords.words('english'))

specifications = {"machine", "google", "learning", "computer", "vision", "image", "processing","developer", "engineer", "ai", "developer", "python","computing", "ml", "medical",
                  "data","CEO", "CTO","linkedin","manager","paytm","visa","hyderabad","amazon","research","flipkart","quantum","tesla","facebook","apple","scientist", "analyst", "deep", "learning", "microsoft", "intel", "ibm", "nlp", "accenture", "hp", "dell"}


def Relevant_Requests_Sorting(ul, all_items, n):
    tokenizer = RegexpTokenizer(r'\w+')
    empty = 0
    for item in all_items:
        li_id = item.get_attribute("id")
        each_li = ul.find_element_by_id(li_id)
        li_id_num = int(li_id[5:])

        li_a = each_li.find_element_by_id("ember"+str(li_id_num+5))
        name = li_a.find_element_by_class_name(
            "discover-person-card__name.t-16.t-black.t-bold")
        occupation = li_a.find_element_by_class_name(
            "discover-person-card__occupation.t-14.t-black--light.t-normal")

        l = {i for i in tokenizer.tokenize(
            (occupation.text).lower()) if i not in stop}
        if l == {}:
            empty+=1
        if empty >= 10:
            exit()
        print(l)
        if len(specifications.intersection(l)) > 1:
            n = Sending_Requests.Send_Request(each_li, li_id_num, n)

    return n

def My_Network(browser):
        while True:
            network_url = "https://www.linkedin.com/mynetwork/"
            no_of_requests_sent = 0
            i = 0
            try:
                browser.get((network_url))
                time.sleep(3)
                while i!=10000:
                    print(i)
                    browser.execute_script("window.scrollTo(0,"+str(i)+")")
                    i+=1000
                    time.sleep(2)
                    ul_class = browser.find_element_by_class_name("js-discover-entity-list__pymk.discover-entity-list.ember-view")
                    ul_id = ul_class.get_attribute("id")
                    ul = browser.find_element_by_id(ul_id)
                    all_items = ul.find_elements_by_tag_name("li")
                    no_of_requests_sent = Relevant_Requests_Sorting(ul, all_items, no_of_requests_sent)
                    print(no_of_requests_sent)
                    print(len(all_items))

            except KeyboardInterrupt:
                print("Requests Sent: ",no_of_requests_sent)
                pass