import unittest

import {{cookiecutter.module_name.lower().replace(' ', '_').replace('-', '_')}}


class Test{{cookiecutter.module_name.lower().replace(' ', '_').replace('-', '_')|title}}(unittest.TestCase):
    def test_echo(self):
        self.assertEqual('foo', {{cookiecutter.module_name.lower().replace(' ', '_').replace('-', '_')}}.echo('foo'))
