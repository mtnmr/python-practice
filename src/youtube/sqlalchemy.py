#SQLAlchemyでデータベース（CSVファイル）を操作する
#!pip3 install sqlalchemy

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

import pandas as pd
import os

from sqlalchemy.sql.visitors import cloned_traverse

#カレントディレクトリにファイルを作成
datebase_file = os.path.join(os.path.abspath(os.getcwd()), 'date.db') 

#エンジンをセットする
engine = create_engine('sqlite:///' + datebase_file, convert_unicode=True, echo=True)

#sessionを作成,さっき作ったエンジンを紐付ける
db_session = scoped_session(
    sessionmaker(
        autocommit=False,
        autoflush=False,
        bind = engine
    )
)

#元にするデータベースを作成する
Base = declarative_base()
Base.query = db_session.query_property()  #このコードは細かく気にしない


#CSVファイルからデータを読み込んでデータベースに入れる
from sqlalchemy import Column, Integer, Float

class Wine(Base):
    __tabelename__ = 'wine_class'
    id = Column(Integer, primary_key=True)
    wine_class = Column(Integer, unique=False)
    alcohol = Column(Float, unique=False)
    ash = Column(Float, unique=False)
    hue = Column(Float, unique=False)
    proline = Column(Integer, unique=False)

    def __init__(self, wine_class=None, alcohol=None, ash=None, hue=None, proline=None):
        self.wine_class = wine_class
        self.alcohol = alcohol
        self.ash = ash
        self.hue = hue
        self.proline = proline

#クラスを元にデータベースを作成
Base.metadate.create_all(bind = engine)

#作成したデータベース内に実際のデータを入れる
def read_date():
    wine_df =  pd.read_csv('wine_class.csv')

    for index, _df in wine_df.iterrows():
        row = Wine(wine_class=_df['Class'], alcohol=_df['Alcohol'], ash=_df['Ash'], hue=_df['Hue'], proline=_df['Proline'])
        db_session.add(row)
    db_session.commit()

#入れたデータを元にCRUD操作
#read
db = db_session.query(Wine).all()
for row in db:
    print(row.alcohol)

#特定のカラムのみ抽出する時はクエリの中に指定
db = db_session.query(Wine.hue, Wine.proline).all()
for row in db:
    print(row.hue)

#条件抽出
db = db_session.query(Wine).filter(Wine.hue > 1.0)

#データ数制限
db = db_session.query(Wine).limit(20).all()

#並べ替え
from sqlalchemy import desc
db = db_session.query(Wine).order_by(desc(Wine.hue)).limit(20).all()

#create
wine = Wine(wine_class=1, alcohol=1, ash=1, hue=1, proline=1) #新しいデータを作ってみた
db_session.add(wine)
db_session.commit()

db = db_session.query(Wine).filter(Wine.proline==1).all() #ちゃんと入ってるか条件絞って確認してみる
for row in db:
    print(row.id, row.wine_class, row.alcohol, row.ash, row.hue, row.proline)

#update
db = db_session.query(Wine).filter(Wine.proline==1).first()  #変更するデータを1つとってくる
db.wine_class = 10
db_session.commit()

#delete
db = db_session.query(Wine).filter(wine.proline==1).delete()




