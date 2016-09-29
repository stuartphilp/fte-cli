"""Verify `fte new` subcommand works correctly."""


from subprocess import PIPE, Popen as popen
from unittest import TestCase


class TestNew(TestCase):
    def test_returns_multiple_lines(self):
        output = popen(['fte', 'new'], stdout=PIPE).communicate()[0]
        lines = output.split('\n')
        self.assertTrue(len(lines) != 1)

