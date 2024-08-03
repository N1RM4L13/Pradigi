import re
import requests
from bs4 import BeautifulSoup as bs
import random
import json

uastrings = [
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36", \
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.72 Safari/537.36", \
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10) AppleWebKit/600.1.25 (KHTML, like Gecko) Version/8.0 Safari/600.1.25", \
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:33.0) Gecko/20100101 Firefox/33.0", \
        "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36", \
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36", \
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/600.1.17 (KHTML, like Gecko) Version/7.1 Safari/537.85.10", \
        "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko", \
        "Mozilla/5.0 (Windows NT 6.3; WOW64; rv:33.0) Gecko/20100101 Firefox/33.0", \
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.104 Safari/537.36" \
        ]


def AboutUs():
  headers = {"User-Agent":random.choice(uastrings)}
  url : str =f"https://pratham.org/about/"
  web = requests.get(url, headers=headers)
  if web.status_code == 200:
    scrap = bs(web.text, "html.parser")

  data = scrap.find("div", class_="site").find("div", id="content")

  Aboutus = "\n\n".join([(data.find("div", id="panel-w5c08297618721-0-0-0").text.strip()+"\n"+
  "\n".join([i.text.strip() for i in data.find("div", id="panel-w5c08297618721-0-0-1").find_all("p")])),

  (data.find("div", id='pg-w5d31c18fd4857-1').find("div", id="pgc-w5d31c18fd4857-1-0").find("h3").text.strip() +"\n"+
  "\n".join([i.text.strip() for i in data.find("div", id='pg-w5d31c18fd4857-1').find("div", id="pgc-w5d31c18fd4857-1-0").find_all("p")])),

  (data.find("div", id='pg-w5d31c18fd4857-1').find("div", id="pgc-w5d31c18fd4857-1-1").find("h3").text.strip()+"\n"+
  "\n".join([i.text.strip() for i in data.find("div", id='pg-w5d31c18fd4857-1').find("div", id="pgc-w5d31c18fd4857-1-1").find_all("p")])),

  (data.find("div", id='pg-w5d31c18fd4857-2').find("div", id="pgc-w5d31c18fd4857-2-0").find("h3").text.strip()+"\n"+
  "\n".join([i.text.strip() for i in data.find("div", id='pg-w5d31c18fd4857-2').find("div", id="pgc-w5d31c18fd4857-2-0").find_all("p")])),

  (data.find("div", id='pg-w5d31c18fd4857-2').find("div", id="pgc-w5d31c18fd4857-2-0").find("h3").text.strip()+"\n"+
  "\n".join([i.text.strip() for i in data.find("div", id='pg-w5d31c18fd4857-2').find("div", id="pgc-w5d31c18fd4857-2-0").find_all("p")])),

  (data.find("div", id="pg-w5d31c18fd4857-3").find("h3").text.strip()+"\n"+
  "\n".join([i.text.strip() for i in data.find("div", id="pg-w5d31c18fd4857-3").find_all("p")]))])

  return Aboutus


def board(profile):
  headers = {"User-Agent":random.choice(uastrings)}
  url : str = profile
  web = requests.get(url, headers=headers)
  if web.status_code == 200:
    scrap = bs(web.text, "html.parser")
  data = scrap.find("div", class_="site").find("div", id="content")

  head = data.find("h1").text.strip()
  date = "-".join([data.find("div", class_="content-wrapper").find("span", class_="day").text.strip(),data.find("div", class_="content-wrapper").find("span", class_="month").text.strip(),data.find("div", class_="content-wrapper").find("span", class_="year").text.strip()])
  post = " - ".join([i.text.strip() for i in data.find("div", class_="content-wrapper").find("div", class_="entry-content").find_all("span")[:2]])
  h_text = "\n".join([i.text.strip() for i in data.find("div", class_="content-wrapper").find("div", class_="entry-content").find_all("p")])

  return "\n".join([head , h_text, post, date])

def Board():
  headers = {"User-Agent":random.choice(uastrings)}
  url : str =f"https://pratham.org/about/board/"
  web = requests.get(url, headers=headers)
  if web.status_code == 200:
    scrap = bs(web.text, "html.parser")

  data = scrap.find("div", class_="site").find("div", id="content")

  intro = (data.find("div", id="panel-2420-0-0-0").find("h3").text.strip()+"\n"+
  "\n".join([i.text.strip() for i in data.find("div", id="panel-2420-0-0-1").find_all("p")]))

  members = ['https://pratham.org/2019/02/08/ajay-g-piramal-chairman-pratham-education-foundation/', 'https://pratham.org/2019/05/04/arvind-sanger/', 'https://pratham.org/2020/10/20/banmali-agrawala/', 'https://pratham.org/2019/05/04/deepak-raj/', 'https://pratham.org/2019/05/04/dinyar-s-devitre/', 'https://pratham.org/2019/05/04/jalaj-dani/', 'https://pratham.org/2019/05/04/dr-madhav-chavan/', 'https://pratham.org/2019/05/04/nirmal-jain/', 'https://pratham.org/2019/05/04/pramit-jhaveri/', 'https://pratham.org/2019/05/04/ramesh-mangaleswaran/', 'https://pratham.org/2019/05/04/dr-rukmini-banerji/', 'https://pratham.org/2019/05/04/sanjay-nayar/', 'https://pratham.org/2019/12/25/sanjiv-malhotra/', 'https://pratham.org/2019/05/21/vibha-paul/', 'https://pratham.org/2019/05/04/vijay-goradia/', 'https://pratham.org/2019/12/25/vilas-gadkari-2/']
  return intro + "\n\n"+ "\n\n".join([board(i) for i in members])


def Leadership():
  headers = {"User-Agent":random.choice(uastrings)}
  url : str =f"https://pratham.org/about/leadership/"
  web = requests.get(url, headers=headers)
  if web.status_code == 200:
    scrap = bs(web.text, "html.parser")

  data = scrap.find("div", class_="site").find("div", id="content")

  intro = (data.find("div", id="panel-2422-0-0-0").find("h3").text.strip()+"\n"+
  "\n".join([i.text.strip() for i in data.find("div", id="panel-2422-0-0-1").find_all("p")]))

  leader= ['https://pratham.org/2020/05/14/dr-madhav-chavan-2/',
  'https://pratham.org/2019/05/21/dr-rukmini-banerji-3/',
  'https://pratham.org/2019/05/21/dr-wilima-wadhwa/',
  'https://pratham.org/2019/05/07/ms-farida-lambay/',
  'https://pratham.org/2019/07/11/usha-rane/']

  return intro + "\n\n"+ "\n\n".join([board(i) for i in leader])


def TeachingRightLevel():
  headers = {"User-Agent":random.choice(uastrings)}
  url : str =f"https://pratham.org/about/teaching-at-the-right-level/"
  web = requests.get(url, headers=headers)
  if web.status_code == 200:
    scrap = bs(web.text, "html.parser")
  data = scrap.find("div", class_="site").find("div", id="content")

  all_data = [(data.find("div", class_="max-width panel-row-style panel-row-style-for-2424-0").find("div", id="panel-2424-0-0-0").text.strip() +"\n"+
  "\n".join([i.text.strip() for i in data.find("div", class_="max-width panel-row-style panel-row-style-for-2424-0").find("div", id="panel-2424-0-0-1").find_all("p")]+
  [i.text.strip() for i in data.find("div", class_="max-width panel-row-style panel-row-style-for-2424-0").find("div", id="panel-2424-0-0-1").find_all("li")])),

  (data.find("div", class_="max-width panel-row-style panel-row-style-for-2424-0").find("div", id="panel-2424-0-0-2").text.strip() +"\n"+
  "\n".join([i.text.strip() for i in data.find("div", class_="max-width panel-row-style panel-row-style-for-2424-0").find("div", id="panel-2424-0-0-3").find_all("p")]) +"\n"+
  "\n\n".join(["  |  ".join([j.text.strip() for j in i.find_all("td")]) for i in data.find("div", class_="max-width panel-row-style panel-row-style-for-2424-0").find("div", id="panel-2424-0-0-3").find_all("tr") ])),

  data.find("div", class_="max-width panel-row-style panel-row-style-for-2424-0").find("div", id="panel-2424-0-0-4").text.strip(),

  (data.find("div", class_="max-width panel-row-style panel-row-style-for-2424-0").find("div", id="panel-2424-0-0-6").text.strip()+"\n"+
  "\n".join([i.text.strip() for i in data.find("div", class_="max-width panel-row-style panel-row-style-for-2424-0").find("div", id="panel-2424-0-0-7").find_all("p")])+"\n"+
  ("  --  ".join([i.text.strip() for i in data.find("div", class_="max-width panel-row-style panel-row-style-for-2424-0").find("div", id="panel-2424-0-0-7").find_all("th")])
    +"\n"+
    "\n\n".join(["  |  ".join([j.text.strip() for j in i.find_all("td")]) for i in data.find("div", class_="max-width panel-row-style panel-row-style-for-2424-0").find("div", id="panel-2424-0-0-7").find_all("tr") ]))),

  (data.find("div", class_="max-width panel-row-style panel-row-style-for-2424-0").find("div", id="panel-2424-0-0-8").text.strip() +"\n"+
    "\n".join([i.text.strip() for i in data.find("div", class_="max-width panel-row-style panel-row-style-for-2424-0").find("div", id="panel-2424-0-0-9").find_all("p")]))]

  return "\n\n".join(all_data)


def Recognition():
  headers = {"User-Agent":random.choice(uastrings)}
  url : str =f"https://pratham.org/about/recognition/"
  web = requests.get(url, headers=headers)
  if web.status_code == 200:
    scrap = bs(web.text, "html.parser")
  data = scrap.find("div", class_="site").find("div", id="content")
  intro = "\n".join([i.text.strip() for i in data.find("div", id="panel-2426-0-0-0").find_all("p")])
  award = [board(i) for i in [i.find("a").get("href") for i in data.find("div", id="panel-2426-0-0-2").find_all("li")]]+ [board(i) for i in [i.find("a").get("href") for i in data.find("div", id="panel-2426-0-0-4").find_all("li")]]
  return intro +"\n\n"+ "\n\n".join(award)


headers = {"User-Agent":random.choice(uastrings)}
url : str =f"https://pratham.org/resources/publications/"
web = requests.get(url, headers=headers)
if web.status_code == 200:
  scrap = bs(web.text, "html.parser")
data = scrap.find("div", class_="site")

program = [(i.text, i.get("href")) for i in data.find("li", id="menu-item-16726").find("ul").find_all("a")]


def Education():
  headers = {"User-Agent":random.choice(uastrings)}
  url : str =program[0][1]
  web = requests.get(url, headers=headers)
  if web.status_code == 200:
    scrap = bs(web.text, "html.parser")
  data = scrap.find("div", class_="site")
  intro = "\n".join([i.text.strip() for i in data.find("div", id="panel-2126-0-0-0").find_all("p")])
  edu = [(data.find("div", id=f"pg-w64c64e0c673e4-{k}").find("h3").text.strip() +"\n"+"".join([i.text.strip() for i in data.find("div", id=f"pg-w64c64e0c673e4-{k}").find_all("p") if len(i.text.strip().split())>2]).split("\n\n")[0]) for k in range(5)]
  return intro + "\n\n" + "\n\n".join(edu)


def HamaraGaon():
  headers = {"User-Agent":random.choice(uastrings)}
  url : str =program[1][1]
  web = requests.get(url, headers=headers)
  if web.status_code == 200:
    scrap = bs(web.text, "html.parser")
  data = scrap.find("div", class_="site")
  target_class = "kc-elm kc-css-"
  all_card = data.find("div", class_="kc-col-container").find_all("div", class_=lambda c: target_class in c)
  return "\n".join([i.text.strip() for i in all_card[:-8]])


def clean_text(text):
    # Remove extra newlines
    text = re.sub(r'\n+', '\n', text)

    # Replace multiple tabs with a single tab
    text = re.sub(r'\t+', '\t', text)

    # Split the text into lines
    lines = text.split('\n')

    # Process each line
    cleaned_lines = []
    for line in lines:
        if line.strip():  # If the line is not empty
            # If the line starts with a single tab, consider it as a heading
            if line.startswith('\t'):
                cleaned_lines.append('\n\n' + line.strip())
            else:
                cleaned_lines.append(line.strip())

    # Join the lines into a single string
    cleaned_text = '\n'.join(cleaned_lines)

    return cleaned_text

def EarlyChildhood():
  headers = {"User-Agent":random.choice(uastrings)}
  url : str =program[2][1]
  web = requests.get(url, headers=headers)
  if web.status_code == 200:
    scrap = bs(web.text, "html.parser")
  data = scrap.find("div", class_="site")

  intro = data.find("div", id="panel-11703-0-0-0").find("h3").text.strip() +"\n"+"\n".join([i.text.strip() for i in data.find("div", id="panel-11703-0-0-1").find_all("p")])
  return intro +"\n\n" + clean_text(data.find("div", id="pgc-w65df035669446-0-0").text.strip()).replace("\n\n\n", "\n\n")


def ElementaryYears():
  headers = {"User-Agent":random.choice(uastrings)}
  url : str =program[3][1]
  web = requests.get(url, headers=headers)
  if web.status_code == 200:
    scrap = bs(web.text, "html.parser")
  data = scrap.find("div", class_="site")

  return "\n\n".join([data.find("div", class_="kc-elm kc-css-708673 kc_col-sm-9 kc_column kc_col-sm-9").text.strip(),
  data.find("section", class_="kc-elm kc-css-901347 kc_row hgaon").text.strip(),
  data.find("section", class_="kc-elm kc-css-615994 kc_row hgaon").text.strip(),
  data.find("section", class_="kc-elm kc-css-865614 kc_row").text.strip(),
  data.find("section", class_="kc-elm kc-css-318755 kc_row hgaon").text.strip(),
  data.find("section", class_="kc-elm kc-css-172426 kc_row").text.strip()])


def SecondChance():
  headers = {"User-Agent":random.choice(uastrings)}
  url : str =program[4][1]
  web = requests.get(url, headers=headers)
  if web.status_code == 200:
    scrap = bs(web.text, "html.parser")
  data = scrap.find("div", class_="site")

  return "\n\n".join([data.find("div", class_="kc-elm kc-css-796833 kc_text_block white-box table-box introBoxCol").text.strip(),
  data.find("section", class_="kc-elm kc-css-23360 kc_row").text.strip(),
  data.find("section", class_="kc-elm kc-css-206654 kc_row hgaon").text.strip(),
  data.find("section", class_="kc-elm kc-css-217394 kc_row").text.strip(),
  data.find("section", class_="kc-elm kc-css-380604 kc_row girl-scale").text.strip(),
  data.find("section", class_="kc-elm kc-css-771641 kc_row").text.strip(),
  data.find("section", class_="kc-elm kc-css-604994 kc_row hgaon").text.strip()])


def DigitalInitiatives():
  headers = {"User-Agent":random.choice(uastrings)}
  url : str =program[5][1]
  web = requests.get(url, headers=headers)
  if web.status_code == 200:
    scrap = bs(web.text, "html.parser")
  data = scrap.find("div", class_="site").find("div", id="content")
  return clean_text(data.find("div", class_="panel-grid panel-has-style").text.strip().split("Beyond Elementary Vocational Training")[0])


def VocationalTraining():
  headers = {"User-Agent":random.choice(uastrings)}
  url : str =program[6][1]
  web = requests.get(url, headers=headers)
  if web.status_code == 200:
    scrap = bs(web.text, "html.parser")
  data = scrap.find("div", class_="site")

  return "\n\n".join([data.find("div", class_="kc-elm kc-css-78939 kc_text_block white-box table-box introBoxCol").text.strip(),
  data.find("section", class_="kc-elm kc-css-683780 kc_row").text.strip(),
  data.find("section", class_="kc-elm kc-css-145614 kc_row hgaon").text.strip(),
  data.find("section", class_="kc-elm kc-css-523260 kc_row").text.strip(),
  data.find("section", class_="kc-elm kc-css-766893 kc_row rscale").text.strip(),
  data.find("section", class_="kc-elm kc-css-141953 kc_row").text.strip(),
  data.find("section", class_="kc-elm kc-css-617748 kc_row hgaon voc-app").text.strip(),
  data.find("section", class_="kc-elm kc-css-774338 kc_row hgaon mx-wid2").text.strip(),
  data.find("section", class_="kc-elm kc-css-266079 kc_row hgaon").text.strip(),
  data.find("section", class_="kc-elm kc-css-409843 kc_row hgaon").text.strip()])


def PrathamCouncil():
  headers = {"User-Agent":random.choice(uastrings)}
  url : str =program[7][1]
  web = requests.get(url, headers=headers)
  if web.status_code == 200:
    scrap = bs(web.text, "html.parser")
  data = scrap.find("div", class_="site")

  return "\n\n".join([data.find("div", class_="kc-elm kc-css-307359 kc_col-sm-9 kc_column kc_col-sm-9").text.strip(),
  data.find("section", class_="kc-elm kc-css-326432 kc_row hgaon").text.strip(),
  data.find("section", class_="kc-elm kc-css-281164 kc_row hgaon").text.strip(),
  data.find("section", class_="kc-elm kc-css-157956 kc_row outcomes").text.strip(),
  data.find("section", class_="kc-elm kc-css-439167 kc_row hgaon").text.strip()])


def AnnualStatus():
  headers = {"User-Agent":random.choice(uastrings)}
  url : str =program[8][1]
  web = requests.get(url, headers=headers)
  if web.status_code == 200:
    scrap = bs(web.text, "html.parser")
  data = scrap.find("div", class_="site")

  return "\n\n".join([data.find("div", class_="kc-elm kc-css-559555 kc_text_block white-box table-box introBoxCol").text.strip(),
  data.find("section", class_="kc-elm kc-css-491100 kc_row hgaon").text.strip(),
  data.find("section", class_="kc-elm kc-css-109303 kc_row hgaon").text.strip(),
  data.find("section", class_="kc-elm kc-css-982027 kc_row outcomes rsapp").text.strip(),
  data.find("section", class_="kc-elm kc-css-558684 kc_row hgaon").text.strip(),
  data.find("section", class_="kc-elm kc-css-796757 kc_row res-reach").text.strip(),
  data.find("section", class_="kc-elm kc-css-101198 kc_row hgaon").text.strip()])


def IAmPratham():
  headers = {"User-Agent":random.choice(uastrings)}
  url : str = "https://www.pratham.org/iampratham/"
  web = requests.get(url, headers=headers)
  if web.status_code == 200:
    scrap = bs(web.text, "html.parser")
  data = scrap.find("div", class_="site")

  return "\n\n".join([data.find("section", class_="kc-elm kc-css-939520 kc_row").text.strip(),
  data.find("section", class_="kc-elm kc-css-128339 kc_row").text.strip(),
  "\n".join(data.find("section", class_="kc-elm kc-css-354446 kc_row").text.strip().split("\n")[:2]),
  data.find("section", class_="kc-elm kc-css-666544 kc_row").text.strip()])


def DaanUtsav():
  headers = {"User-Agent":random.choice(uastrings)}
  url : str = "https://www.pratham.org/daan-utsav-2/"
  web = requests.get(url, headers=headers)
  if web.status_code == 200:
    scrap = bs(web.text, "html.parser")
  data = scrap.find("div", class_="site")

  return data.find("section", class_="kc-elm kc-css-922077 kc_row").text.strip()[21:]


def CAMaLKaCamp():
  headers = {"User-Agent":random.choice(uastrings)}
  url : str = "https://www.pratham.org/camal-ka-camp-2023/"
  web = requests.get(url, headers=headers)
  if web.status_code == 200:
    scrap = bs(web.text, "html.parser")
  data = scrap.find("div", class_="site")

  return "\n\n".join([data.find("section", class_="kc-elm kc-css-943244 kc_row").text.strip(),
  data.find("section", class_="kc-elm kc-css-447512 kc_row").text.strip(),
  data.find("section", class_="kc-elm kc-css-593617 kc_row").text.strip(),
  data.find("section", class_="kc-elm kc-css-896575 kc_row outcomes").text.strip(),
  data.find("section", class_="kc-elm kc-css-902695 kc_row").text.strip(),
  data.find("section", class_="kc-elm kc-css-513460 kc_row").text.strip(),
  data.find("section", class_="kc-elm kc-css-608148 kc_row").text.strip(),
  data.find("section", class_="kc-elm kc-css-401355 kc_row").text.strip(),
  data.find("section", class_="kc-elm kc-css-740713 kc_row").text.strip(),
  data.find("section", class_="kc-elm kc-css-299403 kc_row").text.strip(),
  data.find("section", class_="kc-elm kc-css-327862 kc_row outcomes").text.strip()])


metaData = [{"AboutUs": AboutUs(), "Cat":[{"Board":Board(), "SubCat":[]}, {"Leadership":Leadership(), "SubCat":[]}, {"Teaching at the Right Level": TeachingRightLevel(), "SubCat":[]}, {"Recognition":Recognition(), "SubCat":[]}]},
 {"Programs": "", "Cat":[{"Education":Education(), "SubCat":[{"Hamara Gaon":HamaraGaon()}, {"Early Childhood Education":EarlyChildhood()}, {"Elementary":ElementaryYears()}, {"Second Chance":SecondChance()}, {"Digital Initiatives":DigitalInitiatives()}]}, {"Vocational Training":VocationalTraining(), "SubCat":[]}, {"Pratham Council For Vulnerable Children": PrathamCouncil(),"SubCat":[]}, {"Annual Status of Education Report":AnnualStatus(), "SubCat":[]}]},
 {"Resources":"", "Cat":[{"Campaigns": "", "SubCat":[{"IAmPratham":IAmPratham()}, {"Daan utsav": DaanUtsav()}, {"CAMaL Ka Camp":CAMaLKaCamp()}]}]}]

if __name__=='__main__':
    with open("Partham.txt", "w", encoding="utf-8") as f:
        f.write(("ABOUT US"+"\n\n"+AboutUs()+"\n\n"))
        f.write(("Board"+"\n\n"+Board()+"\n\n"))
        f.write(("Leadership" +"\n\n"+Leadership()+"\n\n"))
        f.write(("Teaching at the Right Level" +"\n\n"+TeachingRightLevel()+"\n\n"))
        f.write(("Recognition" +"\n\n"+Recognition()+"\n\n"))
        f.write(("\n\n"+"-"*100+"\n\n"))
        f.write(("Programs"+"\n\n"))
        f.write(("Education"+"\n\n"+Education()+"\n\n"))
        f.write(("Hamara Gaon"+"\n\n"+HamaraGaon()+"\n\n"))
        f.write(("Early Childhood Education"+"\n\n"+EarlyChildhood()+"\n\n"))
        f.write(("Elementary"+"\n\n"+ElementaryYears()+"\n\n"))
        f.write(("Second Chance"+"\n\n"+SecondChance()+"\n\n"))
        f.write(("Digital Initiatives"+"\n\n"+DigitalInitiatives()+"\n\n"))
        f.write(("Vocational Training"+"\n\n"+VocationalTraining()+"\n\n"))
        f.write(("Pratham Council For Vulnerable Children"+"\n\n"+PrathamCouncil()+"\n\n"))
        f.write(("Annual Status of Education Report"+"\n\n"+AnnualStatus()+"\n\n"))
        f.write(("\n\n"+"-"*100+"\n\n"))
        f.write(("Resources"+"\n\n"))
        f.write(("Campaigns"+"\n\n"))
        f.write(("IAmPratham"+"\n\n"+IAmPratham()+"\n\n"))
        f.write(("Daan utsav"+"\n\n"+DaanUtsav()+"\n\n"))
        f.write(("CAMaL Ka Camp"+"\n\n"+CAMaLKaCamp()+"\n\n"))
        f.close()
        print("txt file ready!!")
   
    with open('pratham.json', 'w',encoding="utf-8") as f:
        json.dump(metaData, f)
    print("json file ready!!")
