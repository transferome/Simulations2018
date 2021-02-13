"""Clear files except the package contents from the folder"""
import os
import glob
import shutil


def clean():
    files_keep = glob.glob('*py')
    folders_keep = ['constructhaplotypes', 'forqs', 'foundinghaplotypes',
                    'multinomialfreqs', 'preselect', 'recombination',
                    'selectprep', 'simreads', 'harpsnp', 'core',
                    '.git', '.idea']
    keep = files_keep + folders_keep
    folder_contents = os.listdir()
    contents_delete = [content for content in folder_contents if content not in keep]
    for content in contents_delete:
        if os.path.isfile(content):
            print(content)
            os.remove(content)
        else:
            print(content)
            shutil.rmtree(content)


if __name__ == '__main__':
    clean()
