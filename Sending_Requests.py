def Send_Request(Person, n, name, occupation):
    
    li_button = Person.find_element_by_class_name("full-width.artdeco-button.artdeco-button--2.artdeco-button--full.artdeco-button--secondary.ember-view")
    try:
        li_button.click()
        print("Request Sent to: ", name, " - ", occupation)
        n = n+1
    except:
        pass
    
    return n
