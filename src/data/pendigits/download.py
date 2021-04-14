import pandas as pd 
import os 
import pathlib 

name = 'pendigits'

train = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/{name}/{name}.tra'.format(name=name), header=None)
test = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/{name}/{name}.tes'.format(name=name), header=None)

data = pd.concat([train, test], axis=0)

data.columns = ['sequence', 'mcg',
	'gvh', 'alm', 'mit', 'erl', 'pox', 'vac', 'nuc']

out_dir = 'data/{}/processed/'.format(name)
os.system('mkdir -p {}'.format(out_dir))
data.to_parquet(os.path.join(out_dir, 'data.parquet'))