from setuptools import setup
setup(
        name = 'sic',
        version = '0.2',
        description = 'simple image clustering',
        packages = ['sic'],
        install_requires =['numpy', 'opencv-python'],
        entry_points = {'console_scripts': ['sic = sic.sic:main']}
        )
