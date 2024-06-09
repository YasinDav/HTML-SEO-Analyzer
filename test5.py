from html.parser import HTMLParser
import requests
from bs4 import BeautifulSoup

class Html:

    def __init__(self, html:str):
        self.html = html

    def __str__(self):
        return str(self.html)

    def tag(self):
        html_tag = self.html.replace('>', "").replace('<', '').split("\n")
        h=[]
        for i in html_tag:
            if not(i == "" or i == " "):
               h.append(i.lstrip(" "))
        return h

    def list_tag(self):
        list_tag = []
        html_tag = self.tag()
        h=[]
        for i in html_tag:
           h.append(i.lstrip(" ").split(" "))
        return h

    def head(self):
        html = self.tag()
        head = html.index("head")
        end_tag = html.index("/head")
        range_of_tag = list(range(head, end_tag))
        head_tag = []
        for i in html:
            if html.index(i) in range_of_tag:
                head_tag.append(i)
        head_tag.pop(0)
        head_tag.pop(-1)
        return head_tag

    def body(self):
        html = self.tag()
        head = html.index("body")
        end_tag = html.index("/body")
        range_of_tag = list(range(head, end_tag))
        head_tag = []
        for i in html:
            if html.index(i) in range_of_tag:
                head_tag.append(i)
        head_tag.pop(0)
        head_tag.pop(-1)
        return head_tag

    def list_page(self):
        link = self.tag()
        link.count("a")

    def finde_tag(self, tag:str):
        list_tag = self.list_tag()
        tags_find = []
        for i in list_tag:
            if i[0] == tag:
                tags_find.append(i)
        return tags_find

    def get_tag_map(self, tag:str):
        list_dict = []
        tags = self.finde_tag(tag)
        for i in tags:
            dict_tag = {}
            dict_tag["tag"] = i[0]
            j=i
            j.pop(0)
            for i in j:
                try:
                    dict_tag[i.split("=")[0]] = i.split("=")[1].replace("\"", "")
                except:
                    dict_tag[i.split("=")[0]] = i.split("=")[0].replace("\"", "")
            list_dict.append(dict_tag)
        return list_dict

    def between(self, tag):
        between_list = []
        tags=self.list_tag()
        print(tags)
        index_list = []
        for i in tags:
            if i[0] == tag:
                index_list.append(tags.index(i))
            if i[0] == "/"+tag:
                index_list.append(tags.index(i))
        print(index_list)
        for i in range(0, len(index_list), 2):
             b_list = []
             for j in range(index_list[i], index_list[i+1]):
                 b_list.append(self.get_tag_map(tags[j]))
             between_list.append(b_list)
        return between_list

    def remove_comment(self):
        tags = self.html.split("\n")
        for i in tags:
            if str(i).lstrip(" ").startswith("<!--")and str(i).lstrip(" ").endswith("-->"):
                tags.remove(i)
        html = ""
        for i in tags:
                html += i + "\n"
        self.html = html
    def remove_space(self):
        tags = self.html.split("\n")
        html = ""
        for i in tags:
            if i == "" or i.isspace():
                pass
            else:
                html += i + "\n"
        self.html = html
    def clean_html(self):
        self.remove_comment()
        self.remove_space()
    class Parser(HTMLParser):
            def __init__(self):
                super().__init__()
                self.title = ""
                self.paragraphs = []

            def handle_starttag(self, tag, attrs):
                if tag == "title":
                    self.title = "Title: "
                elif tag == "p":
                    self.paragraphs.append("Paragraph: ")

            def handle_data(self, data):
                if self.title:
                    self.title += data
                if self.paragraphs:
                    self.paragraphs[-1] += data

            def get_title(self):
                return self.title

            def get_paragraphs(self):
                return self.paragraphs

line = lambda title : print(f"{"\033[00m"}-"*30+title+f"{"\033[00m"}-"*30)

# line("--")
# html_string = """
# <html>
# <head>
# <title>Sample HTML Page</title>
# </head>
# <body>
# <h1>Welcome to my website!
# <p>This is a sample HTML page.
# </body>
# </html>
# """
#
# parser = Html.Parser()
# parser.feed(html_string)
#
# title = parser.get_title()
# paragraphs = parser.get_paragraphs()
#
# print(title)
# for paragraph in paragraphs:
#     print(paragraph)
#
# line("-------")
# line("-------")
# line("-------")
# line("-------")
# line("-------")
# line("-------")
# line("-------")

# page = requests.get("https://www.digikala.com/")
# sup = BeautifulSoup(page.content, "html.parser")
# html_code_digikala = sup.prettify()

omid_html = """
<!DOCTYPE html>
   <html lang="en">
   <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">

      <!--=============== REMIXICONS ===============-->
      <link href="https://cdn.jsdelivr.net/npm/remixicon@2.5.0/fonts/remixicon.css" rel="stylesheet">

      <!--=============== CSS ===============-->
      <link rel="stylesheet" href="assets/css/styles.css">

      <title>Animated login form - Bedimcode</title>
   </head>
   <body>
      <div class="login">
         <img src="assets/img/login-bg.png" alt="login image" class="login__img">

         <form action="" class="login__form">
            <h1 class="login__title">Login</h1>

            <div class="login__content">
               <div class="login__box">
                  <i class="ri-user-3-line login__icon"></i>

                  <div class="login__box-input">
                     <input type="email" required class="login__input" id="login-email" placeholder=" ">
                     <label for="login-email" class="login__label">Email</label>
                  </div>
               </div>

               <div class="login__box">
                  <i class="ri-lock-2-line login__icon"></i>

                  <div class="login__box-input">
                     <input type="password" required class="login__input" id="login-pass" placeholder=" ">
                     <label for="login-pass" class="login__label">Password</label>
                     <i class="ri-eye-off-line login__eye" id="login-eye"></i>
                  </div>
               </div>
            </div>

            <div class="login__check">
               <div class="login__check-group">
                  <input type="checkbox" class="login__check-input" id="login-check">
                  <label for="login-check" class="login__check-label">Remember me</label>
               </div>

               <a href="#" class="login__forgot">Forgot Password?</a>
            </div>

            <button type="submit" class="login__button">Login</button>

            <p class="login__register">
               Don't have an account? <a href="#">Register</a>
            </p>
         </form>
      </div>
      
      <!--=============== MAIN JS ===============-->
      <script src="assets/js/main.js"></script>
   </body>
</html>
"""


#
# h=Html(omid_html)
# line("orginal code")
# print(omid_html)
# line("-")
# line("tag")
# print(h.tag())
# line("list tag")
# print(h.list_tag())
# line("head")
# print(h.head())
# line("body")
# print(h.body())
# line("finde tag")
# print(h.finde_tag("div"))
# line("get tag map")
# print(h.get_tag_map("div"))
# line("between")
# for i in h.between("a"):
#     print("[")
#     for j in i:
#         print(" ",j)
#     print("]")
# line("----")
# line("----")
# h.remove_comment()
# print(h)
# line("#####")
# h.remove_space()
# print(h)
again = True
url = input(f"{'\x1b[38;5;4m'}Enter url : ")
html_code_url = ""
try:
    page = requests.get(url)
    sup = BeautifulSoup(page.content, "html.parser")
    html_code_url = sup.prettify()
    print(f"{'\033[32m'}Connected to "+f"{'\033[00m'}"+url.split(".")[1])
    h = Html(html_code_url)
    line("\033[93m" + "Html code")
    print('\033[00m' + html_code_url)
    line("\033[93m" + "Command")
    again_code = ""
except:
    print(f"{"\033[31m"}Something went")
    again = False
while again:
    x = input(f"{'\033[32m'}Choice one [tag, list_tag, head, body, find_tag, get_tag_map, between, remove_comment, remove_space, clean_html, exit, a (again)] : ")
    if x == "a":
        if again_code == "":
            line("\033[93m" + "Don't enter anything")
        x = again_code
    if x == "exit":
        line("\033[93m"+"Exit")
        again = False
        break
    elif x == "tag":
        line("\033[93m"+"tag")
        print('\033[00m'+str(h.tag()))
    elif x == "list_tag":
        line("\033[93m"+"list tag")
        print('\033[00m'+str(h.list_tag()))
    elif x == "head":
        line(f"{"\033[93m"}header")
        print('\033[00m'+str(h.head()))
    elif x == "body":
        line(f"{"\033[93m"}body")
        print(f"{"\033[35m"}body")
        print('\033[00m'+str(h.body()))
    elif x == "find_tag":
        line(f"{"\033[93m"}find tag")
        print('\033[00m'+str(h.finde_tag(input(f"{'\033[32m'}Enter tag name : "))))
    elif x == "get_tag_map":
        line(f"{"\033[93m"}get tag map")
        print('\033[00m'+str(h.get_tag_map(input(f"{'\033[32m'}Enter tag name : "))))
    elif x == "between":
        line(f"{"\033[93m"}between")
        print('\033[00m'+str(h.between(input(f"{'\033[32m'}Enter between tag name : "))))
    elif x== "remove_comment":
        line(f"{"\033[93m"}remove comment")
        h.remove_comment()
        print('\033[00m'+str(h))
    elif x == "remove_space":
        line(f"{"\033[93m"}remove space")
        h.remove_space()
        print('\033[00m'+str(h))
    elif x == "clean_html":
        line(f"{"\033[93m"}clean html")
        h.clean_html()
        print('\033[00m'+str(h))
    else:
        line(f"{"\033[31m"}unknown command")
    again_code = x