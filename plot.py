from dotenv import load_dotenv
load_dotenv()

import os
import pandas as pd
import geopandas as gpd
import psycopg2
import sqlalchemy as db
import matplotlib.pyplot as plt
import descartes
import platform
import mapclassify as mc
import json
import seaborn as sns
import numpy as np
import io
from datetime import datetime

from sqlalchemy import create_engine
postgres_str = os.environ['DATABASE_URL']

cnx = create_engine(postgres_str)
conditions = pd.read_sql_query('SELECT * FROM conditions', cnx)

conditions = conditions[['name', 'state']]
conditions_map_data = conditions.rename(index=int, columns={'name':'CONDITION', 'state':'STATE_ABBR'})

states= gpd.read_file('./data/states.shp')
states_formatted = states[['STATE_ABBR', 'geometry']]
# Remove Hawaii and Alaska
usa = states_formatted[~states_formatted.STATE_ABBR.isin(['HI', 'AK'])]

merged = usa.set_index('STATE_ABBR').join(conditions_map_data.set_index('STATE_ABBR'))

grpd = merged.groupby(['STATE_ABBR','CONDITION']).size().to_frame('NUM').reset_index()

def fetch_map_data(condition):
    user_condition = grpd[grpd.CONDITION == f'{condition}']
    joined = usa.set_index('STATE_ABBR').join(user_condition.set_index('STATE_ABBR')).reset_index()
    values = {'CONDITION': 'no record', 'NUM': 0}
    rtp = joined.fillna(value = values)
    return rtp

def render_map(condition):
    map_data = fetch_map_data(condition)
    ax = map_data.dropna().plot(column=map_data.NUM, cmap =
                                 'Blues',
                                 figsize=(15,9),
                                 scheme='natural_breaks', k=6,
                                 legend=True,
                                 edgecolor='black',
                                 linewidth=0.8,
                                 legend_kwds=dict(title="Number of MeMD Users\n", frameon=False));
    ax.axis('off')
    ax.set_title(f'MeMD {condition.capitalize()} Diagnosis Across the US', fontdict={'fontsize': '35', 'fontweight' : '5'})
    ax.get_legend().set_bbox_to_anchor((.22,.29))
    current_time = datetime.now()
    date = current_time.strftime('%m-%d-%Y')
    ax.annotate(f'This map is a representation of {condition} diagnosis across the US among MeMD users only. Last Updated: {date}', xy=(0.52, .15),  xycoords='figure fraction', horizontalalignment='center', verticalalignment='top', fontsize=12, color='#555555')
    ax.get_figure()
    return ax
