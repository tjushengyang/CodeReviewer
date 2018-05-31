#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import git
import sys
import os
def copy_file(old_branch,new_branch,src_path,dst_path):
    if(os.path.exists(src_path) and os.path.isdir(src_path)):
        pass
    else:
        return -1
    if(os.path.exists(dst_path) and os.path.isdir(dst_path)):
        pass
    else:
        return -1
    try:
        repo = git.Repo(src_path)
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
            abs_file_list.append(os.path.join(dst_path,item.replace('/','\\')))
        print(abs_file_list)
        
    return 0

print(copy_file('HEAD','HEAD^','D:\\project\\test1','D:\\'))