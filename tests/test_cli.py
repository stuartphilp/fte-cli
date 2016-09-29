"""Tests for our main FTE CLI module."""


from subprocess import PIPE, Popen as popen
from unittest import TestCase

from fte import __version__ as VERSION


class TestHelp(TestCase):
    def test_returns_usage_information(self):
        output = popen(['fte', '-h'], stdout=PIPE).communicate()[0]
        self.assertTrue('Usage:' in output)

        output = popen(['fte', '--help'], stdout=PIPE).communicate()[0]
        self.assertTrue('Usage:' in output)


class TestVersion(TestCase):
    def test_returns_version_information(self):
        output = popen(['fte', '--version'], stdout=PIPE).communicate()[0]
        self.assertEqual(output.strip(), VERSION)
