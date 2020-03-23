from setuptools import setup
import nonpythonic

setup(
    name='nonpythonic',
    version=nonpythonic.__version__,
    description="Dance in Python's crippled lambdas.",
    keywords=["nonpythonic", "lambda", "assignment expression", "try except expression"],
    url='http://github.com/weakish/nonpythonic',
    author='Jang Rush',
    author_email='weakish@gmail.com',
    license='0BSD',
    py_modules=['nonpythonic'],
    python_requires="~=3.8",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: Public Domain",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Typing :: Typed"])
