from setuptools import setup
setup(
        name = 'sic',
        version = '1.2',
        author = 'Joshua Butke',
        author_email= 'butkej@gmail.com',
        description = 'simple image clustering',
        #package_dir = {'': 'sic'},
        packages = ['sic'],
        install_requires =['numpy', 'opencv-python', 'matplotlib'],
        #entry_points = {'console_scripts': ['sic=sic.sic:main'],},
        scripts=['bin/sic']
        )
