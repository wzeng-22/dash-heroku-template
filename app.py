# change this to see if it works:
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

########### Define your variables
#beers=['Chesapeake Stout', 'Snake Dog IPA', 'Imperial Porter', 'Double Dog IPA']
# reorganized gss data: extracting relevant data:

# regions: as beers above:
region = ['e.nor.central', 
    'e.sou.central',
    'middle_atlantic',
    'mountain',
    'new_england',
    'pacific',
    'south_atlantic',
    'w.nor.central',
    'w.sou.central' ]


# creating a list for opinions
#opinion=['strongly disagree', 'disagree', 'agree', 'strongly agree'] 

# create list for count values:

#reorganize the opinions
strong_disagree_values = [ 8, 5, 7, 6, 3, 11, 25, 5, 6]
disagree_values= [43, 26, 29, 29, 19, 47, 69, 15, 47 ]
agree_values = [131, 48, 64, 51, 28, 107, 145, 29, 67 ]
strong_agree_values= [74, 24, 55, 20, 38, 60, 95, 36, 58]

# values:
#ibu_values=[35, 60, 85, 75]
#abv_values=[5.4, 7.1, 9.2, 4.3]
color1='darkred'
color2='orange'
color3='navy'
color4='blue'

mytitle='Opinion Comparison by region'
tabtitle='opinion on working mothers relationship with kids'
myheading='Opinion Comparison on working mothers relationship with kids by region'
heading2='This is my first Heroku app, by WenWei Zeng, DS6001 student'

label1='strongly disagree'
label2='disagree'
label3='agree'
label4='strongly agree'

githublink='https://github.com/wzeng-22/dash-heroku-template'
sourceurl='https://github.com/jkropko/DS-6001/raw/master/localdata/gss2018.csv'

########### Set up the chart
bitterness = go.Bar(
    x=region,
    y=strong_disagree_values,
    name=label1,
    marker={'color':color1}
)
alcohol = go.Bar(
    x=region,
    y=disagree_values,
    name=label2,
    marker={'color':color2}
)

bar3 = go.Bar(
    x=region,
    y=agree_values,
    name=label3,
    marker={'color':color3}
)

bar4 = go.Bar(
    x=region,
    y=strong_agree_values,
    name=label4,
    marker={'color':color4}
)

gss_data = [bitterness, alcohol, bar3, bar4]
gss_layout = go.Layout(
    barmode='group',
    title = mytitle
)

gss_fig = go.Figure(data=gss_data, layout=gss_layout)


########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title=tabtitle

########### Set up the layout
app.layout = html.Div(children=[
    html.H1(myheading),
    html.H5(heading2),
    dcc.Graph(
        id='flyingdog',
        figure=gss_fig
    ),
    html.A('Code on Github', href=githublink),
    html.Br(),
    html.A('Data Source', href=sourceurl),
    ]
                     
)

if __name__ == '__main__':
    app.run_server()

