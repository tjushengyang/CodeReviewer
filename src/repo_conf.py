#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import configparser
def get_option_value(section,option):
    cf=configparser.ConfigParser()
    cf.read('..\\conf\\config.ini','utf-8')
    if(cf.has_option(section, option)):
        return cf.get(section,option)
    return ''


