#元々ついているファイル名に先頭に規則性のある連番をつけてファイル名を変更、これを一括で実施
#日付＿タイトルに変更してみる

import os
import datetime

path = '.'  #.でカレントディレクトリを指定
files = os.listdir(path)  #隠しファイルも全て表示される、必要なファイルだけ取り出したい

files_dir = []  #必要なdirのみを取り出して格納する場所

for file in files:
    #隠しファイルは基本'.'で始まっているから、隠しファイルじゃないものをTrue/Flaseで判定
    #file.startwith('.') 

    #ディレクトリ以外のものを除くため、dirかどうかTrue/Flasede判定
    #os.path.isdir(os.path.join(path, file)  

    if not file.startswith('.') and os.path.isdir(os.path.join(path, file)):
        files_dir.append(file)

#使用するフォルダを1つずつ見てみる
dir_name = files_dir[0]
#この中から1つファイルを取り出してやってみる
file = os.listdir(os.path.join(path, dir_name))[1]

file_name = file.split('.')[0]   #今のファイル名から、拡張子を抜いた部分を取り出す
ext = file.split('.')[1]  #拡張子は別の変数に保存しておく

os.path.join(path, dir_name, file)  #ファイルのパス名

#日付を取得
create_time = os.stat(os.path.join(path, dir_name, file)).st_birthtime #タイムスタンプの形
date = datetime.datetime.fromtimestamp(create_time) #日付の形に変換
date = date.strftime('%Y%M%D')  #年月日だけを20211018みたいな形で表示してくれる

#新しいファイル名を作成
new_file = '{}_{}.{}'.format(date, file_name, ext)

#ファイル名を作成した新しいファイル名に変更する
#旧ファイル名(パス名)
os.path.join(path, dir_name, file) 
#新ファイル名(パス名)
os.path.join(path, dir_name, new_file) 

os.rename(os.path.join(path, dir_name, file) , os.path.join(path, dir_name, new_file) )


#全て一括で変更するためにまとめると
path = '.'
files = os.listdir(path) 

files_dir = []
for file in files:
    if not file.startswith('.') and os.path.isdir(os.path.join(path, file)):
        files_dir.append(file)

for dir_name in files_dir:
    files = os.listdir(os.path.join(path, dir_name))
    for file in files:
        file_name = file.split('.')[0]
        ext = file.split('.')[1] 

        create_time = os.stat(os.path.join(path, dir_name, file)).st_birthtime 
        date = datetime.datetime.fromtimestamp(create_time) 
        date = date.strftime('%Y%M%D') 

        new_file = '{}_{}.{}'.format(date, file_name, ext)
        os.rename(os.path.join(path, dir_name, file), os.path.join(path, dir_name, new_file))




