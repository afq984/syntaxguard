import pathlib


versions = []
for file in pathlib.Path().glob('py??.py'):
    major, minor = map(int, file.name[2:-3])
    versions.append((major, minor))


versions.sort()


header = '''import sys
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
'''


template = '''
    def testXY(self):
        if sys.version_info >= (X, Y):
            import pyXY
        else:
            with self.assertRaises(SyntaxError) as ctx:
                import pyXY
            self.assertLooseMessage(ctx.exception.text, 'Please use Python X.Y')
'''


footer = '''

if __name__ == '__main__':
    unittest.main()
'''


print(end=header)
for major, minor in versions:
    print(end=template.replace('X', str(major)).replace('Y', str(minor)))
print(end=footer)
