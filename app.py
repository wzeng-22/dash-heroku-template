# extra credit assignment for hw 12: DS 6001:
# responding to challenges # 1 and 3:

import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff
import dash
from jupyter_dash import JupyterDash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# reading in data frame and cleaning it:

#%%capture
gss = pd.read_csv("https://github.com/jkropko/DS-6001/raw/master/localdata/gss2018.csv",
                 encoding='cp1252', na_values=['IAP','IAP,DK,NA,uncodeable', 'NOT SURE',
                                               'DK', 'IAP, DK, NA, uncodeable', '.a', "CAN'T CHOOSE"])



mycols = ['id', 'wtss', 'sex', 'educ', 'region', 'age', 'coninc',
          'prestg10', 'mapres10', 'papres10', 'sei10', 'satjob',
          'fechld', 'fefam', 'fepol', 'fepresch', 'meovrwrk'] 
gss_clean = gss[mycols]
gss_clean = gss_clean.rename({'wtss':'weight', 
                              'educ':'education', 
                              'coninc':'income', 
                              'prestg10':'job_prestige',
                              'mapres10':'mother_job_prestige', 
                              'papres10':'father_job_prestige', 
                              'sei10':'socioeconomic_index', 
                              'fechld':'relationship', 
                              'fefam':'male_breadwinner', 
                              'fehire':'hire_women', 
                              'fejobaff':'preference_hire_women', 
                              'fepol':'men_bettersuited', 
                              'fepresch':'child_suffer',
                              'meovrwrk':'men_overwork'},axis=1)
gss_clean.age = gss_clean.age.replace({'89 or older':'89'})
gss_clean.age = gss_clean.age.astype('float')


markdown_text='''
This is my work for extra credit homework 12, answering challenges # 1 and 3:


'''


# answering challenge 1 and 3:
# extra credit figure: group the relationship variable by region:
gss_plot = gss_clean.groupby(['region', 'relationship']).size().reset_index()
gss_plot = gss_plot.rename({0:'count'}, axis=1)
gss_plot



# creating figure: facet bar graph: for extra credit question 1:




# second figure for extra credit:
# analyzing the socioeconomic index by gender:
fig_e2 = px.histogram(gss_clean, x='socioeconomic_index', nbins=60, marginal='box', color ='sex',
                   labels={'socioeconomic_index':'score of socioeconomic index'},
                   title = 'Distribution of score of socioeconomic index by gender')
fig_e2.update(layout=dict(title=dict(x=0.5)))
fig_e2.show()


app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


app.layout = html.Div(
    [
        #this is displaying to the dashboard to Heroku       
        
        
        
        html.H2("Distributions of score of socioeconomic index by gender"),
        
        dcc.Graph(figure=fig_e2),
        
    
    
    ]
)

if __name__ == '__main__':
    app.run_server( debug=True, port=8052)


