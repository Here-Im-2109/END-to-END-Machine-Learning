# setup.py is used to buils and distribute the package in pypi means we can upload our package to 
# pypi server so that others can also use it by installing through pip command

from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'


def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements

setup(
name='end_to_end_ml_project',
version='0.0.1',
author='Arpan Chandra',
author_email='1.arpanchandra@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')

)