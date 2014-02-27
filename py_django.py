import urllib.request

for i in range(1,15):
	url = 'http://osantana.me/pydjango/resources/video'+str(i)+'.mp4'
	print ('Baixando video - '+str(i))
	abre = urllib.request.urlopen(url).read()
	with open('Video '+str(i)+'.mp4','wb') as f:
		print ('Gravando arquivo...')
		f.write(abre)
		print ('Pronto')
		f.close()
