# -*- coding: utf-8 -*-
"""
The how to:
https://stackoverflow.com/questions/58043978/display-data-on-real-map-based-on-postal-code
https://gist.github.com/samik-saha/c8c565e5bf4d2d203c210d90573141ef

Files you will need:
https://www12.statcan.gc.ca/census-recensement/2011/geo/bound-limit/bound-limit-2016-eng.cfm
https://open.canada.ca/data/en/dataset/ce99c2c9-c224-43eb-aef0-1f379b70c91d

"""

import geopandas
import pandas as pd
import pandas_bokeh
import matplotlib.pyplot as plt

canada = geopandas.read_file("C:/Users/Charles Bouwer/Documents/ESDC/Evaluation/lfsa000b16a_e.shp")

df =pd.read_excel("C:/Users/Charles Bouwer/Documents/ESDC/Evaluation/Cumulative_CLB_20201231v3.xlsx")

new_df=canada.join(df.set_index('FSA'), on='CFSAUID')


new_df.plot_bokeh(simplify_shapes=20000,
                  category="CLB", 
                  colormap="Spectral", 
                  hovertool_columns=["CFSAUID","CLB"])
