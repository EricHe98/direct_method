import pandas as pd 
import os 
import pathlib 

name = 'yeast'

data = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/{name}/{name}.data'.format(name=name), header=None)

data.columns = ['sequence', 'mcg',
	'gvh', 'alm', 'mit', 'erl', 'pox', 'vac', 'nuc']

out_dir = 'data/{}/processed/'.format(name)
os.system('mkdir -p {}'.format(out_dir))
data.to_parquet(os.path.join(out_dir, 'data.parquet'))