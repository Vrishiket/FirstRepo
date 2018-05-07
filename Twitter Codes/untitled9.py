import scipy

import math as mt

import pickle as pkl
import os
import psycopg2
import matplotlib
import matplotlib.pyplot as plt
from numpy.random import normal
import calendar
from scipy.optimize import curve_fit
  matplotlib inline
plt.rcParams['figure.figsize'] = (16,8)
import warnings
warnings.filterwarnings('ignore')

#import plotly
import plotly.plotly as py
import plotly.graph_objs as go
import plotly.figure_factory as ff
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
init_notebook_mode(connected=True)