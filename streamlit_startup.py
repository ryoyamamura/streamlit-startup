###streamlitでWebアプリを作る方法を勉強
###参考URL：https://www.youtube.com/watch?v=zp-kAt1Ih5k

###streamlit helloでデモ画面を表示

###streamlit docs（右側のメニューからアクセス可能）にチュートリアルがある
###参考URL：https://docs.streamlit.io

import streamlit as st
#import numpy as np
#import pandas as pd
#from PIL import Image
import time

###タイトルを表示
st.title('streamlit超入門')

###文字を入力
#st.write('DataFrame')

#df = pd.DataFrame({
#    '1列目':[1, 2, 3, 4],
#    '2列目':[10, 20, 30, 40]
#                  })

###dataframe関数でデータフレームを表示
###write関数ではできない表のサイズ調整等が可能
#st.dataframe(df, width=200, height=200)

###stile.highlight_maxメソッドで最大値をハイライト
#st.dataframe(df.style.highlight_max(axis=0), width=200, height=200)

###スタティックな表（ソートなどができない↔動的なものはdataframe）を作るときはtable関数を利用
#st.table(df)

###streamlitチュートリアルの display data で様々なデータの表示方法を学べる

###マークダウン記法でテキストを入力する
"""
# 章
## 節
### 項

```python
import streamlit as st
import numpy as np
import pandas as pd
```
"""

###(20行×3列）の乱数のデータ表を作成
#df1 = pd.DataFrame(
#    np.random.rand(20,3),
#    columns=["a", "b", "c"]
#    )

###グラフを作成＆可視化
#st.area_chart(df1)

####streamlitチュートリアルの display chart で様々なグラフの表示方法を学べる

###(100行×2列）の乱数のデータ表を作成
###新宿付近は緯度35.69度、経度139.70
###35.69、139.70を中心とした乱数表に変換　乱数の大きさも50で割って小さくする
#df2 = pd.DataFrame(
#    np.random.rand(100,2)/[50,50] + [35.69, 139.70],
#    columns=["lat", "lon"]
#    )

###マップを表示
#st.map(df2)

###画像を読み込む
img = Image.open('IMG_0262.JPG')

###画像を表示
###use_column_widthはページ幅に合わせるか否か
#st.image(img, caption="山村亮")

###streamlitチュートリアルの display image で様々なデータ（音楽、ビデオ）の表示方法を学べる

###インタラクティブなウィジェットを学ぶ

###チェックボックス True/Falseを返す
#if st.checkbox('Show Image'):
#    st.image(img, caption="山村亮", use_column_width=True)

###セレクトボックス
#option = st.selectbox(
#        'あなたの好きな数字を教えてください',
#        list(range(1,11)) #1~10の数字のリストを作成
#        )

#'あなたの好きな数字は、', option, 'です'

###テキスト入力フォーム
#text = st.text_input('あなたの趣味を教えてください。')
#st.write('あなたの趣味は、', text, 'です')

###スライダー
#condition = st.slider('あなたの今の調子は？', 0, 10, 1)
#st.write('あなたの今の調子は、', condition, 'です')

###streamlitチュートリアルの Display interactive widgets で様々なウィジェットの表示方法を学べる


###レイアウトを整える

###サイドバー sidebarをメソッドの間に挟み込むだけ！
#text = st.sidebar.text_input('あなたの趣味を教えてください。')
#st.write('あなたの趣味は、', text, 'です')

###ツーカラムレイアウトにする
#left_column, right_column = st.columns(2)
#button = left_column.button("右カラムに文字を表示")
#if button:
#    right_column.write("ここは右カラムです")

###エクスパンダー　Q&Aを作るイメージ
#expander = st.expander('問い合わせ')
#expander.write("問い合わせ内容を書く")


###プログレスバー
"start!!"
latest_iteraction = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteraction.text(f"Iteration {i+1}")
    bar.progress(i+1)
    time.sleep(0.05)
    
"Done!!!"


