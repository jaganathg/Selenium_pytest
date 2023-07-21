import pytest
from selenium import webdriver
from PageObjects.LoginPage import Login
from PIL import Image
from Screenshot import Screenshot


class Test_001_Login:
    baseURL = "https://admin-demo.nopcommerce.com/"
    username = "admin@yourstore.com"
    password = "admin"
    
    def test_homePageTitle(self, setup):
        ss = Screenshot.Screenshot()
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title=self.driver.title
        
        if act_title == "Your store. Login":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".//ScreenShots//"+"home_page.png")
            #img_url = ss.full_screenshot(self.driver, save_path='./ScreenShots', image_name='home_page.png')
            self.driver.close()
            assert False
            
        
    def test_login(self, setup):
        ss = Screenshot.Screenshot()
        self.driver = setup
        self.driver.get(self.baseURL)
        
        self.lp = Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)  
        self.lp.clickLogin()
        act_title= self.driver.title
           
        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
        else:
            #self.driver.save_screenshot("test_login.png")
            img_url = ss.full_screenshot(self.driver, save_path='./ScreenShots', image_name='login_page.png')
            self.driver.close()
            assert False

        """
        This test is to verify the failure of the login page title, the expecting resutl is failure
        """
    def test_login_failure(self, setup):
        ss = Screenshot.Screenshot()
        self.driver = setup
        self.driver.get(self.baseURL)
        
        self.lp = Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)  
        self.lp.clickLogin()
        act_title= self.driver.title
           
        if act_title != "Dashboard / nopCommerce administration1":
            #self.driver.save_screenshot("test_login.png")
            img_url = ss.full_screenshot(self.driver, save_path='./ScreenShots', image_name='login_page_title_error.png')
            self.driver.close()
            assert True
        else:
            self.driver.close()
            assert False
