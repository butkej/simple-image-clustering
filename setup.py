from setuptools import setup, find_packages
setup(
        name = 'sic',
        version = '0.2',
        description = 'simple image clustering',
        package_dir = {'': 'sic'},
        packages = find_packages(where='sic'),
        install_requires =['numpy', 'opencv-python'],
        entry_points = {'console_scripts': ['sic=sic:main',],}
        )
