import requests
import re

ss_main_pattern = '(<a href="(\S+)" (style="font-weight:bold")?>(.+)<\/a>\n<\/td>\n<\/tr>\n<tr>\n<TD valign="top" align="center" class="normal">\n(<img src="http://source.ncix.com/bnr/webonlydeal/webonlydeal_btn.gif" border="0" align="texttop" width="75" height="16" />\n)?<B>Price:&nbsp;&nbsp;<\/B>\n<B><FONT color="#\S{6}" size="2">\n\$(\d{1,5}\.\d{2})\n)'
re.compile(ss_main_pattern, re.MULTILINE)

scrape_url = 'http://www.ncix.com/promo/Black-Friday-Sale-2014.htm'

response = requests.get(scrape_url)

# surprise specials
Objs = re.findall(ss_main_pattern, response.text)

# separate objects into items
for i in range(0, len(Objs)):

    Objs[i].__str__().replace('\\n', '')
    Objs[i].__str__().replace('\n', '')
    Objs[i] = re.sub('<a href="', ' ', Objs[i].__str__())
    Objs[i] = re.sub('" style="font-weight:bold">', ' ', Objs[i].__str__())
    Objs[i] = re.sub('(<\w>|</\w>|<\w\w>|</\w\w>)', ' ', Objs[i].__str__())
    Objs[i] = re.sub('<FONT color="#\S{6}" size="2">', ' ', Objs[i].__str__())
    Objs[i] = re.sub('<TD valign="top" align="center" class="normal">', ' ', Objs[i].__str__())
    Objs[i] = re.sub('Price:&nbsp;&nbsp;', ' ', Objs[i].__str__())

    print(Objs[i]+'\n')



print('Number of items on surprise special: ' + str(len(Objs)))