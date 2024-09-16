import pandas as pd
import sqlite3

df = pd.read_excel('C:/Users/hrith/Desktop/Portfolio_Projects/Depression/Workbook.xlsx', sheet_name = 'depression_data_work')
conn = sqlite3.connect('Depression.db')
df.to_sql('Raw',conn,if_exists='replace',index=False)
conn.close()
