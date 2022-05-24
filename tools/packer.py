from . import utils
from zipfile import ZipFile
import os
  
def get_all_file_paths(directory): 
    # initializing empty file paths list
    file_paths = []
  
    # crawling through directory and subdirectories
    for root, directories, files in os.walk(directory):
        for filename in files:
            # join the two strings in order to form the full filepath.
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)
  
    # returning all file paths
    return file_paths        

def pack_lambda():
    print(utils.REPO_ROOT)
    deps_lib_root = os.path.join(utils.REPO_ROOT, f'.venv/lib/python{utils.PYTHON_VERSION}/site-packages')
    lambda_src_root = os.path.join(utils.REPO_ROOT, 'src/sample_python_lambda')
    lambda_zip = os.path.join(utils.REPO_ROOT, 'artifacts', 'lambda.zip')
    print(f'Creating package {lambda_zip}')
    
    with utils.cd(deps_lib_root):
        deps_paths = get_all_file_paths('.')
        # for p in deps_paths:
        #     print(deps_paths)
        with ZipFile(lambda_zip,'w') as zip:
            # writing each file one by one
            for file in deps_paths:
                zip.write(file)

    with utils.cd(lambda_src_root):
        paths = get_all_file_paths('.')
        with ZipFile(lambda_zip,'a') as zip:
            # writing each file one by one
            for file in paths:
                zip.write(file)
  
    print('All files zipped successfully!')  

    # with cd(REPO_ROOT):
    #     print('aaa')

def unpack_lambda(zip_file, target_dir):
    with ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall(target_dir)