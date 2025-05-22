import requests
from lxml import html 
"""
Написати 25 XPath та 25 CSS локаторів для сайту https://qauto2.forstudy.space/
"""

username = "guest"
passwd = "welcome2qauto"
url = f"https://{username}:{passwd}@qauto2.forstudy.space"

def get_html_content(url):
    response = requests.get(url)
    return response.text

def get_tree(html_text):
    return html.fromstring(html_text)

def find_by(tree, locator):
    return tree.xpath(locator)

   
    
if __name__ == "__main__":
    html_content = get_html_content(url)
    tree = get_tree(html_content)
    
    signup_button = find_by(tree, './/button[@class="hero-descriptor_btn btn btn-primary"]')
    print("Кнопка Sign Up", signup_button)
    
    title = find_by(tree, './/h1[@class="hero-descriptor_title display-2"]')
    print("Title 'Do more!'", title)
    
    text = find_by(tree, './/p[contains(text(), "Keep track of your replacement schedule and plan your vehicle maintenance expenses in advance.")]')
    print("Text:", text)

    paragraph = find_by(tree, '//*[@id="aboutSection"]')
    print("Watch over 100 instructions and repair your car yourself.", paragraph)
    
    link = find_by(tree, '//a[@class="header_logo"]')
    print("Link ithillel.ua", link)
    
    email = find_by(tree, '//*[@class="contacts_link h4"]')
    print("Email to support@ithillel.ua", email)
    
    
    
    
    
    
    
    
    
    
    
    