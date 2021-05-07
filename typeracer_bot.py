from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://play.typeracer.com")
sleep(1)
enter_race = driver.find_element_by_xpath('//*[@id="gwt-uid-1"]/a')
enter_race.click()

sleep(0.5)

text = driver.find_element_by_xpath(
    '//*[@id="gwt-uid-20"]/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[1]/td/div/div').text

print(text)

text_area = driver.find_element_by_xpath(
    '//*[@id="gwt-uid-20"]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/input')
if text_area:
    print("input found")

while True:
    print('trying to type')
    try:
        print('typing...')
        for i in range(len(text)):
            text_area.send_keys(text[i])
            sleep(0.01)
        break
    except:
        sleep(0)

exit()
