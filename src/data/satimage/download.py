import pandas as pd 
import os 
import pathlib 

name = 'satimage'

train = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/statlog/{name}/sat.trn'.format(name=name), 
	sep=" ",
	header=None)
test = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/statlog/{name}/sat.tst'.format(name=name), 
	sep=" ", 
	header=None)

data = pd.concat([train, test], axis=0)

data.columns = ['sequence', 'mcg',
	'gvh', 'alm', 'mit', 'erl', 'pox', 'vac', 'nuc']

out_dir = 'data/{}/processed/'.format(name)
os.system('mkdir -p {}'.format(out_dir))
data.to_parquet(os.path.join(out_dir, 'data.parquet'))