import setuptools

setuptools.setup(
    name="samples201",
    version="0.0.1",
    description="A second small example package",
    url="https://github.com/nerdguru/samples201",
    packages=setuptools.find_packages(),
    install_requires=[
       'samples101'
    ],
)
