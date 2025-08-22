from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = "-e ."
def get_requirement(file_path:str)-> List[str]:
    '''
    This function will return the list of requirements.
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("/n","") for req in file_obj]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name="SCT_ML_01",
    version="0.0.1",
    author="Koushik",
    author_email="kmanna713@gmail.com",
    packages=find_packages(),
    install_requires=get_requirement("requirements.txt")
)