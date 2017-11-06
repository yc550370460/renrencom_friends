#!/usr/bin/python

import common
import urllib2
import urllib
import cookielib

log_data = {
    "email": common.USERNAME,
    "password": common.PASSWD
}
log_data=urllib.urlencode(log_data)
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
           'Referer': 'http://www.renren.com/'}
req = urllib2.Request(common.LOGIN_PAGE, log_data, headers)
cookie_handler = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie_handler))
resp = opener.open(req)
# page_info = resp.read()
req_friends_page = urllib2.Request(common.FRIENDS_MGT_PAGE,None,headers)
resp2 = urllib2.urlopen(req_friends_page)
page_info_friends = resp2.read()
print page_info_friends