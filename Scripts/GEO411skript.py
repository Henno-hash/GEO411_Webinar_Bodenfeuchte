import glob
import pandas as pd
import datetime
import io

def hainich_bf2pd(file):

    colnames = ['date', 'time', 'node', 'bat', 'V5', 'V6', 'V7', 'V8', 'EPS1', 'SM1', 'ST1', 'V12', 'V13', 'EPS2',
                'SM2', 'ST2', 'V17', 'V18', 'EPS3', 'SM3', 'ST3', 'V22', 'V23', 'EPS4', 'SM4', 'ST4', 'V27', 'V28',
                'EPS5', 'SM5', 'ST5', 'V32', 'V33', 'EPS6', 'SM6', 'ST6', 'V37', 'WPOT7', 'MPS_2_1_T7', 'V40', 'V41',
                'V42', 'WPOT8', 'MPS_2_2_T8', 'V45', 'V46', 'V47', 'WPOT9', 'MPS_2_3_T9', 'V50', 'V51']

    # read content of txt-file into panda data frame and assign column names
    # open file for reading
    f = open(file, "r")

    # read file content into the string "temp"
    temp = f.read()

    # search and replace "+" in the string "temp"
    temp = temp.replace("+", "")

    # search and replace double tabs "\t\t" in the string "temp"
    temp = temp.replace("\t\t", "")

    # import the string into a panda data frame
    df = pd.read_csv(io.StringIO(temp), sep='\t', dtype=str, header=None, names=colnames, index_col=False)

    # concatenate content of columns "date" and "time" into new column "date_time" to a list, convert to datetime format and
    # append it as 52nd column named "d_t" to data frame

    dt = (df['date'].map(str) + ' ' + df['time'].map(str)).tolist()
    d_t = [datetime.datetime.strptime((date), '%d.%m.%Y %H:%M:%S') for date in dt]
    df['d_t'] = d_t
   
    # set data format for columns containing soil moisture (SM) to float
    df.SM1 = df.SM1.astype(float)
    df.SM2 = df.SM2.astype(float)
    df.SM3 = df.SM3.astype(float)
    df.SM4 = df.SM4.astype(float)
    df.SM5 = df.SM5.astype(float)
    df.SM6 = df.SM6.astype(float)
    
    # set data format for columns containing soil temperature (ST) to float
    df.ST1 = df.ST1.astype(float)
    df.ST2 = df.ST2.astype(float)
    df.ST3 = df.ST3.astype(float)
    df.ST4 = df.ST4.astype(float)
    df.ST5 = df.ST5.astype(float)
    df.ST6 = df.ST6.astype(float)

    # return imported data frame
    return (df)

# data search path
inDir = 'E:/UNI/GEO411_Bodenfeuchte/BodenfeuchteSonden/restruct_data/RO_SE_001/2015/'

# find txt-files in data search path
files = sorted(glob.glob(inDir + '*.txt', recursive=False))

# to read content of a single text file (e.g. first file in list "files") into pandas data frame "df" do this:
###########################################################################################################
df = hainich_bf2pd(files[0])
# to read content of all text files in a folder into pandas data frame "df_all" do this:
#####################################################################################
i=0
for file in files:
    i+=1
    df=hainich_bf2pd(file)
    if (i == 1):
        all_df = df
    else:
        all_df=pd.concat([all_df, df])