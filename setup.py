from setuptools import setup, find_packages

setup(
    name='erplib',
    version='0.1.15',
    packages=find_packages(),
    install_requires=[
        'fastapi',
        'sqlalchemy',
        'psycopg2-binary',
        'alembic',
        'pydantic-settings'
    ],
    url='https://github.com/abhineshkr/erplib',
    author='Your Name',
    author_email='yourname@example.com',
    description='A Python library for ERP systems using PostgreSQL and SQLAlchemy',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    license='MIT',
)
