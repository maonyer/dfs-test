#!/usr/bin/python
# _*_ coding: UTF-8 _*_

import configparser
from selenium import webdriver
import os



class Driver(object):
    def __init__(self):
        config=configparser.ConfigParser()
      #  config = ConfigParser.ConfigParser()
      #   print(os.getcwd() + "/../lib/conf.ini")
        config.read(filenames=os.getcwd() + "/../lib/conf.ini")
        # config.options("baseconf")
        self.ip_address=config.get("baseconf","ip")
       # print("ip:",self.ip_address)

        self.port=config.get("baseconf","port")
        #print 'port:',port

        self.user=config.get("baseconf","user")
        #print 'user:',user

        self.password=config.get("baseconf","password")
        #print 'password:',password

        self.share_name=config.get("share", "share_name")
        # print (self.share_name)

        self.share_volume=config.get("share", "share_volume")

        self.owner=config.get("share", "owner")

        self.share_size=config.get("share", "share_size")

        self.quota_unit=config.get("share", "quota_unit")

        self.share_type=config.get("share","share_type")

        self.share_edit_size = config.get("share_edit", "share_size")

        self.quota_edit_unit = config.get("share_edit", "quota_unit")

        self.share_edit_type = config.get("share_edit", "share_type")

        self.iscsi_name = config.get("iscsi_user", "iscsi_name")

        self.iscsi_password = config.get("iscsi_user", "iscsi_password")

        self.iscsi_confirm_pwd = config.get("iscsi_user", "iscsi_confirm_pwd")

        self.iscsi_volume = config.get("iscsi", "iscsi_volume")

        # driver.find_element_by_class_name("fa-sign-out").click()

    def close(self):
        self.driver.quit()

    def open(self):
        self.driver = webdriver.Firefox()
        # self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.url = "http://" + self.ip_address + ":" + self.port
        self.driver.get(self.url)
        self.driver.find_element_by_xpath("//input[@type='text']").send_keys(self.user)
        self.driver.find_element_by_xpath("//input[@type='password']").send_keys(self.password)

        self.driver.find_element_by_id("loginBtn").click()
