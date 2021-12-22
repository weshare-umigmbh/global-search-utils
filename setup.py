import setuptools

dependencies = [
    "google-cloud-secret-manager==1.0.0"
]

packages = [
    package for package in setuptools.find_packages() if package.startswith("globalsearch")
]

# Determine which namespaces are needed.
namespaces = ["globalsearch"]
if "globalsearch.utils" in packages:
    namespaces.append("globalsearch.utils")

setuptools.setup(name='globalsearch-utils',
                 version='0.1.0',
                 description='Python global search utilities',
                 author='Philipp Schierz',
                 author_email='philipp.schierz.ext@urban-mobility.io',
                 packages=packages,
                 namespaces=namespaces,
                 install_requires=dependencies
                 )
