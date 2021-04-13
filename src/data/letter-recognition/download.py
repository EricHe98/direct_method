import pandas as pd 
import os 
import pathlib 

name = 'letter-recognition'

data = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/{name}/{name}.data'.format(name=name), header=None)

data.columns = ['letter', 'x-box',
	'y-box', 'width', 'high', 'onpix', 
	'x-bar', 'y-bar', 'x2bar', 'y2bar',
	'xybar', 'x2ybr', 'xy2br', 'x-ege',
	'xegvy', 'y-ege', 'yegvx']

out_dir = 'data/{}/processed/'.format(name)
os.system('mkdir -p {}'.format(out_dir))
data.to_parquet(os.path.join(out_dir, 'data.parquet'))