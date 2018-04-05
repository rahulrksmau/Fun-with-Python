import csv
import pandas as pd
from collections import OrderedDict

class Filter:
	def __init__(self, infilename, outfilename):
		self.infile = infilename
		self.outfile= outfilename
	
	def convDict(self):
		self.dic = OrderedDict()
		fl = pd.read_csv(self.infile)
		for index,key in fl.iterrows():
				line = key.tolist()[1:]
				key = key['Invoice No']
				if self.dic.has_key(key):
					self.dic[key].append(line)
				else:
					self.dic[key] = []
					self.dic[key].append(line)

	def appendVal(self):
		with open(self.outfile, 'wb') as fl:
			rowWriter = csv.writer(fl,delimiter = ',')
			for key in self.dic.keys():
				row = [key]
				for item in self.dic[key]:
					for col in item:
						row.append(col)
				rowWriter.writerow(row)


def main():
	filename = raw_input('File Name\n')
	opfilename = raw_input('Output File Name\n')
	f = Filter(filename, opfilename)
	f.convDict()
	print ("Writting new CSV.....")
	f.appendVal()
	print ("new CSV named %s done."%f.outfile)

if __name__ == "__main__":
	main()

