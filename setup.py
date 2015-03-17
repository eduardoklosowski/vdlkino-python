from setuptools import find_packages, setup


version = __import__('vdlkino').__version__


setup(
    name='vdlkino',
    version=version,
    description='Library in Python for comunicate computer with Arduino running VDLKino',
    author='Eduardo Klosowski',
    author_email='eduardo_klosowski@yahoo.com',
    license='MIT',
    packages=['vdlkino'],
    zip_safe=False,
    extras_require={
        'serial': ['pyserial'],
    },
)
