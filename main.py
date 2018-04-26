from pytube import YouTube
from tqdm import *

to_dl = ''
dled = ''

with open('./to_dl.txt', 'r') as f:
	to_dl = f.read()
with open('./dled.txt', 'r') as wd:
	dled = wd.read()

to_dl = to_dl.split('\n')
dled = dled.split('\n')

for i in tqdm(to_dl):
	with open('./dled.txt', 'r') as wd:
		dled = wd.read().split('\n')
	if i in dled:
		continue
	yt = YouTube(i)
	print('starting download on', i)
	yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()
	with open('./dled.txt', 'a') as pf:
		pf.write(i+'\n')
