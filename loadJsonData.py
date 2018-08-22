#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import sys
import json
from string import Template
from loadBankOrg import loadBank
class jsonloadBank(loadBank):
      def readBankOrg(self,args):
                    #print ('args[0] is %s' %(args[0])) 
                    with open(args) as load_f:
                            jobCfg = json.load(load_f)
                    #return (user = Template(username).substitute(**jobCfg))
                    return  (Template(username).substitute(**jobCfg),Template(password).substitute(**jobCfg))
                    #return  (Template(dicForm).substitute(**jobCfg))

def main(argv):
      global username 
      global password
      username = "${username}"
      password = "${password}" 
      file_load = argv
     # print('file is %s' %(file_load))
      C1=jsonloadBank(username,password)
      user,passwd = C1.readBankOrg(file_load)
      userList=user.split()
      passwdList=passwd.split()
      name_org=C1.listToDic(userList,passwdList)
      json_name_org=json.dumps(name_org)
      print(json_name_org)
     # print(name_org) 
     # print('user is %s passwd is %s' %(user,passwd))
     # return name_org
if __name__ == "__main__":
    main(sys.argv[1])
