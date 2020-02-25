import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
     name='bizzzz',  
     version='0.1',
     scripts=['bizzzz'] ,
     author="Ankur Singh",
     author_email="ankur310794@gmail.com",
     description="A utility package",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/Ankur3107/Research/tree/master/pip_package/bizzzz",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent"
     ]
 )