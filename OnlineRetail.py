#%%
import pandas as pd

df = pd.read_csv("OnlineRetail.csv")
df
df.info()
# %%
df_small = df.loc[:,['Description','Quantity']]
df_small.to_csv('OnlineRetail_csv.csv')
df_csv = pd.read_csv('OnlineRetail_csv.csv')
df_csv = df_csv.drop(df_csv.columns[[0]],axis=1)
df_csv

# %%
df_small1 = df.iloc[:1000]
df_small1.to_excel('OnlineRetail_xlsx.xlsx')
df_xlsx = pd.read_excel('OnlineRetail_xlsx.xlsx')
df_xlsx = df_xlsx.drop(df_xlsx.columns[[0]],axis=1)
df_xlsx

#%%
df_small2 = df.loc[df['Quantity']>10]
df_small2.to_hdf('OnlineRetail_h5.h5','table')
df_h5 = pd.read_hdf('OnlineRetail_h5.h5','table')
df_h5 = df_h5.drop(df_h5.columns[[0]],axis=1)
df_h5

# %%
df_small3 = df[['Quantity','InvoiceDate','UnitPrice']].iloc[1000:2000]
df_small3.to_json('OnlineRetail_json.json',orient='columns')
df_json = pd.read_json('OnlineRetail_json.json')
df_json = df_json.drop(df_json.columns[[0]],axis=1)
df_json

# %%
df_small3 = df.loc[df['InvoiceNo']=='536365']
df_small3.to_html('OnlineRetail_html.html')
df_html = pd.read_html('OnlineRetail_html.html')
df_html[0] = df_html[0].drop(df_html[0].columns[[0]],axis=1)
df_html[0]
