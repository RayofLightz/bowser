# csv_tool.py
# the csv recorder function
import csv
class Csv_tool:
    def __init__(self,c_file):
        self.csv_file = open(c_file,"w+")

    def record_csv(self,data):
        # data is a list with three items
        # uri,checksum,linecount
        writer = csv.writer(self.csv_file,dialect='excel')
        writer.writerow(data)

    def __del__(self):
        self.csv_file.close()


