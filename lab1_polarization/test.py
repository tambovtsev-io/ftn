import plotly.graph_objects as go
import plotly.io as pio
import plotly.express as px
import chart_studio
import chart_studio.plotly as py
import plotly.graph_objects as go
import sys; sys.path.insert(1, r"C:\Users\rurur\Desktop\p\python\plotly")
from credentials import USERNAME, API_KEY

chart_studio.tools.set_credentials_file(username=USERNAME, api_key=API_KEY)
pio.templates["labs"] = go.layout.Template(
    layout=go.Layout(dict(
        font=dict(size=18),
        title=dict(x=0.5, xanchor="center",
                   font=dict(size=22)),
        xaxis=dict(showgrid=True),
        yaxis=dict(showgrid=True)
    ))
)

pio.templates.default = "plotly_white+labs"

fig = px.scatter(x=[1, 5], y=[1, 5])

fig.update_layout(
    title="TITLE",
    xaxis_title="x-axis",
    yaxis_title="y-axis"
)
# py.plot(data, filename='test', auto_open=True)
py.plot(fig, filename='test', auto_open=True)
# %%