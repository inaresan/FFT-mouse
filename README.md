＃プログラムの概略：画像を取り込み自動でフーリエ変換を行い、黒い画面を表示する。画面上でマウスをドラッグするとフーリエ変換のその周波数における値がストックされ、マウスを離したときにマウス入力された部分を逆フーリエ変換し画像を表示する。

#使い方：パスとファイルを元画像に設定し、実行すると黒い画面が表示される。画面上をドラッグするとフーリエ変換の画像がその部分にかきこまれ、マウスを離すと明るい部分に対応する逆フーリエ変換の画像が出力される。ドラッグ線はキーボードの数字入力により対応する太さに設定できる。qキーで終了する。

#バージョン： python:3.7.3 opencv-python:4.1.0.25 numpy:1.16.2 matplotlib:3.0.3

#参考リンク
cluller『Pythonで画像処理（2次元FFTとパワースペクトル）』cBlog(最終閲覧日8/4)https://yaritakunai.hatenablog.com/entry/2016/03/20/235500
FFTの関数の用い方について参考にしました。

aster『numpyとopencvを使った画像のフーリエ変換と逆変換』Python in the box　（最終閲覧日8/4）http://www.hello-python.com/2018/02/16
同様に、FFTの関数の用い方、および逆変換について参考にしました

codegraffiti『【Python】OpenCVを使ったマウス操作での直接描画 – setMouseCallback() 』(最終閲覧日8/4)https://code-graffiti.com/opencv-direct-drawing-with-a-mouse-in-python/
マウスのイベント処理について参考にしました。
