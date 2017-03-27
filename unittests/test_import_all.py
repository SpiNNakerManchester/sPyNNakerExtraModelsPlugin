import unittest

import spinn_utilities.package_loader as package_loader


class ImportAllModule(unittest.TestCase):

    def test_import_all(self):
        package_loader.load_module("spynnaker_extra_pynn_models",
                                   remove_pyc_files=False)
