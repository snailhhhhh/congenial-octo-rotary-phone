import cv2,pyautogui,time
while True:
    pyautogui.screenshot(region=(1926,754,2560-1926,1600-754)).save('screenshot.png')
    template = cv2.imread('1.png')
    screenshot = cv2.imread('screenshot.png')
    match = cv2.matchTemplate(screenshot, template, cv2.TM_SQDIFF_NORMED)
    if cv2.minMaxLoc(match)[0] < 0.1:
        pyautogui.click(button='right')
        time.sleep(0.5)
        pyautogui.click(button='right')
        time.sleep(2)
        #print("收杆成功", time.asctime())
    #else:print("识别失败", time.asctime())
time.sleep(0.4)
