#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import git
import os
import shutil
import zipfile
def get_file_content(git_oper,branch_name,rel_file):
    try:
        git_cmd = branch_name +r':'+ rel_file
        raw_content = git_oper.show(git_cmd)
        single_file_content = raw_content.encode('utf-8','ignore')
    except:
        raise
    return single_file_content

def copy_single_file(dst_path,rel_file,file_content):
    if(not (os.path.exists(dst_path) and os.path.isdir(dst_path)) ):
        return -1
    full_path = os.path.join(dst_path,rel_file.replace('/','\\'))
    dir_name = os.path.dirname(full_path) 
    if(not os.path.exists(dir_name)):
        os.makedirs(dir_name)
    with open(full_path,'wb') as f:
        f.write(file_content)

def dfs_get_zip_file(input_path,result):
#
    files = os.listdir(input_path)
    for file in files:
        if os.path.isdir(input_path+'\\'+file):
            dfs_get_zip_file(input_path+'\\'+file,result)
        else:
            result.append(input_path+'\\'+file)

def zip_path(input_path,output_path,output_name):
    with zipfile.ZipFile(output_path+'\\'+output_name,'w',zipfile.ZIP_DEFLATED) as f:
        filelists = []
        dfs_get_zip_file(input_path,filelists)
        for file in filelists:
            f.write(file)
    return output_path+'\\'+output_name

    
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
        for single_file in rel_file_list:
            try:
                old_file_content = get_file_content(git_oper,old_branch,single_file)
            except:
                pass
            else:
                copy_single_file(temp_path_old,single_file,old_file_content) 
            try:
                new_file_content = get_file_content(git_oper,new_branch,single_file)
            except:
                pass
            else:
                copy_single_file(temp_path_new,single_file,new_file_content)
                  
            zip_path(temp_path,dst_path,'work1.zip')               
                
    finally:
        shutil.rmtree(temp_path)
        pass
    return 0

print(copy_file('HEAD^','HEAD','D:\\project\\python\\CodeReviewer','D:\\'))