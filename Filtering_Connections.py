from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
import Sending_Requests

stop = set(stopwords.words('english'))

specifications = {"machine", "google", "learning", "computer", "vision", "image", "processing", "developer", "engineer", "ai"
                  "data", "apple","scientist", "analyst", "enthusiast", "deep", "learning", "microsoft", "intel", "ibm", "nlp", "iiit", "accenture", "hp", "dell"}


def Relevant_Requests_Sorting(ul, all_items, n):
    tokenizer = RegexpTokenizer(r'\w+')
    
    for item in all_items:
        li_id = item.get_attribute("id")
        each_li = ul.find_element_by_id(li_id)
        li_id_num = int(li_id[5:])

        li_a = each_li.find_element_by_id("ember"+str(li_id_num+4))
        name = li_a.find_element_by_class_name(
            "mn-discovery-person-card__name.t-14.t-black.t-bold")
        occupation = li_a.find_element_by_class_name(
            "mn-discovery-person-card__occupation.t-12.t-black--light.t-normal")

        l = {i for i in tokenizer.tokenize(
            (occupation.text).lower()) if i not in stop}

        if len(specifications.intersection(l)) > 1:
            print("Sent Request to: "+name.text, end="\t\t")
            print(occupation.text)
            n = Sending_Requests.Send_Request(each_li, li_id_num, n)

    return n

def My_Network(browser):
    network_url = "https://www.linkedin.com/mynetwork/"
    no_of_requests_sent = 0
    try:
        while True:
            browser.get((network_url))
            ul = browser.find_element_by_id("ember58")
            all_items = ul.find_elements_by_tag_name("li")

            no_of_requests_sent = Relevant_Requests_Sorting(ul, all_items, no_of_requests_sent)
            print(no_of_requests_sent)

    except KeyboardInterrupt:
        print("Requests Sent: ",no_of_requests_sent)
        pass