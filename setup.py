from setuptools import setup , find_packages
from typing import List


project_name="housing_project"
version="0.0.1"
author="hema srinivasulu"
desc="my third project"
requirements_file="requirements.txt"

hypen="-e ."
requirements=[]


def get_requirements(file_name:str)->List[str]:
    with open(file_name) as f:
        requirements=f.readlines()
        requirements=[i.replace("\n","") for i in requirements]
        
        if hypen in requirements:
            requirements.remove(hypen)
            
    return requirements

setup(name=project_name,
      version=version,
      description=desc,
      author=author,
      packages=find_packages(),
      install_requires=get_requirements(requirements_file))

