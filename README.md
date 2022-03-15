## 運用爬蟲實現背景網頁自動點擊
### 動機 : 
2021年8月7日，一款網頁遊戲突然受到台灣人的關注。

遊戲以網路迷因「Popcat」為題材，進入網站後只要觸發鍵盤或滑鼠任何一個按鍵都能使點擊次數+1，網頁會用ip偵測玩家所在的地區，將點擊次數以國家為單位統計。

因其簡單的遊戲特性和競爭性質，造成此遊戲在台灣掀起一陣旋風，各路大神都在提供快速點擊的方法，而我也投入其中。
![](https://i.imgur.com/L3fpK7k.png)


### 最初想法

在當時接觸到這款遊戲時，就在想有什麼方法能夠讓他自動點擊，不用耗費人力，可以放著讓它自己跑。為此我下載了一款自動點擊器，他能模擬真實滑鼠點擊，可以開啟後掛在網頁讓他自己點。

### 發現不便

使用一段時間後，我發現了一個問題，那個程式的運作原理是模擬真實滑鼠點擊，所以我電腦畫面要留在那個頁面，不能同時做其他事，這個不便使我萌生了自己寫一個程式讓他能在背景跑的念頭。

### 撰寫新程式

要寫程式，首先要考慮的是用什麼語言。

既然是要跑網頁，我首先想到的是python的爬蟲，雖然對python不甚熟悉，但高一社團課時由稍微接觸過，了解可以用xpath抓到想要的元素，再用指令去點擊，點擊頻率則用sleep控制。

### 程式碼
```python=
from selenium import webdriver
from time import sleep

chromeDriverPath = r"chromedriver.exe"
site = webdriver.ChromeOptions()
# site

browser = webdriver.Chrome(executable_path=chromeDriverPath) 

url = 'https://popcat.click' #給網址
browser.get(url) #抓網址
browser.maximize_window() #視窗最大化
sleep(2)#怕有人網頁還沒跑好，所以睡個兩秒

#用無限迴圈執行點擊作業
while 1:
    browser.find_element_by_xpath('//*[@id="app"]/img').click() #我是抓標題POPCAT的xpath來點
    browser.find_element_by_xpath('//*[@id="app"]/img').click()
    sleep(0.03) #睡覺
```

> [name=YuYu][time=Tue, December 7, 2021 1:52 PM]

### 測試

完成程式後，接著就是測試環節，我用了自己的電腦進行測試，程式能夠順利執行。
因此，我將程式的demo影片上傳到Youtube。
並在說明欄附上程式下載連結。

<iframe width="560" height="315" src="https://www.youtube.com/embed/lHarZ_vUgmI" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### 成效
這部影片獲得了5000多觀看, 46個讚和38則留言
![](https://i.imgur.com/LoawKl8.png)


新版和舊版的程式下載次數共1萬多次
![](https://i.imgur.com/G8Zyoj4.png)

在Github上也獲得了一顆星星(很少但我很開心 :D)
![](https://i.imgur.com/rYPMBZ5.png)

### 心得
其實我也有將程式上傳到論壇，但時間久那篇文就被刪掉了，在哪裡有人和我建議能用代理ip來跑，其實那時的我是第一次聽到代理ip，研究了好久，但最終不知是ip的問題，還是我程式的問題，總是無法順利請求伺服器。
最終，代理ip的程式只好作罷，但自己也還是學到了不少。
![](https://i.imgur.com/kuRQfVR.png)
![](https://i.imgur.com/CcDylw3.png)
![](https://i.imgur.com/cbWQa6K.png)
