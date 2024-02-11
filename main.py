from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

options = Options()
# options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

driver.implicitly_wait(3.5)

def S1toS2(driver):
    driver.switch_to.default_content()
    frame_element = driver.find_element(By.ID, "fraDisabled")
    driver.switch_to.frame(frame_element)
    driver.find_element(By.XPATH, "//button[text()='Simulator 2']").click()
    sleep(0.5)



def HA_Simulator(driver):
    frame_element = driver.find_element(By.XPATH, "//iframe[@src='half_adder.html']")
    driver.switch_to.frame(frame_element)
    aBtn = driver.find_element(By.XPATH, "//img[@id='A']")
    bBtn = driver.find_element(By.XPATH, "//img[@id='B']")
    addBtn = driver.find_element(By.XPATH, "(//input[@id='button' and @value='ADD'])")
    Supply = driver.find_element(By.ID, "Supply")
    Supply.click()
    driver.execute_script("arguments[0].scrollIntoView(true);", Supply)
    for a in range(0,2):
        for b in range(0,2):
            if "switchon.png" in aBtn.get_attribute("src"):
                aBtn.click()
            if "switchon.png" in bBtn.get_attribute("src"):
                bBtn.click()
            sleep(0.5)
            if a:
                aBtn.click()
            if b:
                bBtn.click()
            sleep(0.5)
            addBtn.click()
    sleep(1)
    driver.save_screenshot("HA_Sim_1.png")
    sleep(1)

    S1toS2(driver)

    frame_element = driver.find_element(By.XPATH, "//div[@id='sim2']//iframe")
    driver.switch_to.frame(frame_element)

    myinputA = driver.find_element(By.NAME, "myinputA")
    myinputB = driver.find_element(By.NAME, "myinputB")
    myinputZ = driver.find_element(By.NAME, "myinputZ")
    myinputC = driver.find_element(By.NAME, "myinputC")
    check = driver.find_element(By.XPATH, "//input[@value='Check']")
    scroll = driver.find_element(By.XPATH, "//img[@src='HA.png']")
    driver.execute_script("arguments[0].scrollIntoView(true);", scroll)
    for a in range(0,2):
        for b in range(0,2):
            myinputA.clear()
            myinputB.clear()
            myinputZ.clear()
            myinputC.clear()
            sleep(0.5)
            myinputA.send_keys(str(a))
            myinputB.send_keys(str(b))
            if a ^ b:
                myinputZ.send_keys("1")
            else:
                myinputZ.send_keys("0")
            if a & b:
                myinputC.send_keys("1")
            else:
                myinputC.send_keys("0")
            sleep(0.5)
            check.click()
    sleep(1)
    driver.save_screenshot("HA_Sim_2.png")
    sleep(1)



def FA_Simulator(driver):
    frame_element = driver.find_element(By.XPATH, "//iframe[@src='full_adder.html']")
    driver.switch_to.frame(frame_element)
    aBtn = driver.find_element(By.XPATH, "//img[@id='A']")
    bBtn = driver.find_element(By.XPATH, "//img[@id='B']")
    cBtn = driver.find_element(By.XPATH, "//img[@id='C']")
    addBtn = driver.find_element(By.XPATH, "(//input[@id='button' and @value='ADD'])")
    driver.find_element(By.ID, "Supply").click()
    sleep(0.5)
    driver.execute_script("arguments[0].scrollIntoView(true);", aBtn)
    for a in range(0,2):
        for b in range(0,2):
            for c in range(0,2):
                if "switchon.png" in aBtn.get_attribute("src"):
                    aBtn.click()
                if "switchon.png" in bBtn.get_attribute("src"):
                    bBtn.click()
                if "switchon.png" in cBtn.get_attribute("src"):
                    cBtn.click()
                sleep(0.5)
                if a:
                    aBtn.click()
                if b:
                    bBtn.click()
                if c:
                    cBtn.click()
                sleep(0.5)
                addBtn.click()
    sleep(1)
    driver.save_screenshot("FA_Sim_1.png")
    sleep(1)

    S1toS2(driver)

    frame_element = driver.find_element(By.XPATH, "//div[@id='sim2']//iframe")
    driver.switch_to.frame(frame_element)


    myinputA = driver.find_element(By.NAME, "myinputA")
    myinputB = driver.find_element(By.NAME, "myinputB")
    myinputCin = driver.find_element(By.ID, "Cin")
    myinputS = driver.find_element(By.XPATH, "(//*[@name='myinputZ'])[1]")
    myinputCout = driver.find_element(By.XPATH, "(//*[@name='myinputZ'])[2]")
    check = driver.find_element(By.XPATH, "//input[@value='Check']")

    scroll = driver.find_element(By.XPATH, "//img[@src='FA.png']")
    driver.execute_script("arguments[0].scrollIntoView(true);", scroll)

    for a in range(0,2):
        for b in range(0,2):
            for c in range(0,2):
                myinputA.clear()
                myinputB.clear()
                myinputCin.clear()
                myinputS.clear()
                myinputCout.clear()
                sleep(0.5)
                myinputA.send_keys(str(a))
                myinputB.send_keys(str(b))
                myinputCin.send_keys(str(c))
                if a ^ b ^ c:
                    myinputS.send_keys("1")
                else:
                    myinputS.send_keys("0")
                if (a & b) | (b & c) | (c & a):
                    myinputCout.send_keys("1")
                else:
                    myinputCout.send_keys("0")
                sleep(0.5)
                check.click()
    sleep(1)
    driver.save_screenshot("FA_Sim_2.png")
    sleep(1)




driver.get("https://de-iitr.vlabs.ac.in/exp/half-full-adder/index.html")
driver.maximize_window()
print("Proccessing......")
sleep(0.5)

aim = driver.find_element(By.ID, "to-verify-the-truth-table-of-half-adder-and-full-adder-by-using-xor-and-nand-gates-respectively-and-analyse-the-working-of-half-adder-and-full-adder-circuit-with-the-help-of-leds-in-simulator-1-and-verify-the-truth-table-only-of-half-adder-and-full-adder-in-simulator-2")
aim_txt = aim.text
with open("practical.txt", 'w') as file:
        file.write("AIM :- ")
        file.write(aim_txt)
        file.write("\n\n")

driver.find_element(By.XPATH, "(//a[@href='theory.html'])[2]").click()
theory = driver.find_element(By.XPATH, "//div[contains(@class, 'vlabs-page-content') and contains(@class, 'px-5') and contains(@class, 'pb-4') and contains(@class, 'flex-grow-1') and contains(@class, 'markdown-body')]")
theory_txt = theory.text
theory_imgs = driver.find_elements(By.XPATH, "//div[contains(@class, 'vlabs-page-content') and contains(@class, 'px-5') and contains(@class, 'pb-4') and contains(@class, 'flex-grow-1') and contains(@class, 'markdown-body')]//img")
with open("practical.txt", 'a') as file:
        file.write("\n\n")
        file.write("THEORY :- \n")
        file.write(theory_txt)
        file.write("\n\n")
sleep(0.5)
with open("practical.txt", 'a+') as file:
        file.write("IMG LINKS :- \n")
        for img in theory_imgs:
            img_src = img.get_attribute("src")
            file.write(f"{img_src}\n")

driver.find_element(By.XPATH, "(//a[@href='procedure.html'])[2]").click()
procedure = driver.find_element(By.XPATH, "//div[@class='vlabs-page-content px-5 pb-4 flex-grow-1 markdown-body']")
procedure_txt = procedure.text

try:
    with open("practical.txt", 'a+') as file:
        file.write("\nPROCEDURE :- \n")
        file.write(procedure_txt)
except Exception as e:
    print("An error occurred while writing to the file:", e)

sleep(2)

# Simulation
driver.find_element(By.XPATH, "(//a[@href='simulation.html'])[2]").click()
frame_element = driver.find_element(By.ID, "fraDisabled")
driver.switch_to.frame(frame_element)

try:
    HA_Sim = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "(//a[@href='Simulator.html'])")))
    HA_Sim.click()
    HA_Simulator(driver)
except Exception as e:
    print("Error:", e)


driver.back()

driver.switch_to.frame(frame_element)
try:
    FA_Sim = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "(//a[@href='Simulator1.html'])")))
    FA_Sim.click()
    FA_Simulator(driver)
except Exception as e:
    print("Error:", e)

print("DONE✅")
driver.quit()
