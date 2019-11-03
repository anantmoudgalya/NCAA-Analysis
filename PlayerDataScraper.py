from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:\\Users\\GV62\\Downloads\\chromedriver_win32_new\\chromedriver.exe')
driver.get("https://www.sports-reference.com/cbb/schools/colgate/2012.html")
num_rows=len(driver.find_elements_by_xpath('//*[@id="advanced_conf"]/tbody/tr'))
num_cols=len(driver.find_elements_by_xpath('//*[@id="advanced_conf"]/thead/tr/th'))
full_team_name=driver.find_element_by_xpath("//*[@id='meta']/div[2]/h1/span[2]").text.split()
school_name=full_team_name[0]
for r in range(2,25):
    heading = driver.find_element_by_xpath("//*[@id='per_game_conf']/thead/tr/th["+str(r)+"]").text
    print(heading, end =',')
for k in range(2,23):
    heading2 = driver.find_element_by_xpath("//*[@id='advanced_conf']/thead/tr/th["+str(r)+"]").text
    print(heading2, end=',')
for r in range(1,num_rows+1):
    for c in range(1,25):
        firstvalue=driver.find_element_by_xpath("//*[@id='per_game_conf']/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
        print(firstvalue, end =',')
    for k in range(1,23):
        if k > 4:
            value=driver.find_element_by_xpath("//*[@id='advanced_conf']/tbody/tr["+str(r)+"]/td["+str(k)+"]").text
            print(value,end=',')
    print(school_name,end=',')
    print()
driver.close()