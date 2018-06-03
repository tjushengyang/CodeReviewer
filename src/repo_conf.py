#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import configparser
import os
class LogInfo():
    def __init__(self,username,password,repo_path,dst_path):
        self.username= username
        self.password = password
        self.repo_path = repo_path
        self.dst_path = dst_path
        
def get_option_value(section,option):
    cf=configparser.ConfigParser()
    cf.read('..\\conf\\config.ini','utf-8')
    if(cf.has_option(section, option)):
        return cf.get(section,option)
    return ''

def set_cfg(myloginfo):
    cf=configparser.ConfigParser()
    cf.add_section('remote')
    cf.set('remote', 'username', myloginfo.username)    
    cf.set('remote', 'password', myloginfo.password)

    cf.add_section('local')
    cf.set('local', 'repository', myloginfo.repo_path)    
    cf.set('local', 'output', myloginfo.dst_path)
    if(not os.path.exists('..\\conf')):
        os.makedirs('..\\conf')
    with open('..\\conf\\config.ini','w') as f:
        cf.write(f)
    


