#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import git
import sys
import os
def copy_file(src_branch,dst_branch,source_path = r'D:\project\test1'):
    if(os.path.exists(source_path) and os.path.isdir(source_path)):
        pass
    else:
        return -1
    try:
        repo = git.Repo(source_path)
    except git.InvalidGitRepositoryError as e:
        print("path %s is not a repo" % e)
        return -1
    except:
        return -1
    else:
        git_oper = repo.git
        git_oper.fetch() 
        print(git_oper.diff('--name-only',src_branch,dst_branch))    



print(copy_file('HEAD','HEAD^'))