
import datetime
t = (3,30,2019,9,25)

str = datetime.datetime(t[2], t[3],t[4],t[0],t[1])
print(str.strftime("%m/%d/%Y %H:%M"))