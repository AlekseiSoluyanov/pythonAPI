import time
import yaml

with open("testdata.yaml") as f:
    testdata = yaml.safe_load(f)


def test_step1(site, log_xpath, pass_xpath, btn_xpath, result_xpath):
    input1 = site.find_element("xpath", log_xpath)
    input1.send_keys("test")
    input2 = site.find_element("xpath", pass_xpath)
    input2.send_keys("test")
    btn = site.find_element("xpath", btn_xpath)
    btn.click()
    err_lable = site.find_element("xpath", result_xpath)
    assert err_lable.text == "401"


def test_step2(site, log_xpath, pass_xpath, btn_xpath, result_login):
    input1 = site.find_element("xpath", log_xpath)
    input1.send_keys(testdata["name"])
    input2 = site.find_element("xpath", pass_xpath)
    input2.send_keys(testdata["passwd"])
    btn = site.find_element("xpath", btn_xpath)
    btn.click()
    login = site.find_element("xpath", result_login)
    assert login.text == "Blog"


def test_step3(site, log_xpath, pass_xpath, btn_xpath, btn_create_post,
               btn_save_post, tittle_post_xpath, description_post_xpath,
               content_post_xpath, tittle_save_post):
    input1 = site.find_element("xpath", log_xpath)
    input1.send_keys(testdata["name"])
    input2 = site.find_element("xpath", pass_xpath)
    input2.send_keys(testdata["passwd"])
    btn = site.find_element("xpath", btn_xpath)
    btn.click()
    time.sleep(testdata["sleep_time"])
    btn_create = site.find_element("xpath", btn_create_post)
    btn_create.click()
    time.sleep(testdata["sleep_time"])
    input1 = site.find_element("xpath", tittle_post_xpath)
    input1.send_keys('Grand Theft Auto VI')
    input2 = site.find_element("xpath", description_post_xpath)
    input2.send_keys('Релиз игры запланирован на 2025')
    input2 = site.find_element("xpath", content_post_xpath)
    input2.send_keys('предстоящая компьютерная игра в жанре action-adventure с открытым миром, '
                     'разрабатываемая компанией Rockstar Games.')
    btn_post = site.find_element("xpath", btn_save_post)
    btn_post.click()
    time.sleep(testdata["sleep_time"])
    result = site.find_element("xpath", tittle_save_post)
    assert result.text == "Grand Theft Auto VI"
