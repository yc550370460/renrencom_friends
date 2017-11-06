#!/usr/bin/python
#coding:utf-8

import common
import urllib2
import urllib
import cookielib
import json
import threading

class Request_renren(object):
    def __init__(self, path, username, password):
        self.path = path
        self.username = username
        self.password = password
        self.friends_list = []
        self.year = []
        self.month = []
        self.lock = threading.Lock()
        self.cookie  = cookielib.CookieJar()
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cookie))
        urllib2.install_opener(self.opener)

    def login(self):
        data = {'email': self.username,
                'password': self.password}
        req = urllib2.Request(self.path, urllib.urlencode(data))
        try:
            resp = self.opener.open(req)
            resp_friend_list = urllib2.urlopen(common.FRIENDS_LIST)
            friend_str = resp_friend_list.read()
            friend_str = friend_str.strip().split("=")[2]
            friend_str = friend_str.rstrip(';')
            friend_list = (friend_str.split('"friends":')[1].split('"specialfriends":')[0]).strip().strip(",")
            # friend_list = re.findall('"friends":.*}]', friend_str)
            friend_list = eval(friend_list)
            for item in friend_list:
                self.friends_list.append(item["fid"])
            print self.friends_list
        except Exception, e:
            print e.message

    def visit_friend_homepage(self):
        while self.friends_list:
            self.lock.acquire()
            try:
                url = r"http://www.renren.com/" + str(self.friends_list[0]) + r"/profile"
                print url
                resp = urllib2.urlopen(url)
                res = resp.read()
                result = (res.split('tlNavData =')[1].split(";")[0]).strip().strip("'")
                print result
                if result:
                    result = eval(result)[0]
                    self.year.append(result["year"])
                    self.month.append(result["month"][0])
                self.friends_list.pop(0)
                print self.year
                print self.month

            except Exception, e:
                print e.message
            finally:
                self.lock.release()

    def run_threading(self):
        t1 = threading.Thread(target = self.visit_friend_homepage)
        t2 = threading.Thread(target = self.visit_friend_homepage)
        t1.start()
        t2.start()



instance = Request_renren(common.LOGIN_PAGE, common.USERNAME, common.PASSWD)
instance.login()
instance.run_threading()




