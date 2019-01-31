# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 16:20:16 2019

@author: RMaksyutov
"""
import pandas
from sqlalchemy import create_engine

def RetrieveCategories():
    engine = create_engine('mssql+pyodbc://mirr.db.cnetcontent.net/MDB_Mirror?driver=SQL+Server+Native+Client+11.0')
    connection = engine.connect()
    categories = pandas.read_sql_query(("""
    SELECT TOP 1000 [category_code]
          ,[lang_code]
          ,[category_name]
      FROM [MDB_Mirror].[dbo].[mdb_category_voc] WITH (NOLOCK)
    
    WHERE
    	lang_code = 'en'
    ORDER BY
    	category_name
    """), engine)
    cat_codes = categories['category_code'].values.tolist()
    cat_names = categories['category_name'].values.tolist()
    cat_cat = []
    for x in range(0, len(categories)):
        cat_cat.append(cat_codes[x]+" "+cat_names[x])
    return cat_cat, cat_codes

categories = RetrieveCategories()