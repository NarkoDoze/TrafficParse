# -*- coding: utf-8 -*-
import requests

session = "JSESSIONID=8H1HlGx6xt1ZpYuztFaYCESWaLargjWlyI2au6zeooyH7JFw9OgowCk0vqEbReWy.UHdlYnN2ci9zZXJ2ZXIxMw=="
csvsession = session + "; _ga=GA1.3.1534967766.1499256541; _gid=GA1.3.2009760238.1499256541"

cheaders = {
    "Accept":"text/plain, */*; q=0.01",
    "Accept-Encoding":"gzip, deflate",
    "Accept-Language":"ko-KR,ko;q=0.8,en-US;q=0.6,en;q=0.4",
    "Connection":"keep-alive",
    "Content-Length":"98",
    "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
    "Cookie":csvsession,
    "Host":"hubbi.its.ulsan.kr",
    "Origin":"http://hubbi.its.ulsan.kr",
    "Referer":"http://hubbi.its.ulsan.kr/ingecep/launcher/embed_1.jsp?lang=ko_KR&mts=INGECEP&objid=84466814-713e496d&_d=ulsanhub",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
    "X-Requested-With":"XMLHttpRequest",
}
cdata = {
    "ack":"11",
    "__i":"",
    "_mts_":"",
    "option":"ls",
    "mts":"INGECEP",
    "lang":"ko_KR",
    "__g":"option;mts;lang",
    "uniquekey":"201775211339"
}
cr = requests.post("http://hubbi.its.ulsan.kr/ingecep/servlet/krcp", data=cdata, allow_redirects=True, headers=cheaders)
print(cr.content)