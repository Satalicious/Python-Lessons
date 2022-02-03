"""
Library providing functions to automatically grade student homeworks.
"""

import doctest
import importlib
import subprocess
import sys
import unittest


class TestCaseWithDoctests(unittest.TestCase):
    """Subclass this Test class if doctests should be checked."""
    def test_doctests(self):
        """Ensure doctests are present and pass."""
        from os.path import splitext
        module = importlib.import_module(splitext(self.target)[0])
        r = doctest.testmod(module)
        self.assertTrue(r.attempted, f'{self.target} does not have a doctest')
        self.assertFalse(r.failed, f'{self.target} contains failing doctests')


def grade_by_io(script, in_data, expected, points=1):
    """Grade a submitted example."""
    process = subprocess.Popen(["python3", script],
                               stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
    out, err = process.communicate(in_data.encode("utf-8"))
    actual = out.decode("utf-8")
    if expected.split() == actual.split():
        print("{} points for".format(points), script)
        return points
    else:
        print("0 points for", script)
        if err:
            print("error:\n", err.decode('utf-8'))
        else:
            print("actual:\n", actual)
            print("expected:\n", expected)
    return 0


def main():
    print('library only for importing, call')
    print('python3 hw?_grader.py*')
    print('instead')


if __name__ == "__main__":
    sys.exit(main())
