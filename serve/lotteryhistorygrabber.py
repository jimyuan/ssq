#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import requests
from html.parser import HTMLParser

# code folked from git@github.com:BEWINDOWEB/lotteryhistorygrabber.git
# ================ define const ===============
BASEPATH = "../public/"
HTMLURLS = "http://datachart.500.com/ssq/history/newinc/history.php"
HEADERS = {
    "Host": "datachart.500.com",
    "Connection": "keep-alive",
    "Accept": "*/*",
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62."
    "0.3202.94 Safari/537.36",
    "Referer": "http://datachart.500.com/ssq/history/history.shtml",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language":"zh-CN,zh;q=0.9",
    "Cookie":"ck_RegFromUrl=http%3A//www.500.com/; sdc_session=1533916356798; _jzqy=1.1528606472.1533916357.1."
    "jzqsr=baidu.-; _jzqckmp=1; seo_key=baidu%7C%7Chttps://www.baidu.com/link?url=MQcB3-er5rK249eCQNw"
    "G8A4N-hontstLi8HIy9E7H_q&wd=&eqid=fec80b7400019715000000035b6db4d7; bdshare_firstime=15339164028"
    "59; WT_FPC=id=undefined:lv=1533916553308:ss=1533916402791; _qzja=1.190448226.1533829920533.15338"
    "29920534.1533916402865.1533916409059.1533916553371.0.0.0.5.2; _qzjc=1; _jzqa=1.20620370185900751"
    "00.1533829921.1533829921.1533916357.2; _jzqc=1; Hm_lvt_4f816d475bb0b9ed640ae412d6b42cab=15338299"
    "21,1533916357; Hm_lpvt_4f816d475bb0b9ed640ae412d6b42cab=1533916554; __utma=63332592.612539621.15"
    "33916358.1533916358.1533916358.1; __utmc=63332592; __utmz=63332592.1533916358.1.1.utmcsr=baidu|u"
    "tmccn=(organic)|utmcmd=organic; CLICKSTRN_ID=123.98.36.94-1533829945.911636::415C872F9F26292A610C"
    "843E6BD7FEB2; motion_id=1533920615560_0.37147948464863223",
}
PARAMS = {
    "start": "1",
    "end": "19046"
}
DATAPATHS = "data.txt"


# ================ private parser class ===============
class Parser500ssq(HTMLParser):
    flag_tbody = False
    flag_tr = False
    flag_td = False
    linedata = []
    result = []

    def handle_starttag(self, tag, attrs):    # start tag
        if (str(tag).startswith("tbody")):
            for k,v in attrs:
                if k == 'id' and v == 'tdata':
                    self.flag_tbody = True
                    return
        elif (self.flag_tbody == True):
            if (str(tag).startswith("tr")):
                self.flag_tr = True
            if (str(tag).startswith("td")):
                self.flag_td = True

    def handle_endtag(self, tag):             # end tag
        if (self.flag_tbody == True):
            if (str(tag).startswith("tr")):
                self.result.append(self.linedata)
                self.linedata = []
                self.flag_tr = False
            elif (str(tag).startswith("td")):
                self.flag_td = False
            elif (str(tag).startswith("tbody")):
                self.flag_tbody = False

    def handle_data(self, data):              # <xx>data</xx>
        if (self.flag_td == True):
            if '\xa0' in data:
                self.linedata.append("-".join(data.replace(u'\xa0', u'').split(",")))
            else:
                self.linedata.append("".join(data.split(",")))
'''
    def handle_startendtag(self, tag, attrs): # start and end tag
        print('<%s/>' % tag)

    def handle_comment(self, data):           # <!-->comment<--!>
        print('<!--', data, '-->')

    def handle_entityref(self, name):         # special char: like &nbps
        print('&%s;' % name)

    def handle_charref(self, name):           # special string: like &#
        print('&#%s;' % name)
'''

# ================ private functions ===============
def parse500ssq(html,datapath):
    print("start grabbing...")
    parser = Parser500ssq()
    parser.feed(html)
    print(parser.result)
    with open(BASEPATH + datapath, 'w') as f:
        for line in parser.result:
            print(line)
            f.write(",".join(line))
            f.write("\n")
    print("finished.")

# ================ public functions ===============
def getHtml(url, headers={}, params={}):
    html = requests.get(url, headers=headers,  params=params)
    html.encoding = 'utf-8' #html.apparent_encoding
    return html.text

# ================ main ===============
if __name__ == "__main__":
    html = getHtml(HTMLURLS, HEADERS, PARAMS)
    parse500ssq(html, DATAPATHS)