# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 15:46:30 2020

@author: pvo
"""


        
            
        ## PVO
            
        
        colName = df2.columns[1]
        colName
            
        newcolName = df2.columns.str.split('Total',2).str[1][1] #change second number
        
        
        if str(newcolName) != 'nan':
            if newcolName[0:2] == '!!':
                newcolName = newcolName[2:]

                
        if str(newcolName) == 'nan' or newcolName =='':
            newcolName = 'Total'
            
        #print(str(newcolName))
            
        
        df2.rename(columns = {colName : newcolName}, inplace = True)
        
        
        #dfMaster = pd.merge(dfMaster, df2, on=['UniqueID'], how='left')
        #dfMaster= pd.concat([dfMaster, df2], sort=True)
        
        
        dfMaster = dfMaster.append(df2, ignore_index = True, sort=False) 
        
        
        #dfMaster = dfMaster[dfMaster.sum(axis = 1, skipna = True) > 0]
        
        #dfMaster = dfMaster.drop(columns=['Grouping_x'])
    
            
        print(str("Renamed : " + colName + "     to        " + newcolName))
    
        
        n += 1
        
        dfMaster.to_csv('dfMaster.csv', sep=',', encoding='utf-8')
        #dfFinal
        
        #dfMaster = dfMaster[dfMaster["Grouping"].notnull()]
    
    else:
      
      print("Loop is complete")
      dfMaster = dfMaster[dfMaster['Total'] >= 0]
      dfMaster.to_csv('dfMaster.csv', sep=',', encoding='utf-8')
    
    
    
    
    
    
    
    
    
    
    
    
    
    loop2Count = dfMaster.copy() #.drop(columns=['Total','Grouping'])
    loop2Count
    #loop2Count.to_csv('loop2Count.csv', sep=',', encoding='utf-8')
    
    dfLoop2 = loop2Count.copy()
    
    dfLoop2.to_csv('dfLoop2.csv', sep=',', encoding='utf-8')
    
    
    #loop2Count = loop2Count.drop(columns=['Total','Grouping'])
    
    
    Loop2countCol = loop2Count.shape[1]-6

    

    #test run
    if Loop2countCol > 15: 
       Loop2countCol = 15        
    
    print("Total Loop2 Runs :" + str(Loop2countCol))
    
    n2 = 0
    
    
    while (n2) < Loop2countCol:
            
        
        print("Sub Num : " + str(subn))
        print("Loop 2 :")
        print("Run Number : " + str(n2))
        
        dfLoop2a = dfLoop2.iloc[:, [n2+6,0]].copy()
        
        Grouping1Value = subjectareasFilterName
        dfLoop2a
        #group1.to_csv('group1.csv', sep=',', encoding='utf-8')
        
        dfLoop2ColName= dfLoop2a.columns.str.split('!!',1).str[0][0]
        dfLoop2ColName
        
        dfLoop2a['Grouping2'] = dfLoop2ColName
        dfLoop2a   
        
        
        
        Group2Name.insert(n2, dfLoop2ColName)
                        
                
        
                    
    
                    
        #newcolName = dfLoop2a.columns.str.split('!!',1).str[0][6] #change second number
        
        dfLoop2ColumnName = dfLoop2a.columns.str.split('!!',1).str[1][0]    
        dfLoop2ColumnName
        
        
        if str(dfLoop2ColumnName) != 'nan': #and not str(dfLoop2ColumnName).isspace():
            
            dfLoop2UseName =  dfLoop2a.columns.str.split('!!',1).str[1][0]    
        
        else :     
            dfLoop2UseName = 'Total'
        
        
        dfLoop2UseName
           
        colName = dfLoop2a.columns[0]
        colName
                
        newcolName = dfLoop2UseName
        newcolName
            
            
        dfLoop2b = dfLoop2a #.drop(columns=['Total'])
        dfLoop2b.rename(columns = { colName : newcolName}, inplace = True)
        
        
        dfLoop2b['Grouping'] =  (subjectareasFilterName["ColNames"].iloc[0])
        dfLoop2b['Grouping3'] = ""
        dfLoop2b['Grouping4'] = ""
        
        
        if dfLoop2UseName == 'Total':
            dfLoop2b = dfLoop2b[['UniqueID','Grouping','Grouping2','Grouping3','Grouping4','Total']]
        else :
            dfLoop2b['Total'] = ""
            dfLoop2b = dfLoop2b[['UniqueID','Grouping','Grouping2','Grouping3','Grouping4','Total',newcolName]]
        
        
        dfLoop2b.to_csv('dfLoop2b.csv', sep=',', encoding='utf-8')   
        
        #dfLoop2b = dfLoop2b[['UniqueID','Grouping','Grouping2','Grouping3','Grouping4','Total',newcolName]]
        
        
        dfMaster = dfMaster[['UniqueID','Grouping','Grouping2','Grouping3','Grouping4','Total']]
        
        
        #dfLoop2a = dfLoop2a[dfLoop2a["Total"].notnull()]    
        
        #dfLoop2b = dfLoop2b.loc[:,~dfLoop2b.columns.duplicated()] 
        #dfLoop2b = dfLoop2b[dfLoop2b.sum(axis = 1, skipna = True) > 0]
            

                          
           
        dfMaster = pd.concat([dfMaster, dfLoop2b], sort=False)
        
        #dfMaster = dfMaster.append(dfLoop2b, ignore_index = True, sort=False) 
        
        
        #dfMaster = dfMaster[dfMaster.sum(axis = 1, skipna = True) > 0]
        
        print(str("Renamed : " + colName + " to " + newcolName))
    
    
        n2 += 1
        
        del dfLoop2a
        del dfLoop2b
    
    
    
    else:
        print("Loop 2 is complete")
        dfMaster.to_csv('dfMaster2.csv', sep=',', encoding='utf-8')  
    
    
    

print("END")           