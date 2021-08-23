from setuptools import setup

setup(
    name='screenplay',
    version='1.0.0',
    description='Screen play pattern in Python',
    url='https://github.com/byran/ScreenPlay',
    author='Byran Wills-Heath',
    author_email='byran@adgico.co.uk',
    license='MIT',
    packages=[
        'screenplay',
        'screenplay.actions',
        'screenplay.matchers',
        'screenplay.threading'
    ],
    zip_safe=False
)
