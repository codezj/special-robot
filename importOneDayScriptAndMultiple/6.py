#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# ## ./3.py -t table -o org_nu -b 20180510   -u  bankname -s  config/lfyh.json
#1.py update based on previous script , it means include some methods which will not use 
#2.py recreate scrpts , it means not used methods are removed
#3.py add dict to remove one parameter which is org_no, when you input bank name, it will provide org_no from dic
#4.py load dict from json file
#5.py user other way instead of eval , based on eval will not work well if json file have multiple lines for one parameter
#6.py connect to json file which have full bank and org,file name fullbankOrg
from datetime import datetime, date, timedelta
from string import Template
import os, sys, getopt, calendar
import json, subprocess
from loadBankOrg import loadBank
#sqoop import -Dmapreduce.map.memory.mb=20480 -Dmapreduce.reduce.memory.mb=20480 -Dmapreduce.job.queuename=root.default.sqoop
#global ENGINE_COMMAND="--connect ${connect} --username ${username} --password ${password}"
class ConnectDB2:
	global ENGINE_COMMAND
	ENGINE_COMMAND="sqoop import -Dmapreduce.map.memory.mb=20480 -Dmapreduce.reduce.memory.mb=20480 -Dmapreduce.job.queuename=root.default.sqoop --connect ${connect} --username ${username} --password ${password}"
	EXEC_CMD=""
	def buildStartCommand(self,options, args):
                    with open(args[0]) as load_f:
                            jobCfg = json.load(load_f)
                    return Template(ENGINE_COMMAND).substitute(**jobCfg)

class ImportDayData:
        def exec(self,schema,table,org,begin,show):
            cmd = '%s --table %s.%s -m 1 --hcatalog-database east --hcatalog-table %s --hcatalog-partition-keys org_no,load_date --hcatalog-partition-values "%s","%s" --where "cjrq=\'%s\' " ' % (EXEC_CMD,schema, table, table, name_org[schema], begin, begin)
            print('exec cmd: %s' % cmd)
            # os.system(cmd)
            if show == False:
                    p = subprocess.Popen(cmd, shell=True)
                    return p
#below function is not used anymore for singel day import 
def get_month_range(start_date=None):
    if start_date is None:
       raise ValueError('start date is null')
    not_use,days_in_month = calendar.momthrange(start_date.year,start_date.month)
    end_date = start_date + timedelta(days = (days_in_month - start_date.day + 1))
    return start_date

class LimitDate:
       begin = None
       global max_date
       global min_date
       max_date = datetime(2019,5,1)
       min_date = datetime(2015,1,1)
       #print(begin)
       def limitDateFunc(self,begin):
            if begin > max_date or begin < min_date :
                  raise ValueError('date is invalid! %s ' % (begin))
def main(argv):
    global name_org
    #obj=subprocess.Popen("./loadBankOrg.py administrator.json", shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    name_org_json=os.popen("./onlyLoad.py fullbankOrg.json").read()
    #name_org=eval(name_org_str)
    name_org=json.loads(name_org_json)
   # print('type is %s' %type(name_org_str))
   # print('dic type is %s' %type(name_org))
   # name_org=json.loads(name_org_str) 
    #name_org=(obj.stdout.read())
    #print(obj.stdout.read())
    #name_org={'hbyh': 313121006888,
    #          'qhdyh': 313126001022,
    #          'hdyh': 313127000013,
    #          'xtyh': 313131000016,
    #          'zjkyh': 313138000019,
    #          'cdyh': 313141052422,
    #          'czyh': 313143005157,
    #          'lfyh': 313146000019,
    #          'hsyh': 313148053964,
    #          'hbsls': 402121000009,
    #          'tsyh': 313124000018,
    #          'bdyh': 313134000011}
    #print('name_org is %s' %name_org)
    #print('name_org is %s' %name_org.keys())

#declare varable which will be used in following process
    show = False
    schema = ''
    table = ''
    org = ''
    begin = None
    processes = []
    global bankExist 
    bankExist = True
    try:
        opts, args = getopt.getopt(argv, "sht:u:o:b:",["show","bankname","help", "table=","org=","begin="])
        global EXEC_CMD
        C1=ConnectDB2()
        EXEC_CMD = C1.buildStartCommand(opts, args)
       # print(EXEC_CMD)
    except getopt.GetoptError as e:
        print(e)
        print('./etl_administrator.py -p no|org|orgdate -u schema -t TABLE_NAME -o ORG_NO -b 201707 -e 201707 -s east_hbyh.json')
        print('-s : only print cmd')
        print('-p : --partition method no|org|orgdate')
        print('-l : add --split-by CJRQ -m 5 parmas')
        sys.exit(2)
    for opt, arg in opts:
            if opt == '-h':
                print('./multi_month.py -t TABLE_NAME -b 20170701  -u bankname')
                sys.exit(2)
            elif opt in ("-s", "--show"):
                show = True
            elif opt in ("-o", "--org"):
                org = arg
            elif opt in ("-u"):
                schema = arg
            elif opt in ("-t"):
                table = arg
            elif opt in ("-b", "--begin"):
                begin = arg
               #begin = datetime.strptime(arg, '%Y%m%d')
               # checkDate=LimitDate()
               # checkDate.limitDateFunc(begin)
    bankExist =  schema in name_org.keys()
    if bankExist:
       print('bank name is  valid  %s'   %schema)
    else :
       raise ValueError('bank name is not valid! %s ' %schema)
    tbls = table.split(',')
    for tbl in tbls:
        importData=ImportDayData()
        p = importData.exec(schema,tbl,org,begin,show)
        processes.append(p)
if __name__ == "__main__":
    main(sys.argv[1:])
