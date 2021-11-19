#datebaseの続き

import sqlite3
import pandas as pd

df = pd.read_csv('パス名')
df.head()  #最初５行で読み込みデータの確認

db_name = 'sample_db'
conn = sqlite3.connect(db_name)

df.to_sql('table_name', conn, if_exists='replace')

c = conn.cursor()
query = 'select * from table_name'  #全てのデータを取得
query = 'select count(*) from table_name'  #全ての行数を取得

c.execute(query) #実行
c.fetchone()

#データを追加してみる
query_create = '''
insert into table_name (class, Alchol)   
values(1, 15.0)
'''
c.execute(query_create) #実行、行の後ろにデータが追加された

#追加されたデータを確認する
query_select = '''
select * from table_name
limit　5  #最大で何行取得できるか
offset 175   #175行目から取得、今回は179行目に追加されているかを確認したい
'''

for row in c.execute(query_select):
    print(row)

#一部の列だけ取得
query = 'select ラベル名 from table_name'

query = '''
select ラベル名 from table_name
where rabel_name >= 14.0
'''

#更新
#今回はtable内のrabel2のデータが14以上のものに関してrabel1のデータを全て２に変更する
query = '''
update table_name set rabel_name1 = 2
where rabel_name2 >= 14.0
''' 

c.execute(query)

#削除
#まず行数確認してみる,そのあとdelete実行すると行数が減ってるのがわかる
query = 'select count(*) from table_name'
c.execute()

query_delete = '''
delete from table_name
where rabel_name = 1
'''