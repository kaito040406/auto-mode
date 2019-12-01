# auto-mode
OANDA APIを用いた自動FX売買ツールです。<br>
10秒間隔で終値を取得し、そのデータをもとに売買を行うシステムです。<br>  
10秒に一度、データを更新させ計算を行わせる。<br>
土曜日と日曜日は、動かない仕様となっております。<br>
### ・用いた理論
短期中期長期で、近似直線の傾きを算出させ、その傾きが一致した際にアクションを起こす<br>
短期間で、急激な相場の変動があった際、跳ね返りを予測し、アクションを起こす。<br>

### ・システムフロー図
https://github.com/kaito040406/auto-mode/blob/master/images/flow.png


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
https://nsplat.wordpress.com/2015/05/24/