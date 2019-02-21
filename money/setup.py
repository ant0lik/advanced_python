import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="moneyor",
    version='0.0.1',
    author="Anatol",
    author_email="author@example.com",
    description="Money Handling Application",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/ant0lik/advanced_python',
    packages=setuptools.find_packages(),
)
