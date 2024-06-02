import requests
from bs4 import BeautifulSoup

class Html:

    def __init__(self, html:str):
        self.html = html

    def tag(self):
        html_tag = self.html.replace('>', "").replace('<', '').split("\n")
        h=[]
        for i in html_tag:
           h.append(i.lstrip(" "))
        return h

    def list_tag(self):
        list_tag = []
        html_tag = self.html.replace('>', "").replace('<', '').split("\n")
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
        tags=self.tag()
        list_tag = []
        for i in tags:
            list_tag.append(self.get_tag_map(i.split(" ")[0]))
        for i in list_tag:
            if i["tag"] :
                pass


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
print(omid_html)
print(h.list_tag())
print(h.head())
print("-"*100)
print(h.finde_tag("form"))
print("-"*100)
print(h.get_tag_map("form"))