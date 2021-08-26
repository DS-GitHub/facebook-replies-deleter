import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
driver = webdriver.Firefox()
#LOGINING
driver.get("https://www.facebook.com")
username = driver.find_element_by_id("email")
password = driver.find_element_by_id("pass")
submit   = driver.find_element_by_name("login")
email = input("Facebook 이메일을 입력하세요(사용자PC 메모리 이외에 절대로 저장되지 않습니다.): ")
pw = input("Facebook 비밀번호를 입력하세요(사용자PC 메모리 이외에 절대로 저장되지 않습니다.): ")
username.send_keys(email)
password.send_keys(pw)
submit.click()
wait = WebDriverWait(driver, 6)
driver.get("https://www.facebook.com/(USER ID. I DIDN'T MAKE FUNCTION THAT FETCHES USER ID. EDIT THIS AND USE)/allactivity?activity_history=false&category_key=COMMENTSCLUSTER&manage_mode=false")
time.sleep(4)
asdf = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div[2]/div[4]/div[3]/div")
asdf.click()
time.sleep(3)
asdf = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div[2]/div[3]/div[4]/div")
asdf.click()
time.sleep(5)
counting = 0
final = False
while True:
    #SCROLLING
    SCROLL_PAUSE_TIME = 4.5
    last_height = driver.execute_script("return document.body.scrollHeight")
    print(f"#{counting} 스크롤링을 시작합니다.")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(SCROLL_PAUSE_TIME)
        new_height = driver.execute_script("return document.body.scrollHeight")
        items = driver.find_elements_by_xpath("//*[@class='l9j0dhe7 btwxx1t3 j83agx80']")
        if len(items) >= 200:
            print(f"#{counting} 스크롤링이 완료되었습니다.")
            break
        if new_height == last_height:
            print(f"#{counting} 마지막 스크롤링이 완료되었습니다.")
            final = True
            break
        last_height = new_height
    #DELETING
    countnumbers = 0
    print(f"#{counting} 댓글 삭제 단계를 시작합니다.")
    time.sleep(7)
    checkbox = driver.find_element_by_name("comet_activity_log_select_all_checkbox")
    checkbox.click()
    time.sleep(3)
    numbers = int(driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/span").text)
    countnumbers += numbers
    print(f"#{counting} {numbers}개의 댓글 삭제가 시작되었습니다.")
    deletebutton = driver.find_element_by_css_selector("div[aria-label='삭제']")
    deletebutton.click()
    time.sleep(0.01)
    deletebutton = driver.find_elements_by_css_selector("div[aria-label='삭제']")
    deletebutton = deletebutton[1]
    deletebutton.click()
    time.sleep(25)
    print(f"#{counting} {numbers}개의 댓글 삭제가 완료되었습니다.")
    if final == True:
        print(f"#{counting} 모든 삭제가 완료되었습니다. 총 {countnumbers}개의 댓글이 삭제되었습니다.")
        break
    counting += 1