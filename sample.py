import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

nickname = input()
driver = webdriver.Chrome()
url = "https://maplestory.nexon.com/N23Ranking/World/Total"
driver.get(url)

search = driver.find_elements(
    "css selector",
    "#container > div > div > div.rank_nav > div > span.word_input.ranking_search_bar_input > input[type=text]",
)[0]

search.click()
search.send_keys(nickname)


search_btn = driver.find_elements(
    "css selector",
    "#container > div > div > div.rank_nav > div > span.word_input.ranking_search_bar_input > span",
)[0]
search_btn.click()

driver.implicitly_wait(2)

character = driver.find_elements(
    "css selector",
    "#container > div > div > div:nth-child(4) > div.rank_table_wrap > table > tbody > tr.search_com_chk > td.left > dl > dt > a",
)[0]

character.click()

driver.implicitly_wait(2)
driver.switch_to.window(driver.window_handles[-1])

driver.implicitly_wait(2)
equipment = driver.find_element(
    "css selector",
    "#container > div.con_wrap > div.lnb_wrap > ul > li:nth-child(3) > a",
)
equipment.click()
char = {}
driver.implicitly_wait(2)
private = driver.find_elements(
    "css selector", "#container > div.con_wrap > div.contents_wrap > div > div.private2"
)
if len(private) > 0:
    print("비공개 상태입니다.")
else:
    for i in range(1, 31):
        tap = driver.find_element(
            "css selector",
            "#container > div.con_wrap > div.contents_wrap > div > div.tab01_con_wrap > div.weapon_wrap > ul > li:nth-child("
            + str(i)
            + ")",
        )
        driver.implicitly_wait(2)

        tap.click()
        title = driver.find_element(
            "css selector",
            "#container > div.con_wrap > div.contents_wrap > div > div.tab01_con_wrap > div.item_info > div > div.item_title > div.item_memo > div.item_memo_title > h1",
        ).get_attribute("innerText")
        info = driver.find_element(
            "css selector",
            "#container > div.con_wrap > div.contents_wrap > div > div.tab01_con_wrap > div.item_info > div > div.stet_info > ul",
        ).get_attribute("innerHTML")
        char[title] = str(info).strip()
# json 파일로 저장

with open("./test.json", "w", encoding="utf-8") as make_file:
    json.dump(char, make_file, indent="\t")
