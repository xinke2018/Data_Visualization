# plotly standard imports
import plotly.graph_objs as go
import plotly.plotly as py

# Data science imports
import pandas as pd
import numpy as np

# Options for pandas
pd.options.display.max_columns = 30

# Display all cell outputs
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = 'all'

# Using plotly + cufflinks in offline mode
import cufflinks
cufflinks.go_offline(connected=True)
init_notebook_mode(connected=True)

# setup credential
plotly.tools.set_credentials_file(username, api_key)

from plotly.offline import iplot
cufflinks.go_offline()

# Set global theme
cufflinks.set_config_file(world_readable=True, theme='pearl')

df = pd.read_csv('computer_security.csv')
df.head()


# ATTN: need to use as_index=False, otherwise l_ipn will be index
data = df.groupby(['l_ipn','date'], as_index=False).mean() 
data.head()

data.columns = ['ID', 'DATE', 'ASN', 'avg_f']
data.head()

data = df.groupby(['l_ipn','date'], as_index=False).sum()
data.columns = ['ID', 'DATE', 'ASN', 'total_f']

tds_1 = data[data['ID'] == 1].set_index('DATE')

tds_1['total_f'].iplot(
    mode='lines+markers',
    opacity=0.8,
    size=8,
    symbol=1,
    xTitle='Date',
    yTitle='total count of connection',
    title='Anomaly Detection - ID:1')

tds_2 = data[data['ID'] == 5].set_index('DATE')

tds_2['total_f'].iplot(
    mode='lines+markers',
    opacity=0.8,
    size=8,
    symbol=1,
    xTitle='Date',
    yTitle='total count of connection',
    title='Anomaly Detection - ID:5')

tds_3 = data[data['ID'] == 3].set_index('DATE')

tds_3['total_f'].iplot(
    mode='lines+markers',
    opacity=0.8,
    size=8,
    symbol=1,
    xTitle='Date',
    yTitle='total count of connection',
    title='Anomaly Detection - ID:3')

tds_4 = data[data['ID'] == 6].set_index('DATE')

tds_4['total_f'].iplot(
    mode='lines+markers',
    opacity=0.8,
    size=8,
    symbol=1,
    xTitle='Date',
    yTitle='total count of connection',
    title='Anomaly Detection - ID:6')

tds_5 = data[data['ID'] == 4].set_index('DATE')

tds_5['total_f'].iplot(
    mode='lines+markers',
    opacity=0.8,
    size=8,
    symbol=1,
    xTitle='Date',
    yTitle='total count of connection',
    title='Anomaly Detection - ID:4')


















