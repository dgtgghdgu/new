# -*- conding:utf8 -*-
import pandas as pd
df = pd.read_csv('student.csv',sep = ',',encoding= "utf-8")

print(df)

pd.io.sql.to_sql(df,'')