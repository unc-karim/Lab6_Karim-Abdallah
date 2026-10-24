from pybuilder.core import init, use_plugin

use_plugin("python.core")
use_plugin("python.unittest")

name = "calculator_Karim_Abdallah"
version = "0.1"
default_task = "run_unit_tests"


@init
def initialize(project):
    project.set_property("dir_source_main_python", "src/main/python")
    project.set_property(
        "dir_source_unittest_python", "tests/unittest/calculator_Karim_Abdallah"
    )
    project.set_property("unittest_module_glob", "test_*")
