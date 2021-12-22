import setuptools

dependencies = [
    "google-cloud-secret-manager==1.0.0"
]

packages = [
    package for package in setuptools.find_packages() if package.startswith("globalSearch")
]

# Determine which namespaces are needed.
namespaces = ["globalSearch"]
if "globalSearch.utils" in packages:
    namespaces.append("globalSearch.utils")

setuptools.setup(name='globalSearch-utils',
                 version='0.1.0',
                 description='Python global search utilities',
                 author='Philipp Schierz',
                 author_email='philipp.schierz.ext@urban-mobility.io',
                 packages=packages,
                 namespaces=namespaces,
                 install_requires=dependencies
                 )
