# auto-mode
### OANDA APIを用いた自動FX売買ツールです。
### 10秒間隔で終値を取得し、そのデータをもとに売買を行うシステムです。  
### 10秒に一度、データを更新させ計算を行わせる。  
### ・用いた理論
短期中期長期で、近似直線の傾きを算出させ、その傾きが一致した際にアクションを起こす<br>
短期間で、急激な相場の変動があった際、跳ね返りを予測し、アクションを起こす。<br>

### ・システムフロー図


# Dependency
言語 python 3.7.4

# Setup
### 1. pipを使い、以下をインストール
pip install oandapyV20<br>
pip install pandas<br>
pip install matplotlib<br>
pip install kivy<br>

### 2. OANDA Japanのデモ講座を登録し、Acount IDとAcount tokenを取得する

### 3. .envに、Acount IDとAcount tokenを以下のように書き込む
export OANDA_ID='000-000-12345678-000'<br>
export OANDA_TOKEN='xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'<br>


# Usage
main_app.pyをターミナルから以下の様に起動させる<br>

$ python main.py<br>


# References
参考にした情報源（サイト・論文）などの情報、リンク<br>
https://developer.oanda.com/docs/jp/<br>
http://unageanu.hatenablog.com/entry/2015/05/12/104942<br>
https://nsplat.wordpress.com/2015/05/24/<br>oanda%E3%81%AE-rest-api%E3%82%92%E4%BD%BF%E3%81%A3%E3%81%A6php%E3%81%8B%E3%82%89%E5%8F%A3%E5%BA%A7%E6%83%85%E5%A0%B1%E3%81%AB%E3%82%A2%E3%82%AF%E3%82%BB%E3%82%B9/<br>