import unittest

import {{cookiecutter.module_name}}


class Test{{cookiecutter.module_name|title}}(unittest.TestCase):
    def test_echo(self):
            self.assertEqual('foo', {{cookiecutter.module_name}}.echo('foo'))
