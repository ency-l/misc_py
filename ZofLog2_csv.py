import pandas as pd
import numpy as np
import scipy
import os

#get user input for where things are
src=input("Input path of data (csv) file (will remove leading and trailing quotation marks):")
if src[0]=="\"":
    src=src.replace("\"","")                    #remove leading and trailing "" so that the string is ready to use
output=input("path to save the output data (csv) file (Use downloads by default if left empty): ")
if output=='':
    output=os.path.expanduser("~\\Downloads")     # set default desktop directory as output path if none was given
name=input("Name of the output file (Use 'processedData' by default if left empty):")
if name=='':
    name='processedData'
    
inDF=pd.read_csv(src)                           #load input datafile to a df
outDF=pd.DataFrame()                            #initialize output datafile as a df

#################### Change this list if needed ########################

inputCols=(list(inDF.columns)                                  # Columns from the input file that will be included in the output file   
)
print(f"-----------------\nHere are the columns in file {src}:")
for i in range(0,len(inputCols)):
    print(i,inputCols[i], sep=": ")

selectedCols=input("-----------------\nPlease select the colummns you want to include in the output file by typing their index numbers, separated by a comma. \nFor example, if you want the first (0.) and third (2.) columns, type \"0,2\". :")
selectedCols_split=selectedCols.split(',')
filteredDF=pd.DataFrame([inDF.iloc[:,int(i)] for i in selectedCols_split]).transpose()
filteredDFCols=list(filteredDF.columns)
print(f"-----------------\nHere are the columns that will be included in the output file:")
for i in range(0,len(filteredDFCols)):
    print(i,filteredDFCols[i], sep=": ")
colsProcess=input(f"-----------------\nPlease select the columns you want to calculate Z(log2()) by typing their index numbers, separated by a comma:")
colsProcess_split=colsProcess.split(',')
for i in range (0,len(colsProcess_split)):
    id=colsProcess_split[i]
    colName=filteredDF.columns[int(id)]
    filteredDF[f'{colName}_log2']=np.log2(filteredDF[colName].astype('float64'))
    filteredDF[f'{colName}_Z_log2']=scipy.stats.zscore(filteredDF[f'{colName}_log2'])
    print(f'processed {colName} ({i}/{len(colsProcess_split)})')
filteredDF.to_csv(f'{output}\\{name}.csv',index=False)
print(f"Saved {name}.csv at {output}.")