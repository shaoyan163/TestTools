from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException,TimeoutException
import traceback
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
try:
    driver.get('https://passport.qschou.com/sdk/passport/login.html?passport_scene=wa_zzck_1&'
               'redirect_url=https%3A%2F%2Fm2.qschou.com%2Ffund%2FpaySuccess%3Fcc%3D20002.v9.payC%'
               '26huzhu%3D0%26platform%3Dhome%26projuuid%3Df882dc4c-125d-4de3-9f9f-8823de88a11f%26recommendindex%3D1%26order_no%3D202004100003447070370158_o_00')
    driver.find_element_by_class_name('ls-input-phone').clear()
    driver.find_element_by_class_name('ls-input-phone').send_keys('18600232284')
    driver.find_element_by_xpath("//input[@type='text' and @placeholder='填写手机验证码']").clear()
    driver.find_element_by_xpath("//input[@type='text' and @placeholder='填写手机验证码']").send_keys("1111")
    driver.find_element_by_class_name('ls-btn-normal').click()
    time.sleep(1)
    driver.find_element_by_xpath("//span[contains(text(),'依恋')]").click()
    driver.find_element_by_xpath("//button[@onclick='selUserSubmit()']").click()
except (NoSuchElementException,TimeoutException) as e:
    traceback.print_exc()