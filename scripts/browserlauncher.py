import webbrowser
import time

googleUrl = "http://www.google.com.tr"
socialMediUrls = ["http://www.twitter.com", "http://www.facebook.com", "http://www.instagram.com", "http://www.linkedin.com"]

def openNewTab(socialMediUrls):
    for page in socialMediUrls:
        webbrowser.open_new_tab(page)
        time.sleep(0.25)       

def openNewPage(Url):
        webbrowser.open(Url, new=0, autoraise=False)
        time.sleep(0.5)

def main():
    openNewPage(googleUrl)    
    openNewTab(socialMediUrls)

if __name__ == '__main__':
        main()


