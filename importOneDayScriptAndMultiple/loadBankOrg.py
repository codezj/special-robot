#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import sys
import json
from string import Template

class loadBank():
      def __init__(self,username,password):
                    self.username=username
                    self.password=password
      def readBankOrg(self,args):
                    #print ('args[0] is %s' %(args[0])) 
                    with open(args) as load_f:
                            jobCfg = json.load(load_f)
                    #return (user = Template(username).substitute(**jobCfg))
                    return  (Template(username).substitute(**jobCfg),Template(password).substitute(**jobCfg))
      def listToDic(self,listA,listB):
                    dict={};
                    i=0
                    length=len(listA) 
                    while i < length:
                           dict[listA[i]]=listB[i]
                           i+=1
                    return dict



def main(argv):
      global username 
      global password

      username = "${username}"
      password = "${password}" 
      file_load = argv
     # print('file is %s' %(file_load))
      C1=loadBank("${username}","${password}")
      user,passwd = C1.readBankOrg(file_load)
      userList=user.split()
      passwdList=passwd.split()
      name_org=C1.listToDic(userList,passwdList)
      print(name_org) 
     # print('user is %s passwd is %s' %(user,passwd))
     # return name_org
if __name__ == "__main__":
    main(sys.argv[1])
