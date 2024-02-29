from setuptools import setup, find_packages

setup(
    name='icc_utils',
    version='0.1',
    packages=find_packages(),
    description='Package used to handle common functions at ICC',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Jordan Bradley',
    author_email='jbradley@internationalcybernetics.com',
    url='https://github.com/yourusername/your_package_name',
    install_requires=[
        # Any dependencies your package needs to work, e.g., 'requests >= 2.20.0'
    ],
)