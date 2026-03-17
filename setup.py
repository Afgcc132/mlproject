from setuptools import find_packages, setup
from typing import List

# Función opcional para leer el requirements.txt automáticamente
def get_requirements(file_path: str) -> List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        # Limpiamos los saltos de línea (\n)
        requirements = [req.replace("\n", "") for req in requirements]
        
        # Eliminamos el '-e .' si está en el archivo para evitar bucles
        if "-e ." in requirements:
            requirements.remove("-e .")
            
    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='Alex',
    author_email='afgcc132@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt') # Lee tus librerías aquí
)