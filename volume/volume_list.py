#!/usr/bin/python`
# _*_ coding: UTF-8 _*_

from lib import driver_instance



class User():

    def __init__(self):
        driver_instance.open()
        self.driver = driver_instance.driver

    def get_volume(self):
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath("//span[text() = ' 卷管理']").click()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id('dossier').click()

    def close(self):
        driver_instance.close()


user = User()
user.get_volume()
user.close()