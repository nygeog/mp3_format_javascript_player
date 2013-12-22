import os
for filename in os.listdir('.'):
	print filename
	#if filename.startswith("cheese_"):
	os.rename(filename, filename.split(' ', 1)[1])