#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import git
import sys
import os
import shutil
def copy_file(old_branch,new_branch,repo_path,dst_path):
    if(os.path.exists(repo_path) and os.path.isdir(repo_path)):
        pass
    else:
        return -1
    if(os.path.exists(dst_path) and os.path.isdir(dst_path)):
        pass
    else:
        return -1
    temp_path = 'C:\\tempForGitDiff'
    temp_path_new = os.path.join(temp_path,'new')
    temp_path_old = os.path.join(temp_path,'old')
    # 创建临时目录
    if(not os.path.exists(temp_path_new)):
        ret = os.makedirs(temp_path_new)
        if(False == ret):
            return -1
    if(not os.path.exists(temp_path_old)):
        ret = os.makedirs(temp_path_old)
        if(False == ret):
            return -1
        
    try:
        repo = git.Repo(repo_path)
    except git.InvalidGitRepositoryError as e:
        print("path %s is not a repo" % e)
        return -1
    except:
        return -1
    else:
        git_oper = repo.git
        git_oper.fetch() 
        query_result = git_oper.diff('--name-only',old_branch,new_branch)
        rel_file_list = query_result.split('\n')
        abs_file_list = []
        for item in rel_file_list:
            abs_file_list.append(os.path.join(temp_path_new,item.replace('/','\\')))
        print(abs_file_list)
    finally:
        shutil.rmtree(temp_path)
        
 #         print(os.path.basename(abs_file_list[0]))
    return 0

print(copy_file('HEAD','HEAD^','D:\\01Code\\UGWV9R18C00_doc','D:\\'))