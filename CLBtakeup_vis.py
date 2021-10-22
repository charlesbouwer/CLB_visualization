# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
https://stackoverflow.com/questions/58043978/display-data-on-real-map-based-on-postal-code
https://gist.github.com/samik-saha/c8c565e5bf4d2d203c210d90573141ef
https://www12.statcan.gc.ca/census-recensement/alternative_alternatif.cfm?archived=1&l=eng&dispext=zip&teng=gfsa000b11a_e.zip&k=%20%20%20%2063981&loc=http://www12.statcan.gc.ca/census-recensement/2011/geo/bound-limit/files-fichiers/gfsa000b11a_e.zip
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