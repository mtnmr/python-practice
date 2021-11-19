#1つのファイルから画像の大きさをリサイズする
import os
from PIL import Image

dir_name = 'img'  #画像が入ってるフォルダを指定
files = os.listdir(dir_name)   #ファイル名、ディレクトリ名（フォルダ名）の一覧を取得

#ファイルは1つずつ操作する
file = files[0]
os.path.join(dir_name, file)  #パスを作成

img = Image.open(os.path.join(dir_name, file))

img.size  #サイズを確認

img_resize = img.resize((256,256))
#比率を変更したくなければ、取得した現在のサイズを使用して/2とかしたり 

#画像を新しいフォルダに保存(ファイル名は変更しない)
new_dir_name = 'resize'
img_resize.save(os.path.join(new_dir_name, file))



#複数のファイルに適用するには
dir_name = 'img'
new_dir_name = 'resize'

files = os.listdir(dir_name)

for file in files:
    img = Image.open(os.path.join(dir_name, file))
    img_resize = img.resize((256,256))

    img_resize.save(os.path.join(new_dir_name, file))





