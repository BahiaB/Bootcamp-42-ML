
import csv

class CsvReader():

    def __init__(self, filename=None, sep=';', header=False, skip_top=0, skip_bottom=0):
            #if not isinstance(filename, str) or not isinstance(sep, str) or not isinstance(header)
            self.filename = filename
            self.sep = sep
            self.headerb = header
            self.skip_top = skip_top
            self.skip_bot = skip_bottom
            self.file = None
            self.data = []
            self.header = None

    def __enter__(self):
        try:
            self.file =  open(self.filename, "r")
            csv_reader = csv.reader(self.file, delimiter=self.sep)
        except:
            return (None)
        for i, row in enumerate(csv_reader):
            for elem in row:
                if len(elem) == 0:
                    return None
            if i == 0 and self.headerb is True:
                self.header = row
            elif i >= self.skip_top and (self.skip_bot == 0 or i < self.skip_bot):
                self.data.append(row)
        return (self)


    def __exit__(self, exc_type, exc_value, exc_traceback):
        if self.file is not None:
            self.file.close()

            
    def getdata(self):
        return (self.data)

    def getheader(self):
        return (self.header)

if __name__ == "__main__":
    with CsvReader("TEST.csv",sep=';', header=True, skip_top=15) as file:
        if file is None:
            print("File not found or is corrupted")
            exit()
        print("Header:")
        print("|%s|" %file.getheader())
        print("Data:")
        for data in file.getdata():
            print("|%s|" %data)
            



            


            