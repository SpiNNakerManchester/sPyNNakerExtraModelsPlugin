from setuptools import setup

from collections import defaultdict
import os
__version__ = None
exec(open("spynnaker_extra_pynn_models/_version.py").read())
assert __version__

# Build a list of all project modules, as well as supplementary files
main_package = "spynnaker_extra_pynn_models"
data_extensions = {".aplx", ".xml"}
main_package_dir = os.path.join(os.path.dirname(__file__), main_package)
start = len(main_package_dir)
packages = []
package_data = defaultdict(list)
for dirname, dirnames, filenames in os.walk(main_package_dir):
    if '__init__.py' in filenames:
        package = "{}{}".format(
            main_package, dirname[start:].replace(os.sep, '.'))
        packages.append(package)
    for filename in filenames:
        _, ext = os.path.splitext(filename)
        if ext in data_extensions:
            package = "{}{}".format(
                main_package, dirname[start:].replace(os.sep, '.'))
            package_data[package].append("*{}".format(ext))
            break

setup(
    name="sPyNNakerExtraModelsPlugin",
    version=__version__,
    description="Extra models not in PyNN",
    url="https://github.com/SpiNNakerManchester/sPyNNakerExtraModelsPlugin",
    packages=packages, package_data=package_data,
    install_requires=['SpyNNaker >= 1!4.0.0a5, < 1!5.0.0']
)
