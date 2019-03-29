from lib import driver_instance
import time
from selenium.webdriver.common.keys import Keys


class Share():

    def __init__(self):
        driver_instance.open()
        self.driver = driver_instance.driver

    def get_share(self):    #打开NAS共享列表
        # self.driver.implicitly_wait(10)
        time.sleep(3)
        self.driver.find_element_by_xpath("//span[text()=' 共享管理']").click()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id('share').click()
        # self.driver.find_element_by_id('iscsi').click()
        time.sleep(5)

    def add_share(self):    #新建NAS共享
        self.driver.find_element_by_id('share_add').click()

        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath("//div[@id = 'share_add_name']/input").send_keys(driver_instance.share_name)      #共享名
        # print (driver_instance.share_name)
        time.sleep(2)

        self.driver.find_element_by_xpath("//div[@id = 'share_add_volume']/input").click()      #选择共享卷
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath("//span[text() = '%s']"%driver_instance.share_volume).click()
        time.sleep(2)

        self.driver.find_element_by_xpath("//div[@id = 'share_add_user']/input").click()        #选择共享所属用户
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath("//span[text() = '%s']"%driver_instance.owner).click()
        time.sleep(2)

        self.driver.find_element_by_xpath("//div[@id = 'share_add_quota']/input").send_keys(driver_instance.share_size)     #设置共享配额大小

        self.driver.find_element_by_xpath("//div[@id = 'share_add_quota_unit']/input").click()      #设置共享配额单位
        self.driver.find_element_by_xpath("//span[text() = '%s']"%driver_instance.quota_unit).click()

        nfs = self.driver.find_element_by_xpath("//input[@value = 'NFS']")      #设置共享类型
        if 'NFS' in driver_instance.share_type:
            nfs.send_keys(Keys.SPACE)
        time.sleep(1)

        cifs = self.driver.find_element_by_xpath("//input[@value = 'CIFS']")
        if 'CIFS' not in driver_instance.share_type:
            cifs.send_keys(Keys.SPACE)
        time.sleep(1)

        ftp = self.driver.find_element_by_xpath("//input[@value = 'FTP']")
        if 'FTP' in driver_instance.share_type:
            ftp.send_keys(Keys.SPACE)
        time.sleep(1)

        self.driver.find_element_by_id('share_add_submit').click()     #提交
        # self.driver.find_element_by_id('share_add_cancel').click()     #取消

    def share_permission(self):     #打开共享授权信息
        self.driver.find_element_by_id('share_permission_details_1').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/div[2]/section/div/div[4]/div/div[1]/button/i').send_keys(Keys.ESCAPE)
        time.sleep(2)

    def share_file(self):     #打开共享文件管理
        self.driver.find_element_by_id('share_file_management_1').click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//a[contains(text(),'新文件夹')]").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//a[contains(text(),'新文件夹')]").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//span[text()='返回共享']").click()
        time.sleep(2)

    def share_permission_management(self):    #单文件授权管理
        self.driver.find_element_by_id('share_autorization_management_1').click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//span[text()='返回共享']").click()

    def share_edit(self):     #共享设置
        self.driver.find_element_by_id('share_edit_1').click()

        self.driver.find_element_by_xpath("//div[@id = 'share_edit_quota']/input").send_keys(Keys.CONTROL,'a')      #修改共享配额大小
        self.driver.find_element_by_xpath("//div[@id = 'share_edit_quota']/input").send_keys(Keys.BACK_SPACE)
        self.driver.find_element_by_xpath("//div[@id = 'share_edit_quota']/input").send_keys(driver_instance.share_edit_size)

        self.driver.find_element_by_xpath("//div[@id = 'share_edit_quota_unit']/input").click()     #修改共享配额单位
        self.driver.find_element_by_xpath("//span[text()='%s']"%driver_instance.quota_edit_unit).click()

        nfs_edit = self.driver.find_element_by_xpath("//input[@value = 'NFS']")
        cifs_edit = self.driver.find_element_by_xpath("//input[@value = 'CIFS']")
        ftp_edit = self.driver.find_element_by_xpath("//input[@value = 'FTP']")
        for type in (nfs_edit,cifs_edit,ftp_edit):      #勾选所有共享类型
            if type.is_selected():
                continue
            else:
                type.send_keys(Keys.SPACE)

        if 'CIFS' not in driver_instance.share_edit_type:       #修改共享类型
            cifs_edit.send_keys(Keys.SPACE)
        time.sleep(1)

        if 'NFS' not in driver_instance.share_edit_type:
            nfs_edit.send_keys(Keys.SPACE)
        time.sleep(1)

        if 'FTP' not in driver_instance.share_edit_type:
            ftp_edit.send_keys(Keys.SPACE)
        time.sleep(1)

        self.driver.find_element_by_id('share_edit_submit').click()     #提交
        # self.driver.find_element_by_id('share_edit_cancel').click()     #取消
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath("//div[@class='el-message-box__btns']/button[2]").click()     #确定
        # self.driver.find_element_by_xpath("//div[@class='el-message-box__btns']/button[1]").click()     #取消

    def delete_share(self):       #删除共享
        self.driver.find_element_by_id('share_delete_1').click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//button[@class ='el-button el-button--default el-button--primary ']").click()

    def iscsi_user(self):       #iscsi验证
        self.driver.find_element_by_xpath("//div[text()='iSCSI 验证']").click()
        time.sleep(2)

    def iscsi_add_user(self):       #创建iscsi验证用户
        # self.driver.implicitly_wait(10)
        self.driver.find_element_by_id('iscsi_add').click()
        self.driver.find_element_by_xpath("//div[@id='iscsi_add_user']/input").send_keys(driver_instance.iscsi_name)
        self.driver.find_element_by_xpath("//div[@id='iscsi_add_pwd']/input").send_keys(driver_instance.iscsi_password)
        self.driver.find_element_by_xpath("//div[@id='iscsi_add_confirm_pwd']/input").send_keys(driver_instance.iscsi_confirm_pwd)
        time.sleep(1)
        self.driver.find_element_by_id('iscsi_add_submit').click()
        # self.driver.find_element_by_id('iscsi_add_cancel').click()

    def iscsi_delete_user(self):        #删除iscsi用户
        # self.driver.implicitly_wait(10)
        self.driver.find_element_by_id('iscsi_delete_1').click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//div[@class='el-message-box__btns']/button[2]").click()  # 确定
        # self.driver.find_element_by_xpath("//div[@class='el-message-box__btns']/button[1]").click()  # 取消

    def iscsi_detail(self):     #iscsi详情页
        self.driver.find_element_by_xpath("//div[text()='iSCSI 详情']").click()
        time.sleep(2)

    def iscsi_add(self):        #创建iscsi
        self.driver.find_element_by_xpath("//div[@id='iscsi_select_volume']/input").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//span[text()='%s']"%driver_instance.iscsi_volume).click()
        time.sleep(1)

        self.driver.find_element_by_id('iscsi_add_target').click()      #创建Target

        self.driver.find_element_by_xpath("//span[@id='21']//i[@id='iscsi_add_lun']").click()   #在第一个Target下创建Lun

        self.driver.find_element_by_xpath("//span[@id='21']//i[@id='iscsi_not_access']").click()      #客户端接入设置
        # self.driver.find_element_by_xpath("//div[@class'el-message-box__btns']/button[1]")  #不允许接入
        self.driver.find_element_by_xpath("//div[@class'el-message-box__btns']/button[2]")  # 允许接入

        # self.driver.find_element_by_id('iscsi_modify_bind_user').click()

    def iscsi_delete_lun(self):
        self.driver.find_element_by_id('iscsi_delete').click()
        self.driver.find_element_by_xpath("//div[@class='el-message-box__btns']/button[2]").click()  # 确定
        # self.driver.find_element_by_xpath("//div[@class='el-message-box__btns']/button[1]").click()  # 取消

    def iscsi_delete_target(self):
        self.driver.find_element_by_xpath("//span[@id='21']//i[@id='iscsi_delete']").click()
        self.driver.find_element_by_xpath("//div[@class='el-message-box__btns']/button[2]").click()  # 确定
        # self.driver.find_element_by_xpath("//div[@class='el-message-box__btns']/button[1]").click()  # 取消

    def close(self):
        driver_instance.close()


share = Share()
share.get_share()
# share.add_share()
# share.share_permission()
# share.share_file()
# share.share_permission_management()
# share.share_edit()
# share.delete_share()
# share.iscsi_user()
# share.iscsi_add_user()
# share.iscsi_delete_user()
# share.iscsi_detail()
# share.iscsi_add()
# share.iscsi_delete_lun()
# share.iscsi_delete_target()
# share.close()
