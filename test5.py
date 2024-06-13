from html.parser import HTMLParser
import requests
from bs4 import BeautifulSoup

html_tags_list = [
    ('html', 'html'), ('head', 'head'), ('title', 'title'), ('base',),
    ('link',), ('meta',), ('style', 'style'), ('script', 'script'),
    ('noscript', 'noscript'), ('body', 'body'), ('section', 'section'),
    ('nav', 'nav'), ('article', 'article'), ('aside', 'aside'), ('h1', 'h1'),
    ('h2', 'h2'), ('h3', 'h3'), ('h4', 'h4'), ('h5', 'h5'), ('h6', 'h6'),
    ('header', 'header'), ('footer', 'footer'), ('address', 'address'),
    ('p', 'p'), ('hr',), ('pre', 'pre'), ('blockquote', 'blockquote'), ('ol', 'ol'),
    ('ul', 'ul'), ('li', 'li'), ('dl', 'dl'), ('dt', 'dt'), ('dd', 'dd'),
    ('figure', 'figure'), ('figcaption', 'figcaption'), ('main', 'main'), ('div', 'div'),
    ('a', 'a'), ('em', 'em'), ('strong', 'strong'), ('small', 'small'), ('s', 's'),
    ('cite', 'cite'), ('q', 'q'), ('dfn', 'dfn'), ('abbr', 'abbr'), ('ruby', 'ruby'),
    ('rt', 'rt'), ('rp', 'rp'), ('data', 'data'), ('time', 'time'), ('code', 'code'),
    ('var', 'var'), ('samp', 'samp'), ('kbd', 'kbd'), ('sub', 'sub'), ('sup', 'sup'),
    ('i', 'i'), ('b', 'b'), ('u', 'u'), ('mark', 'mark'), ('bdi', 'bdi'), ('bdo', 'bdo'),
    ('span', 'span'), ('br',), ('wbr',), ('ins', 'ins'), ('del', 'del'),
    ('picture', 'picture'), ('source',), ('img',), ('iframe', 'iframe'), ('embed',),
    ('object', 'object'), ('param',), ('video', 'video'), ('audio', 'audio'), ('track',),
    ('map', 'map'), ('area',), ('table', 'table'), ('caption', 'caption'),
    ('colgroup', 'colgroup'), ('col',), ('tbody', 'tbody'), ('thead', 'thead'),
    ('tfoot', 'tfoot'), ('tr', 'tr'), ('td', 'td'), ('th', 'th'), ('form', 'form'),
    ('label', 'label'), ('input',), ('button', 'button'), ('select', 'select'),
    ('datalist', 'datalist'), ('optgroup', 'optgroup'), ('option', 'option'),
    ('textarea', 'textarea'), ('output', 'output'), ('progress', 'progress'),
    ('meter', 'meter'), ('fieldset', 'fieldset'), ('legend', 'legend'),
    ('details', 'details'), ('summary', 'summary'), ('dialog', 'dialog'),
    ('script', 'script'), ('noscript', 'noscript'), ('template', 'template'),
    ('canvas', 'canvas')
]
# List of common HTML tags
html_tags = [
    "html", "head", "title", "base", "link", "meta", "style", "script", "noscript", "body",
    "section", "nav", "article", "aside", "h1", "h2", "h3", "h4", "h5", "h6", "header",
    "footer", "address", "p", "hr", "pre", "blockquote", "ol", "ul", "li", "dl", "dt", "dd",
    "figure", "figcaption", "main", "div", "a", "em", "strong", "small", "s", "cite", "q",
    "dfn", "abbr", "ruby", "rt", "rp", "data", "time", "code", "var", "samp", "kbd", "sub",
    "sup", "i", "b", "u", "mark", "bdi", "bdo", "span", "br", "wbr", "ins", "del", "picture",
    "source", "img", "iframe", "embed", "object", "param", "video", "audio", "track", "map",
    "area", "table", "caption", "colgroup", "col", "tbody", "thead", "tfoot", "tr", "td",
    "th", "form", "label", "input", "button", "select", "datalist", "optgroup", "option",
    "textarea", "output", "progress", "meter", "fieldset", "legend", "details", "summary",
    "dialog", "script", "noscript", "template", "canvas"
]
# Tags that do not have closing tags
self_closing_tags = ["!DOCTYPE html", "area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "param", "source", "track", "wbr"]


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

        global self_closing_tags
        html = self.html
        if tag in self_closing_tags:
            return []
        else:
            if html.find(tag) == -1:
                return []
            else:
                index = []
                index2 = []
                s=0
                lenght = html.count(tag)/2
                print(html[s+len(tag):len(html)])
                for i in range(int(lenght)):
                    start = html.find("<" + tag , s + len(tag), len(html))
                    s = start
                    index.append(start)
                s=0
                for i in range(int(lenght)):
                    start = html.find("</"+tag, s+len(tag), len(html))
                    s=start
                    index2.append(start)


                #____________________________________________________#
                list8 = []
                for i in range(len(index)):
                    for j in range(len(index2)):
                        if html[index[i]+len(tag)-1:index2[j]-1].count("<"+tag) == 0 :
                            list8.append(html[index[i]+len(tag)+1:index2[i]-1].replace("  ", "").replace("\n", " "))





                return list8, index, index2


        # global self_closing_tags
        # html = self.html
        # if tag in self_closing_tags:
        #     return ["0"]
        # else:
        #     if html.find(tag) == -1:
        #         return ["1"]
        #     else:
        #         list4 = []
        #         s=0
        #
        #         lenght = html.count(tag)/2
        #         for i in range(int(lenght)):
        #             start=html.find(tag, s+len(tag), len(html))
        #             s=start
        #             end=html.rfind("/"+tag, s+len(tag), len(html))
        #             list4.append(html[start-1:end+len(tag)+2].replace("\n", "").replace("    ", ""))
        # return list4

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

    def correct_line(self):
        global self_closing_tags
        self.clean_html()
        l1 = ""
        for i in self.html.split("\n"):
            l1 += i.lstrip(" ")


        html_correct = ""
        for i in range(l1.count("<")):
            li1 = l1[i:len(l1)].find("<")
            preview = l1[i:len(l1)].find(">")
            not_close = ""

            for i in self_closing_tags:
                if l1[li1+1:len(l1)].startswith(i) or l1[li1+1:len(l1)].startswith("html") or l1[li1+1:len(l1)].startswith("head") or l1[li1+1:len(l1)].startswith("body"):
                    not_close = i
                    break
                elif not(l1[li1+1:len(l1)].startswith(i)):
                    not_close = ""

            html_correct += l1[li1:preview+1]
            if not_close == "":
                html_correct += "\n"
                print(1)
            else:
                print(2)
                end_tag = l1[li1:len(l1)].find("</"+not_close)
                html_correct += l1[li1+len(l1[li1:preview]):end_tag+1]+"\n"
            print("$", html_correct)
        return None

    def tab(self):
        global self_closing_tags, html_tags
        not_html_tags_list = []#like this : <br>
        for i in html_tags:
            if not(i in self_closing_tags):
                not_html_tags_list.append(i)
        back_slash_tags_closed = []#like this : </a>
        for i in not_html_tags_list:
            back_slash_tags_closed.append("/"+i)

        self.clean_html()
        tags = self.list_tag()
        closed = 0
        not_closed = 0
        html_new_tab_code = ""
        for i in tags:
            s = ()
            var = ""
            e = ()
            for j in i:
                if j in self_closing_tags:
                    closed += 1
                    html_new_tab_code += j+"\n"
                elif j in not_html_tags_list:
                    not_closed += 1
                    s = (tags.index(i), i.index(j))
                elif j in back_slash_tags_closed:
                    not_closed -= 1
                    e = (tags.index(i), i.index(j))

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
h=Html(omid_html)

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


# again = True
# url = input(f"{'\x1b[38;5;4m'}Enter url : ")
# if url == "":
#     html_code_url = omid_html
#     h = Html(html_code_url)
#     print(f"{'\033[32m'}Connected to local html code")
#     line("\033[93m" + "Html code")
#     print('\033[00m' + html_code_url)
#     line("\033[93m" + "Command")
#     again_code = ""
# else:
#     try:
#         page = requests.get(url)
#         sup = BeautifulSoup(page.content, "html.parser")
#         html_code_url = sup.prettify()
#         print(f"{'\033[32m'}Connected to "+f"{'\033[00m'}"+url.split(".")[1])
#         h = Html(html_code_url)
#         line("\033[93m" + "Html code")
#         print('\033[00m' + html_code_url)
#         line("\033[93m" + "Command")
#         again_code = ""
#     except:
#         print(f"{"\033[31m"}Something went")
#         again = False
# while again:
#     x = input(f"{'\033[32m'}Choice one [tag, list_tag, head, body, find_tag, get_tag_map, between, remove_comment, remove_space, clean_html, e (exit), a (again)] : ")
#     if x == "a":
#         if again_code == "":
#             line("\033[93m" + "Don't enter anything")
#         else:
#             x = again_code
#     if x == "e":
#         line("\033[93m"+"Exit")
#         again = False
#         break
#     elif x == "tag":
#         line("\033[93m"+"tag")
#         print('\033[00m'+str(h.tag()))
#     elif x == "list_tag":
#         line("\033[93m"+"list tag")
#         print('\033[00m'+str(h.list_tag()))
#     elif x == "head":
#         line(f"{"\033[93m"}header")
#         print('\033[00m'+str(h.head()))
#     elif x == "body":
#         line(f"{"\033[93m"}body")
#         print(f"{"\033[35m"}body")
#         print('\033[00m'+str(h.body()))
#     elif x == "find_tag":
#         line(f"{"\033[93m"}find tag")
#         print('\033[00m'+str(h.finde_tag(input(f"{'\033[32m'}Enter tag name : "))))
#     elif x == "get_tag_map":
#         line(f"{"\033[93m"}get tag map")
#         print('\033[00m'+str(h.get_tag_map(input(f"{'\033[32m'}Enter tag name : "))))
#     elif x == "between":
#         line(f"{"\033[93m"}between tags")
#         print('\033[00m'+str(h.between(input(f"{'\033[32m'}Enter between tag name : "))))
#     elif x== "remove_comment":
#         line(f"{"\033[93m"}remove comment")
#         h.remove_comment()
#         print('\033[00m'+str(h))
#     elif x == "remove_space":
#         line(f"{"\033[93m"}remove space")
#         h.remove_space()
#         print('\033[00m'+str(h))
#     elif x == "clean_html":
#         line(f"{"\033[93m"}clean html")
#         h.clean_html()
#         print('\033[00m'+str(h))
#     else:
#         line(f"{"\033[31m"}unknown command")
#     again_code = x


m=Html(omid_html)
print(m.correct_line())


# m=h.between("div")
# for i in m:
#     print(i+"\n")