# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 15:10:10 2020

@author: Phung Vo
"""



import pandas as pd
import numpy as np
from pathlib import Path
import os 
import wget
#import os
import glob
#from operator import itemgetter


#Step 0: Clean Directory

#Specify data folder to download file
cwd = os.getcwd()
cwd = str(Path(cwd).parents[0]) + "\\data\\"
cwd

fileList = glob.glob(cwd + "*", recursive=True)
fileList

 
# Iterate over the list of filepaths & remove each file.
for cwd in fileList:
    try:
        os.remove(cwd)
    except:
        print("Error while deleting file : ", cwd)
                


#Specify data folder to download file
cwd = os.getcwd()
cwd = str(Path(cwd).parents[0]) + "\\reference\\"
cwd

fileList = glob.glob(cwd + "*", recursive=True)
fileList

 
# Iterate over the list of filepaths & remove each file.
for cwd in fileList:
    try:
        os.remove(cwd)
    except:
        print("Error while deleting file : ", cwd)
                



#Step 1: Download data file from Census

#Specify data folder to download file

cwd = os.getcwd()
cwd = str(Path(cwd).parents[0]) + "\\data\\"
cwd

print('Beginning file download Census 2018 SF 5 Year...')

#url = 'https://www2.census.gov/programs-surveys/acs/summary_file/2018/data/5_year_by_state/Massachusetts_Tracts_Block_Groups_Only.zip'
url = 'https://www2.census.gov/programs-surveys/acs/summary_file/2018/data/5_year_entire_sf/All_Geographies_Not_Tracts_Block_Groups.zip'
wget.download(url, cwd + 'downloadfile.zip')

#Step 2: Extract File

from zipfile import ZipFile
zippedfile = cwd + 'downloadfile.zip'
zippedfile

# Create a ZipFile Object and load sample.zip in it
with ZipFile(zippedfile, 'r') as zipObj:
   # Extract all the contents of zip file in different directory
   zipObj.extractall(cwd)
   

fileList = glob.glob(cwd + '*.zip', recursive=True)
fileList
 
# Iterate over the list of filepaths & remove each file.
for cwd in fileList:
    try:
        os.remove(cwd)
    except:
        print("Error while deleting file : ", cwd)       
           

cwd = os.getcwd()
cwd = str(Path(cwd).parents[0]) + "\\reference\\"
cwd

print('Beginning file download Summary File SEQ data...')

url = 'https://www2.census.gov/programs-surveys/acs/summary_file/2018/data/2018_5yr_Summary_FileTemplates.zip'
wget.download(url, cwd + 'referencefile.zip')




print('Beginning file download : 5 Year Geography file...')

url = 'https://www2.census.gov/programs-surveys/acs/summary_file/2018/documentation/geography/5_year_Mini_Geo.xlsx'
wget.download(url, cwd + 'geofile.xlsx')








#Step 2: Extract File

from zipfile import ZipFile
zippedfile = cwd + 'referencefile.zip'
zippedfile

# Create a ZipFile Object and load sample.zip in it
with ZipFile(zippedfile, 'r') as zipObj:
   # Extract all the contents of zip file in different directory
   zipObj.extractall(cwd)   


fileList = glob.glob(cwd + '*.zip', recursive=True)
fileList
 
# Iterate over the list of filepaths & remove each file.
for cwd in fileList:
    try:
        os.remove(cwd)
        print("Deleted file :", fileList)
    except:
        print("Error while deleting file : ", cwd)       
        
   
#Step 3: Delete unneed Files





cwd = os.getcwd()
cwd = str(Path(cwd).parents[0]) + "\\data\\"
cwd



fileList = glob.glob(cwd + 'm20*.txt', recursive=True)
fileList
 
# Iterate over the list of filepaths & remove each file.
for cwd in fileList:
    try:
        os.remove(cwd)
    except:
        print("Error while deleting file : ", cwd)       
           




cwd = os.getcwd()
cwd = str(Path(cwd).parents[0]) + "\\data\\"
cwd


fileList = glob.glob(cwd + 'g2*.txt', recursive=True)
fileList
 



# Iterate over the list of filepaths & remove each file.
for cwd in fileList:
    try:
        os.remove(cwd)
    except:
        print("Error while deleting file : ", cwd)      



cwd = os.getcwd()
cwd = str(Path(cwd).parents[0]) + "\\data\\"
cwd



fileList = glob.glob(cwd + '*.csv', recursive=True)
fileList


 
# Iterate over the list of filepaths & remove each file.
for cwd in fileList:
    try:
        os.remove(cwd)
    except:
        print("Error while deleting file : ", cwd)
        
        

        


cwd = os.getcwd()
cwd = str(Path(cwd).parents[0]) + "\\data\\"
cwd        

keepList = []

fileList = glob.glob(cwd + '*0340*.txt', recursive=True)
keepList.append(fileList)
fileList = glob.glob(cwd + '*0410*.txt', recursive=True)
keepList.append(fileList)
fileList = glob.glob(cwd + '*0420*.txt', recursive=True)
keepList.append(fileList)
fileList = glob.glob(cwd + '*0430*.txt', recursive=True)
keepList.append(fileList)
fileList = glob.glob(cwd + '*0480*.txt', recursive=True)
keepList.append(fileList)
fileList = glob.glob(cwd + '*0590*.txt', recursive=True)
keepList.append(fileList)
fileList = glob.glob(cwd + '*0630*.txt', recursive=True)
keepList.append(fileList)
fileList = glob.glob(cwd + '*0640*.txt', recursive=True)
keepList.append(fileList)
fileList = glob.glob(cwd + '*0780*.txt', recursive=True)
keepList.append(fileList)
fileList = glob.glob(cwd + '*00140*.txt', recursive=True)
keepList.append(fileList)
fileList = glob.glob(cwd + '*0760*.txt', recursive=True)
keepList.append(fileList)


keepList = str(keepList).strip('[]').replace("\\\\", "\\").replace("'", "")
keepList

#!/usr/bin/python2


fileList = glob.glob(cwd + '*.txt', recursive=True)
fileList



deleteList = [i for i in fileList if i not in keepList] 
deleteList


cwd = os.getcwd()
cwd = str(Path(cwd).parents[0]) + "\\data\\"
cwd        
 
# Iterate over the list of filepaths & remove each file.
for cwd in deleteList:
    try:
        os.remove(cwd)
    except:
        print("Error while deleting file : ", cwd)
        
 
       
        
#Step 4: Put files into a list

#set to the file extension of "to-be-merged" files
ext = ".txt"
#set to your working directory


cwd = os.getcwd()
cwd = str(Path(cwd).parents[0]) + "\\data\\"
cwd

dir_path = cwd
dir_path
#set to the name of your output file
#results = 'ACSSF_2012_2016_Full.txt'


    
files = os.listdir(dir_path)
files

#e20161ak0001000
#e = estimates
#2016 = year
#1 = 1 year estimate vs. 5 year
#ak = state
#0001 = sequence number
#000 = iterationID


files2 = [k for k in files if 'e' in k]
#files3 = [k for k in files2 if 'e2016' in k]
#files3 = [k for k in files2 if '0041' in k]

files4 = [cwd + x for x in files2]
files4


#Step 5: Create Empty File with generic column headers


my_cols = ["1","YEAR","STATE","4","SEQ","LOGRECNO","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25",
"26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48",
"49","50","51","52","53","54","55","56","57","58","59","60","61","62","63","64","65","66","67","68","69","70","71","72",
"73","74","75","76","77","78","79","80","81","82","83","84","85","86","87","88","89","90","91","92","93","94","95","96",
"97","98","99","100","101","102","103","104","105","106","107","108","109","110","111","112","113","114","115","116",
"117","118","119","120","121","122","123","124","125","126","127","128","129","130","131","132","133","134","135","136",
"137","138","139","140","141","142","143","144","145","146","147","148","149","150","151","152","153","154","155","156",
"157","158","159","160","161","162","163","164","165","166","167","168","169","170","171","172","173","174","175","176",
"177","178","179","180","181","182","183","184","185","186","187","188","189","190","191","192","193","194","195","196",
"197","198","199","200","201","202","203","204","205","206","207","208","209","210","211","212","213","214",
"215","216","217","218","219","220","221","222","223","224","225","226","227","228","229","230","231","232","233","234",
"235","236","237","238","239","240","241","242","243","244","245","246","247","248","249","250","251","252","253",
"254","255","256","257","258","259","260","261","262","263","264","265","266","267","268","269","270","271","272",
"273","274","275","276","277","278","279","280","281","282","283","284","285","286","287","288","289","290","291",
"292","293","294","295","296","297","298","299","300","301","302","303","304","305","306","307","308","309","310","311",
"312","313","314","315","316","317","318","319","320","321","322","323","324","325","326","327","328","329","330",
"331","332","333","334","335","336","337","338","339","340","341","342","343","344","345","346","347","348","349","350",
"351","352","353","354","355","356","357","358","359","360","361","362","363","364","365","366","367","368","369","370",
"371","372","373","374","375","376","377","378","379","380","381","382","383","384","385","386","387","388","389","390",
"391","392","393","394","395","396","397","398","399","400","401","402","403","404","405","406","407","408","409",
"410","411","412","413","414","415","416","417","418","419","420","421","422","423","424","425","426","427","428","429",
"430","431","432","433","434","435","436","437","438","439","440","441","442","443","444","445","446","447","448",
"449","450","451","452","453","454","455","456","457","458","459","460","461","462","463","464","465","466","467",
"468","469","470","471","472","473","474","475","476","477","478","479","480","481","482","483","484","485","486",
"487","488","489","490","491","492","493","494","495","496","497","498","499","500","501","502","503","504","505",
"506","507","508","509","510","511","512","513","514","515","516","517","518","519","520","521","522","523","524",
"525","526","527","528","529","530","531","532","533","534","535","536","537","538","539","540","541","542","543",
"544","545","546","547","548","549","550","551","552","553","554","555","556","557"]


singleFile = [k for k in files if '043' in k]
singleFile1 = [cwd + x for x in singleFile]
singleFile2 = str(singleFile1).strip('[]').replace("\\\\", "\\").replace("'", "")
singleFile2

fullfile = pd.read_csv(singleFile2, names=my_cols, engine='python')

fullfile = fullfile.loc[fullfile['557'] == 0]


#Step 6: Import data into Empty File
#fullfile.head()

for f in files4:
  if f.endswith(ext):
    data = open(f)
    
    out = pd.read_csv(data, names=my_cols, engine='python')
    #out = open(results, 'a')
    
    
    #out2 = out.loc[out['5'] == 41]
    out2 = out
    fullfile = pd.concat([fullfile, out2], ignore_index=True)
                         
    #fullfile.merge(out, how='outer')
    #fullfile = [fullfile, out]
    
    
    #for l in data:
      #print(l, file=out)
    data.close()
    #out.close()
#fullfile.to_csv("csvfile.csv", sep=',', encoding='utf-8')    
   
#fullfile.head()  

#Output to csv
    
    
cwd = os.getcwd()
cwd = str(Path(cwd).parents[0]) + "\\data\\"
cwd
fullfile.to_csv( cwd+ "csvfile.csv", sep=',', encoding='utf-8')


#Step 7: Create LogRecoNo File - Main File for all appending



sheet_names = ['ak',	'al',	'ar',	'az',	'ca',	'co',	'ct',	'dc',	'de',
'fl',	'ga',	'hi',	'ia',	'id',	'il',	'in',	'ks',	'ky',
'la',	'ma',	'md',	'me',	'mi',	'mn',	'mo',	'ms',	'mt',
'nc',	'nd',	'ne',	'nh',	'nj',	'nm',	'nv',	'ny',	'oh',
'ok',	'or',	'pa',	'pr',	'ri',	'sc',	'sd',	'tn',	'tx',
'us',	'ut',	'va',	'vt',	'wa',	'wi',	'wv',	'wy'	
]


cwd = os.getcwd()
cwd = str(Path(cwd).parents[0]) + "\\reference\\"
cwd

dfs = pd.read_excel(cwd + 'geofile.xlsx', sheet_name=sheet_names)
LogRecRef = pd.concat((df.assign(source=sheet) for sheet, df in dfs.items()), ignore_index=True)
LogRecRef.rename(columns = {"Logical Record Number":"LOGRECNO", "State":"STATE"}, inplace = True)


LogRecRef.head()




'''
#Step 7: Rename Headers
fullfile["STATE"] = fullfile['STATE'].str.upper() #uppercase space
fullfile = fullfile.dropna(axis=1, how='all') #, thresh=None, subset=None, inplace=False)
fullfile.head()

fullfile2 = fullfile

fullfile2.head()


cwd = os.getcwd()
cwd = str(Path(cwd).parents[0]) + "\\reference\\"

seqFile = cwd + "Seq43.xlsx"
seqFile


columnnames = pd.read_excel(seqFile, sheet_name='e')

values = {'FILEID': "1", 'FILETYPE': "YEAR", 'STUSAB': "STATE", 
                                'CHARITER': "4","SEQUENCE" : "SEQ", "LOGRECNO": "LOGRECNO"
          }


columnnames2 = columnnames.fillna(value = values)

name_str = columnnames2.transpose() 

name_str

fullfile2.drop(fullfile2.columns[0], axis=1).columns = name_str.values


fullfile2.columns = fullfile2.columns.map(str)

fullfile2.columns = fullfile2.columns.str.strip().str.replace(":", '').str.replace("'", '').str.replace(',', '').str.replace('(', '').str.replace(')', '')

fullfile2.head()
'''



#Step 8: Create CSV from all files

#set to the file extension of "to-be-merged" files
ext = ".txt"
#set to your working directory


cwd = os.getcwd()
cwd = str(Path(cwd).parents[0]) + "\\data\\"
cwd

dir_path = cwd
dir_path




for (i) in range(1,123):
    
    seqcount = "000"+str(i)         
    lseqcount = seqcount[::-1][:4][::-1] + '000'
    #print(lseqcount)
    
    
    swd = os.getcwd()
    swd = str(Path(cwd).parents[0]) + "\\reference\\"        
       
    seq_path = swd
    seq_path
    
    Seqfile = seq_path+"\\Seq" + str(i) + ".xlsx"    
    #print(Seqfile)    
    
    CSVfile = r"csvfile" + str(i) + ".csv"
    #print(CSVfile)  




    files = os.listdir(cwd)

        #e20161ak0001000
        #e = estimates
        #2016 = year
        #1 = 1 year estimate vs. 5 year
        #ak = state
        #0001 = sequence number
        #000 = iterationID

    files2 = [k for k in files if 'e' in k] 
    files3 = [k for k in files2 if lseqcount in k] 
    #files3b = [k for k in files3 if 'ma' in k]
    #files3a = [k for k in files3 if 'e' in k]

    files4 = [cwd + x for x in files3]
    files4



    my_cols = ["1","YEAR","STATE","4","SEQ","LOGRECNO","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25",
    "26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48",
    "49","50","51","52","53","54","55","56","57","58","59","60","61","62","63","64","65","66","67","68","69","70","71","72",
    "73","74","75","76","77","78","79","80","81","82","83","84","85","86","87","88","89","90","91","92","93","94","95","96",
    "97","98","99","100","101","102","103","104","105","106","107","108","109","110","111","112","113","114","115","116",
    "117","118","119","120","121","122","123","124","125","126","127","128","129","130","131","132","133","134","135","136",
    "137","138","139","140","141","142","143","144","145","146","147","148","149","150","151","152","153","154","155","156",
    "157","158","159","160","161","162","163","164","165","166","167","168","169","170","171","172","173","174","175","176",
    "177","178","179","180","181","182","183","184","185","186","187","188","189","190","191","192","193","194","195","196",
    "197","198","199","200","201","202","203","204","205","206","207","208","209","210","211","212","213","214",
    "215","216","217","218","219","220","221","222","223","224","225","226","227","228","229","230","231","232","233","234",
    "235","236","237","238","239","240","241","242","243","244","245","246","247","248","249","250","251","252","253",
    "254","255","256","257","258","259","260","261","262","263","264","265","266","267","268","269","270","271","272",
    "273","274","275","276","277","278","279","280","281","282","283","284","285","286","287","288","289","290","291",
    "292","293","294","295","296","297","298","299","300","301","302","303","304","305","306","307","308","309","310","311",
    "312","313","314","315","316","317","318","319","320","321","322","323","324","325","326","327","328","329","330",
    "331","332","333","334","335","336","337","338","339","340","341","342","343","344","345","346","347","348","349","350",
    "351","352","353","354","355","356","357","358","359","360","361","362","363","364","365","366","367","368","369","370",
    "371","372","373","374","375","376","377","378","379","380","381","382","383","384","385","386","387","388","389","390",
    "391","392","393","394","395","396","397","398","399","400","401","402","403","404","405","406","407","408","409",
    "410","411","412","413","414","415","416","417","418","419","420","421","422","423","424","425","426","427","428","429",
    "430","431","432","433","434","435","436","437","438","439","440","441","442","443","444","445","446","447","448",
    "449","450","451","452","453","454","455","456","457","458","459","460","461","462","463","464","465","466","467",
    "468","469","470","471","472","473","474","475","476","477","478","479","480","481","482","483","484","485","486",
    "487","488","489","490","491","492","493","494","495","496","497","498","499","500","501","502","503","504","505",
    "506","507","508","509","510","511","512","513","514","515","516","517","518","519","520","521","522","523","524",
    "525","526","527","528","529","530","531","532","533","534","535","536","537","538","539","540","541","542","543",
    "544","545","546","547","548","549","550","551","552","553","554","555","556","557"]



    
    singleFile = [k for k in files if '043' in k]
    singleFile1 = [cwd + x for x in singleFile]
    singleFile2 = str(singleFile1).strip('[]').replace("\\\\", "\\").replace("'", "")
    singleFile2
    
    fullfile = pd.read_csv(singleFile2, names=my_cols, engine='python')

    fullfile = fullfile.loc[fullfile['557'] == 0]
    #fullfile



    for f in files4:
      if f.endswith(ext):
        data = open(f)

        #out = pd.read_csv(data, names=my_cols, engine='python')
        out = pd.read_csv(data, names=my_cols, sep=',', engine='python')

        out2 = out
       
        
        
        fullfile = pd.concat([fullfile, out2], sort=False, ignore_index=True)
        
        data.close()



    fullfile["STATE"] = fullfile['STATE'].str.upper() #uppercase space
    
    
    
    
    #fullfile = fullfile.dropna(axis=1, how='all')
    fullfile2 = fullfile

    #fullfile2.to_csv("techers.csv", sep=',', encoding='utf-8')
    #out
    #fullfile


    #Macro1
    #columnnames = pd.read_excel(r"C:\Census Data\References\2016_5yr_Summary_FileTemplates\templates\Seq41.xls", sheet_name='E')
    columnnames = pd.read_excel(Seqfile, sheet_name='e')
    values = {'FILEID': "1", 'FILETYPE': "YEAR", 'STUSAB': "STATE", 
                                    'CHARITER': "4","SEQUENCE" : "SEQ", "LOGRECNO": "LOGRECNO"
              }

    
    
    columnnames2 = columnnames.fillna(value = values)
    name_str = columnnames2.transpose() 

    fullfile2 = fullfile2.iloc[:, 0:len(columnnames2.columns)]
    
    fullfile2.columns = name_str.values
    fullfile2.columns = fullfile2.columns.map(str)
    fullfile2.columns = fullfile2.columns.str.strip().str.replace('"', '').str.replace(":", '').str.replace("'", '').str.replace(',', '').str.replace('(', '').str.replace(')', '').str.replace('%', '!!')

    fullfile2.rename(columns = {"STUSAB":"STATE"}, inplace = True)
    
    geofile = pd.merge(fullfile2, LogRecRef, on = ['LOGRECNO', 'STATE'], how = "left")
    geofile = geofile.drop(['source'], 1)



    dataloc = os.getcwd()
    dataloc = str(Path(dataloc).parents[0]) + "\\data\\"               
    
    #geofile.to_csv("csvfile.csv" sep=',', encoding='utf-8')
    
    
        
        
    if geofile.empty == False:
            
        geofile.to_csv(dataloc + CSVfile, sep=',', encoding='utf-8')
          
        print(CSVfile)
                
    else:
        print(CSVfile + ": has not records")
    
    
    
    
    fileList = glob.glob(cwd + 'csvfile.csv', recursive=True)
    fileList
    
    
        
    cwd = os.getcwd()
    cwd = str(Path(cwd).parents[0]) + "\\data\\"
    cwd        
     
    # Iterate over the list of filepaths & remove each file.
    for cwd in fileList:
        try:
            os.remove(cwd)
        except:
            print("Error while deleting file : ", cwd)
            
            
        
#Step 9: Clean Column Names


  
## Create Template dfMaster Table
df = pd.read_csv(r'C:\Users\pvo\OneDrive\Work\Github\CensusData\data\csvfile59.csv', engine='python')

df = df.drop(columns=['Geography ID','Geography Name','FILEID','FILETYPE','CHARITER','SEQUENCE','Unnamed: 0'])
 
dfMaster = df.copy()

dfMaster["UniqueID"] = dfMaster["STATE"] + dfMaster["LOGRECNO"].map(str)
dfMaster['Grouping'] = ""
dfMaster['Grouping2'] = ""
dfMaster['Grouping3'] = ""
dfMaster['Grouping4'] = ""
dfMaster['Total'] = np.nan 

dfMaster = dfMaster[['UniqueID','Grouping','Grouping2','Grouping3','Grouping4','Total']]

 


#asdfMACRO


cwd = os.getcwd()
cwd = str(Path(cwd).parents[0]) + "\\data\\"
cwd


files = os.listdir(cwd)

    #e20161ak0001000
    #e = estimates
    #2016 = year
    #1 = 1 year estimate vs. 5 year
    #ak = state
    #0001 = sequence number
    #000 = iterationID

files2 = [k for k in files if 'csv' in k] 
files4 = [cwd + x for x in files2]





filenum = len(files4)

##Users

runnum = 0 


while (runnum) < filenum:
    
    
    filename = files4[runnum]
    
    df = pd.read_csv(filename, engine='python')
    
    df = df.drop(columns=['Geography ID','Geography Name','FILEID','FILETYPE','CHARITER','SEQUENCE','Unnamed: 0'])
    
    print("FileName : " + str(filename))
    
    #df = df.columns.str.strip().str.replace("$", '').str.replace("'", '').str.replace(',', '')
    
    #Split File into different subject areas
    
    #keep only columns where the name has !!
    
    subjectareas = pd.DataFrame(df.columns)
    subjectareas = subjectareas.rename(columns={0:"ColNames"})
    subjectareas
    
    #dfObj["ColNames"].str.split("',",1)[0]
    
    subjectareas["ColNames"] = subjectareas["ColNames"].str.split("Total", n = 1, expand = True)[0] 
    
    #TestRun
    #subjectareas["ColNames"] = "SEX BY AGE BY EDUCATIONAL ATTAINMENT FOR THE POPULATION 18 YEARS AND OVER!!Population 18 years and over!!"
    #subjectareas = subjectareas.drop_duplicates(subset=None, keep='first')    
    #subjectareas.loc[2] = ['STATE']
    #subjectareas.loc[3] = ['LOGRECNO']
    
    
    #subjectareas.insert(2,"ColNames","STATE")
    #subjectareas.insert("LOGRECNO")
    
    
    #subjectareas = subjectareas[subjectareas["ColNames"].str.contains("!!")]
    #dfObj2 = dfObj[~dfObj["ColNames2"].str.contains("!!")] - #Not contains
    
    
    subjectareas = subjectareas.drop_duplicates(subset=None, keep='first')        
            
            
    
    
    
    subjectareas.to_csv('subjectareas.csv', sep=',', encoding='utf-8')
    
    #[subjectareas.split('Total', 1)[0] for i in subjectareas]
    
    
    fileLoopCount = subjectareas.shape[0]-2 
    
    #test run
    #if fileLoopCount >= 4: 
    #    fileLoopCount = 3
        
    
    
    subn=0    
    runnum += 1 
    
    
    
    while (subn) < fileLoopCount:
    
        print("Sub Num : " + str(subn))
        
        
        
        subjectareasFilter = subjectareas.iloc[[0,1,subn+2],:] #last number is the loop number    
        subjectareasFilter2 = pd.DataFrame(subjectareasFilter)
        subjectareasFilter2 = subjectareasFilter2.rename(columns={0:"ColNames"})    
       
        subjectareasFilterName = subjectareasFilter2[subjectareasFilter2.ColNames != 'STATE']
        subjectareasFilterName = subjectareasFilterName[subjectareasFilterName.ColNames != 'LOGRECNO']
        
        print(str(subjectareasFilterName))
        
        #subjectareasFilterName.to_csv('subjectareasFilterName.csv', sep=',', encoding='utf-8')
        orgDFColumns = pd.DataFrame(df.columns)
        orgDFColumns = orgDFColumns.rename(columns={0:"ColNames2"})    
        
        orgDFColumns["ColNames"] = orgDFColumns["ColNames2"].str.split("Total", n = 1, expand = True)[0] 
      
        
        columnList = pd.merge(orgDFColumns, subjectareasFilter2, how='inner', on='ColNames')
        columnList["ColNames"] = columnList["ColNames2"]
        columnList = columnList.drop(columns=['ColNames2'])
        
        
        orgDFColumnsList = columnList['ColNames'].tolist()    
        #orgDFColumnsFinal = (df.columns)    
        #dfLoop = df[[s for s in orgDFColumnsFinal if (xs in s for xs in orgDFColumnsList)]]
        
        dfLoop = df[orgDFColumnsList]
        
        
        
        dfLoop["UniqueID"] = dfLoop["STATE"] + dfLoop["LOGRECNO"].map(str)
            
        dfLoop['Grouping'] = ""
            
        #dfFinal = df[['UniqueID','Grouping']]
        #dfFinal = dfLoop[['UniqueID']]
        
    
        
        #df = df.drop(columns=['Geography ID','Geography Name','FILEID','FILETYPE','CHARITER','SEQUENCE','Unnamed: 0','STATE','LOGRECNO','Grouping'])
        #
        
        dfLoop = dfLoop.drop(columns=['STATE','LOGRECNO','Grouping'])    
        #
        ## Drop Columns here
        
        
        subn += 1
        #df
        
        countCol = dfLoop.shape[1]-1
        
        
        #test run
        #if countCol > 10: 
        #    countCol = 10
            
        
        
        n=0
        
        #while (i) < countCol:    
        while (n) < countCol:
                
            #print("Sub Num : " + str(subn))
            
            print("Loop 1:")
            print("Run Number : " + str(n))
            
            df2 = dfLoop.iloc[:, [-1,n]].copy()
            #df2
            
            #df2.to_csv('df2.csv', sep=',', encoding='utf-8')
               
            #drig = df2.columns.str.split('Total',1).str[0][1] 
           # drig
            
            #df2['Grouping']= df2.columns.str.split('Total',2).str[0][1] #change first number
            df2['Grouping'] = (subjectareasFilterName["ColNames"].iloc[0])
            
            
            #df2.to_csv('df2.csv', sep=',', encoding='utf-8')
                
            
            if "Total" in df2.columns.str[:][1]: 
                
            
                if "!!" in df2.columns.str.split('Total',2).str[1][1] :                        
                                
                    split_2 = df2.columns.str.split('Total',2).str[1][1][2:]
                    
                    if "!!" not in split_2:
                        
                        Group2Name = df2.columns.str.split('Total',2).str[1][1][2:]
                        df2['Grouping2'] = Group2Name
                        df2['Grouping3'] = ''
                        df2['Grouping4'] = ''
                        
                                
                    if "!!" in split_2:
                        
                        Group2Name = df2.columns.str.split('Total',2).str[1][1][2:]
                        Group2Name1 = split_2.split('!!',1)[0]
                        df2['Grouping2'] = Group2Name1
                        
                        split_3 = split_2.split('!!',1)[1]
                        
                        if "!!" not in split_3:
                        
                            df2['Grouping3'] = split_3
                            df2['Grouping4'] = ''
                                
                        if "!!" in split_3:
                        
                            df2['Grouping3'] = split_3.split('!!',1)[0]
                            df2['Grouping4'] = split_3.split('!!',1)[1]
                            
                if "!!" not in df2.columns.str.split('Total',2).str[1][1] : 
                                 
                     Group2Name = df2.columns.str.split('Total',2).str[1][1]
                     
                     if "!!" in Group2Name: 
                         df2['Grouping2'] = Group2Name[2:]
                         df2['Grouping3'] = ''
                         df2['Grouping4'] = ''
                     
                     if "!!" not in Group2Name: 
                         df2['Grouping2'] = Group2Name
                         df2['Grouping3'] = ''
                         df2['Grouping4'] = ''
                    
            
            if "Total" not in df2.columns.str[:][1]:
                
                if "!!" in df2.columns.str[:][1] :                        
                                
                    split_2 = df2.columns.str.split('!!',1).str[1][1]
                    
                    if "!!" not in split_2:
                        
                        Group2Name = df2.columns.str.split('!!',1).str[1][1]
                        df2['Grouping2'] = Group2Name
                        df2['Grouping3'] = ''
                        df2['Grouping4'] = ''
                        
                                
                    if "!!" in split_2:
                        
                        Group2Name1 = split_2.split('!!',1)[0]
                        df2['Grouping2'] = Group2Name1
                        
                        split_3 = split_2.split('!!',1)[1]
                        
                        if "!!" not in split_3:
                        
                            df2['Grouping3'] = split_3
                            df2['Grouping4'] = ''
                                
                        if "!!" in split_3:
                        
                            df2['Grouping3'] = split_3.split('!!',1)[0]
                            df2['Grouping4'] = split_3.split('!!',1)[1]
                            
                if "!!" not in df2.columns.str[:][1]  : 
                                 
                     Group2Name = df2.columns.str[:][1] 
                     
                     if "!!" in Group2Name: 
                         
                         df2['Grouping2'] = Group2Name[2:]
                         df2['Grouping3'] = ''
                         df2['Grouping4'] = ''
                     
                     if "!!" not in Group2Name: 
                         df2['Grouping2'] = Group2Name
                         df2['Grouping3'] = ''
                         df2['Grouping4'] = ''
                
                
                
                    
            oldColumnName = df2.columns[1]            
            newColumnName = 'Total'            
            df2.rename(columns = {oldColumnName : newColumnName}, inplace = True)
                
            
            df2.to_csv('df2.csv', sep=',', encoding='utf-8')
            
            
    
            df2 = df2[['UniqueID','Grouping','Grouping2','Grouping3','Grouping4','Total']]
            
            
            
            if df2['Total'].dtype != np.number:
            
                
                df2['Total'] = df2['Total'].replace(r'.','0').astype(float)
                
                #df2['Total'] = int(df2['Total'])
                df2 = df2[df2['Total'] >= 0]
                
            
            df2 = df2[df2['Total'] >= 0]
          
            dfMaster = dfMaster[['UniqueID','Grouping','Grouping2','Grouping3','Grouping4','Total']]
            
    
            
            dfMaster = dfMaster.append(df2, ignore_index = True, sort=False) 
    
            n += 1
            
            split_2 = ''
            split_3 = '' 
    
    
    
        else:
          
          print("Loop is complete")
          dfMaster = dfMaster[dfMaster['Total'] >= 0]
            
          dfMaster.to_csv('dfMaster.csv', sep=',', encoding='utf-8')
          
          
          



