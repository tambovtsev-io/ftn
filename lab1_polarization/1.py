import numpy as np
import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
import scipy.stats as sps
import scipy.optimize as spo
import sympy as sp
import uncertainties as uns
from uncertainties import unumpy as unp
import plotly.graph_objects as go
import plotly.io as pio
import plotly.express as px

sp.init_printing(use_latex='mathjax')
pd.options.mode.chained_assignment = None
PALETTE = px.colors.qualitative.Plotly

pio.templates["labs"] = go.layout.Template(
    layout=go.Layout(dict(
        font=dict(size=18),
        title=dict(x=0.5, xanchor="center",
                   font=dict(size=22)),
        xaxis=dict(showgrid=True),
        yaxis=dict(showgrid=True),
        legend={'traceorder':'reversed'}
    ))
)
pio.templates.default = "plotly_white+labs"

# %%
lab712 = pd.DataFrame(dict(
            a=np.arange(132, 122+360+1, 10),
            U=np.array("0 0 0.09 0.237 0.420 0.620 0.8 0.94 1.03 1.06 1.04 0.95 0.785 0.63 0.42 0.25 0.10 0.01 0 0.01 0.08 0.22 0.40 0.58 0.75 0.9 1.0 1.04 1.0 0.92 0.77 0.59 0.39 0.23 0.08 0.01".split(), dtype=np.float)
))

lab713 = pd.DataFrame(dict(
            a=np.arange(0, 370, 10),
            U=np.array("0.45 0.44 0.43 0.34 0.24 0.17 0.11 0.05 0.01 0.0 0.01 0.04 0.09 0.17 0.26 0.33 0.40 0.46 0.49 0.43 0.38 0.33 0.255 0.19 0.11 0.05 0.014 0.004 0.014 0.051 0.110 0.18 0.24 0.33 0.37 0.426 0.43".split(), dtype=np.float)
))

lab715 = pd.DataFrame(dict(
            a=np.arange(0, 360, 45),
            U=np.array("0.81 0.81 1.2 1.22 0.82 0.82 1.24 1.24".split(), dtype=np.float)
))

# %% lab 712
lab712["a1"] = lab712.a - lab712.a[0]
fig = go.Figure(data=[go.Scatter(y=lab712.U, x=lab712.a1,
                                 line=dict(color=PALETTE[0]),
                                 mode="markers",
                                 name="Эксперимент")])

ptx = np.linspace(0, 360, 10000)
fig.add_scatter(x=ptx, y=np.max(lab712.U) * np.sin(ptx*np.pi/180)**2,
                name="Теоретическая <br> зависимость",
                line=dict(color=PALETTE[1]))

fig.data = fig.data[::-1]
fig.update_layout(
    title="Результат эксперимента про закон Малюса",
    xaxis_title="Угол °",
    yaxis_title="Напряжение, мВ",
    width=800, height=500,
)
fig.update_yaxes(showgrid=True)
fig.update_xaxes(tick0=0, dtick=45, showgrid=True)
fig.write_image("pres/img/712.jpg", scale=2)
fig.show()
# %%
fig = go.Figure(data=[go.Scatter(y=lab713.U, x=lab713.a,
                                 line=dict(color=PALETTE[0]),
                                 mode="markers",
                                 name="Эксперимент")])
ptx = np.linspace(0, 360, 10000)
fig.add_scatter(x=ptx, y=np.max(lab713.U) * np.cos(ptx*np.pi/180)**2,
                name="Теоретическая <br> зависимость",
                line=dict(color=PALETTE[1]))

fig.data = fig.data[::-1]
fig.update_layout(
    title="Результат эксперимента по определению <br>"
          "поляризации лазера",
    xaxis_title="Угол °",
    yaxis_title="Напряжение, мВ",
    width=800, height=500,
)
fig.update_xaxes(tick0=0, dtick=45)
fig.write_image("pres/img/713.jpg", scale=2)
fig.show()
# %%
fig = go.Figure(data=[go.Scatter(y=lab715.U, x=lab715.a,
                                 line=dict(color=PALETTE[0]),
                                 mode="markers",
                                 name="Эксперимент")])

y1 = np.mean(lab715.loc[lab715.U < 1].U)
y2 = np.mean(lab715.loc[lab715.U > 1].U)
fig.add_scatter(x=[0, 320], y=[y1, y1],
                mode="lines",
                name="Теоретическая <br> зависимость")
fig.add_scatter(x=[0, 320], y=[y2, y2],
                line=dict(color=PALETTE[1]),
                mode="lines", showlegend=False)
fig.data = fig.data[::-1]
fig.update_layout(
    title="Результаты по пластинке λ/4",
    xaxis_title="Угол °",
    yaxis_title="Напряжение, мВ",
    width=800, height=500,
)
fig.update_xaxes(tick0=0, dtick=45)
fig.write_image("pres/img/715.jpg", scale=2)
fig.show()
