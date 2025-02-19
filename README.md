# 네이버에 로그인 버튼 이미지를 찾아서
# 클릭!!
import pyautogui
import time
# 특정 이미지가 화면에 있는지 검색
time.sleep(3)
button = pyautogui.locateOnScreen("button.png")
print(button)
