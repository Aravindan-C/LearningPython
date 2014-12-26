__author__ = 'aravindan'

import pandas as pd
import time
import pandas.io.sql as sql
import mysql.connector


assetList = ["'RWM'","'HYG'","'FXI'","'VTI'","'XLF'","'EFA'","'XLP'","'EWU'","'BND'","'EPI'","'EWH'","'EWA'","'AMLP'","'USO'","'EWW'","'IWD'","'IWF'","'VEA'","'EZU'","'VGK'"]
str1 = ','.join(assetList)
print str1

host = "172.16.30.122"
user = "dvmonitor"
pwd = "m0nitor"
db = "ceres_config"

queryPrime = "SELECT asset_id FROM `asset_definition` WHERE asset_name IN ("+str1+")"

connect = mysql.connector.connect(host=host, user=user, password=pwd, database=db)
print "Connection Successful"
assetId = sql.read_frame(queryPrime, connect)
connect.close()

date =  (time.strftime("%d-%m-%y"))
time =  (time.strftime("%H-%M-%S"))

datetime = date +"_"+ time
print datetime

strategy = "'svr-eq-strategy'"
assetId = assetId
print (assetId)
assetType = "'EQUITY'"
configId = 18813
poId = 95


length = len(assetList)

strategyList = []
assetTypeList = []
configIdList = []
poIdList = []

for each in assetList:
    strategyList.append(strategy)
    assetTypeList.append(assetType)
    configIdList.append(configId)
    poIdList.append(poId)

InputFileDF = pd.DataFrame(strategyList)

assetListSeries = pd.Series(assetList, name = "asset")
InputFileDF = InputFileDF.join(assetListSeries)
#assetIdSeries = pd.Series(assetId, name = 'Id')
InputFileDF = InputFileDF.join(assetId)
assetTypeList = pd.Series(assetTypeList, name = "Type")
InputFileDF = InputFileDF.join(assetTypeList)
configIdList = pd.Series(configIdList, name = "configId")
InputFileDF = InputFileDF.join(configIdList)

if strategy == "ml-eq-creamer-strategy":
    poIdList = pd.Series(poIdList, name = "poId")
    InputFileDF = InputFileDF.join(poIdList)

fileName = "ProdFile_"+datetime+".txt"
InputFileDF.to_csv("/home/aravindan/ProdFile/"+fileName, index=False, header=False)
