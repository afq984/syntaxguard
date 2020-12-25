import sys
import re
import unittest


class TestVersionChecks(unittest.TestCase):
    def assertLooseMessage(self, actual, expected):
        expected_re = re.compile(r'.+'.join(map(re.escape, expected.split())))
        self.assertTrue(
            re.search(expected_re, actual) is not None,
            "%r doesn't contains message %r" % (actual, expected)
        )

    def test27_(self):
        if sys.version_info[:2] == (2, 7):
            import py27_
        else:
            with self.assertRaises(SyntaxError) as ctx:
                import py27_
            self.assertLooseMessage(ctx.exception.text, 'Please use Python 2.7')

    def test30(self):
        if sys.version_info >= (3, 0):
            import py30
        else:
            with self.assertRaises(SyntaxError) as ctx:
                import py30
            self.assertLooseMessage(ctx.exception.text, 'Please use Python 3.0 or later')

    def test33(self):
        if sys.version_info >= (3, 3):
            import py33
        else:
            with self.assertRaises(SyntaxError) as ctx:
                import py33
            self.assertLooseMessage(ctx.exception.text, 'Please use Python 3.3 or later')

    def test35(self):
        if sys.version_info >= (3, 5):
            import py35
        else:
            with self.assertRaises(SyntaxError) as ctx:
                import py35
            self.assertLooseMessage(ctx.exception.text, 'Please use Python 3.5 or later')

    def test36(self):
        if sys.version_info >= (3, 6):
            import py36
        else:
            with self.assertRaises(SyntaxError) as ctx:
                import py36
            self.assertLooseMessage(ctx.exception.text, 'Please use Python 3.6 or later')

    def test38(self):
        if sys.version_info >= (3, 8):
            import py38
        else:
            with self.assertRaises(SyntaxError) as ctx:
                import py38
            self.assertLooseMessage(ctx.exception.text, 'Please use Python 3.8 or later')

    def test39(self):
        if sys.version_info >= (3, 9):
            import py39
        else:
            with self.assertRaises(SyntaxError) as ctx:
                import py39
            self.assertLooseMessage(ctx.exception.text, 'Please use Python 3.9 or later')


if __name__ == '__main__':
    unittest.main()
