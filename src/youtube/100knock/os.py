#カレントディレクトリ内の全てのファイル情報の取得
import os
for curDir, dirs, files in os.walk('.'):
    for file in files:
        print(f'{curDir}/{file}')

#カレントディレクトリ内のファイル情報の取得
lists = os.listdir('.')

#絶対パスを含んだファイル名の取得
os.path.abspath('パス名')  #walkで取得したパス名は相対パス、これを絶対パスで取得する

#ファイル名のみ取得
os.path.basename('パス名')

#ファイル、ディレクトリの存在確認
os.path.exists('xyz/')  #xyzファイルが存在するか、True.Falseで返す

#ディレクトリの存在確認、exists以外
os.path.isdir('パス名')

#ファイルの存在確認、exists以外
os.path.isfile('パス名')

#パス名の結合
for curDir, dirs, files in os.walk('.'):
    for file in files:
        print(os.path.join(curDir, file))  #最初はf文で結合してたけど


#カレントディレクトリにディレクトリを作成
os.mkdir('mei')

#ファイルの削除
os.remove('sample.txt')  #カレントディレクトリ内にある時はそのままファイル名を書く

#ディレクトリ名の変更
os.rename('mei', 'kawai')  #ディレクトリ名がmeiからkawaiに変わる

#環境変数の確認
os.environ['PATH']

#Unixコマンド
os.system('ls　-a') #pythonスクリプト（.pyファイル）とかならこれで呼び出せる、ターミナル上でやればok
