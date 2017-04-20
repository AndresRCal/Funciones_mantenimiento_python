# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 08:39:57 2017

@author: AAREYESC
"""

import pip
import conda
import alGusto as alg
import os
from subprocess import call

if os.path.exists(os.getcwd()+os.sep+'Logs') == False:
        os.makedirs(os.getcwd()+os.sep+'Logs')
else:
    pass
alg.escribe_log('\n',os.getcwd()+os.sep+'Logs','Matenimiento','.txt')
alg.escribe_log('''MANTENIMIENTO PYTHON UPGRADDE ALL PACKAGES  '''+'__'+alg.fecha,os.getcwd()+os.sep+'Logs','Matenimiento','.txt')
alg.escribe_log('\n',os.getcwd()+os.sep+'Logs','Matenimiento','.txt')
for dist in pip.get_installed_distributions():
    try:
        call("conda update " + dist.project_name, shell=True)
        alg.escribe_log("conda update " + dist.project_name,os.getcwd()+os.sep+'Logs','Matenimiento','.txt')
        print("conda update " + dist.project_name)
    except conda.CondaError as msg:
        alg.escribe_log('ERROR: '+"conda update " + dist.project_name+msg,os.getcwd()+os.sep+'Logs','Matenimiento','.txt')
        print('ERROR: '+"conda update " + dist.project_name+msg)
        call("pip install --upgrade " + dist.project_name, shell=True)
    