import pandas as pd
import io
file='E:/UNI/GEO411_Bodenfeuchte/S1Rueckstreuung/20mPixel/Rueckstreuwerte/point_per_pixel_VH_Asc.csv'
f = open(file, "r")
temp=f.read()
# search and replace "+" in the string "temp"
temp = temp.replace("# ", "")
# search and replace double tabs "\t\t" in the string "temp"
temp = temp.replace("\t\t", "")
# import the string into a panda data frame
vh_asc = pd.read_csv(io.StringIO(temp), sep=',', dtype=str)
vh_asc['date'] = pd.to_datetime(vh_asc['date'], format='%Y%m%d')
vh_asc