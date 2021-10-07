#import urllib.request
from pandas.core.frame import DataFrame
#urllib.request.http.client
from pandas.io.parsers import read_csv
import streamlit
import pandas
import random
streamlit.title('COVID-19 dashboard for India')
#streamlit.sidebar.title('Visualization selector')

dataframe=pandas.read_csv('https://api.covid19india.org/csv/latest/state_wise.csv')

total_dataframe=dataframe[dataframe['State']=='Total']
main_dataframe=dataframe[dataframe['State']!='Total']
streamlit.text('')

l=['Confirmed','Recovered','Deaths','Active']

colors=['Cyan','DarkOrchid','Indigo','SeaGreen']#'Chocolate','Crimson','ForestGreen','SpringGreen'

row1=streamlit.beta_columns(4)
for i in range(4):
    row1[i].markdown(f'<h1 style="color:{colors[i]};font-size:24px;"><u>{l[i]}</u></h1>', unsafe_allow_html=True)
row2=streamlit.beta_columns(4)
for i in range(4):
    row2[i].markdown(f'<p style="color:{colors[i]};font-size:24px;">{int(total_dataframe[l[i]])}</p>', unsafe_allow_html=True)

#visualisation=streamlit.sidebar.selectbox('Select a chart type',('Bar Graph','Pie Chart','Line Graph'))
#select_state=streamlit.sidebar.selectbox('Select a state',main_dataframe['State'].unique())
#select_status=streamlit.sidebar.radio('Covid-19 cases status',('Confirmed Cases','Recovered Cases','Deaths Cases','Active Cases'))
streamlit.header("State-wise data")

row3=streamlit.beta_columns(5)
row3[0].markdown(f'<h1 style="color:ForestGreen;font-size:24px;"><u>State</u></h1>', unsafe_allow_html=True)
row3[1].markdown(f'<h1 style="color:ForestGreen;font-size:24px;"><u>Confirmed</u></h1>', unsafe_allow_html=True)
row3[2].markdown(f'<h1 style="color:ForestGreen;font-size:24px;"><u>Recovered</u></h1>', unsafe_allow_html=True)
row3[3].markdown(f'<h1 style="color:ForestGreen;font-size:24px;"><u>Deaths</u></h1>', unsafe_allow_html=True)
row3[4].markdown(f'<h1 style="color:ForestGreen;font-size:24px;"><u>Active</u></h1>', unsafe_allow_html=True)
#streamlit.write(main_dataframe)
l=list(main_dataframe['State'].unique())

for x in l:
   if x=="State Unassigned":
       continue
   row=streamlit.beta_columns(5)
   temp_dataframe=main_dataframe[main_dataframe["State"]==x]
   state,confirmed,recovered,deaths,active=x,int(temp_dataframe["Confirmed"]),int(temp_dataframe["Recovered"]),int(temp_dataframe["Deaths"]),int(temp_dataframe["Active"])
   row[0].write(f'<h6 style="color:Crimson;">{state}</h6>', unsafe_allow_html=True)
   row[1].write(f'<h6 style="color:Crimson;">{confirmed}</h6>', unsafe_allow_html=True)
   row[2].write(f'<h6 style="color:Crimson;">{recovered}</h6>', unsafe_allow_html=True)
   row[3].write(f'<h6 style="color:Crimson;">{deaths}</h6>', unsafe_allow_html=True)
   row[4].write(f'<h6 style="color:Crimson;">{active}</h6>', unsafe_allow_html=True)

