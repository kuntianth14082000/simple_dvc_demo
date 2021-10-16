from setuptools import setup ,  find_packages

#find_packages will automatically finds the file which is with __xyz__.py

setup(
    name = "src",
    version = "0.0.1",
    description = "it's a wine Q package",
    author = 'kunthal',
    packages = find_packages(),
    licence =  "MIT"
)
