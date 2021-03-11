#%%
from selenium import webdriver
import os
import urllib.request
import argparse

def main(searchterm):
    driver = webdriver.Edge(executable_path='edgedriver_win64/msedgedriver.exe')
    url = "https://www.google.com/search?q="+searchterm+"&source=lnms&tbm=isch"
    driver.get(url)
    
    img_folder_path = 'imgs/'   #이미지 저장 폴더
    
    class_path = os.path.join(img_folder_path,searchterm)
    
    if not os.path.isdir(img_folder_path):      #없으면 새로 생성
        os.mkdir(img_folder_path)

    if not os.path.isdir(class_path):      #없으면 새로 생성
        os.mkdir(class_path)

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    for i in range(500):
        try:
            driver.find_elements_by_css_selector(".rg_i")[i].click()
            url = driver.find_element_by_css_selector(".n3VNCb").get_attribute("src")
            urllib.request.urlretrieve(url, class_path + "/"+str(i) +".jpg")

        except:
            driver.execute_script("return document.body.scrollHeight")
    driver.close()

parser =  argparse.ArgumentParser()
parser.add_argument('-w', type=str, 
                    help='enter search_keyword')
args = parser.parse_args()
main(args.w)
