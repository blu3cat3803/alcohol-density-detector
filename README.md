# alcohol-density-detector
1. 硬體配備： 
   公對公杜邦線 x n條 
   mq3酒精感測器 x 5個 
   麵包版 x 5個 
   linkit 開發版 x 1個 
   樹梅派R3 x 1個 
   
2. 配線：
   將酒精感測器以並聯方式連接，電源3.3V，感測器的AO接腳依序接到linkit的A0, A1, A2, A3, A4,linkit透過microUSB接到樹梅派上，樹梅派再由另一條microUSB接回電腦建立資料庫。 
   
3. 軟體：
   使用Django將資料庫migration後建立資料庫，並建立後端從資料庫取回資料，再利用chart.js建立圖表。
   
4. 運行: 
   啟用採集資料程式: sensor.py 
   啟用伺服器: 在Case目錄下執行指令 python manage.py runserver 192.168.43.150:8000 
 
   //樹梅派IP：192.168.43.150 
   //樹梅派root密碼 ：107061223
