# -- BEGIN LICENSE BLOCK ----------------------------------------------

# catmux
# Copyright (C) 2018  Felix Mauch
# MIT License
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# -- END LICENSE BLOCK ------------------------------------------------

"""A split in a tmux session"""

import libtmux

from catmux.utils import parse_commands


class Split(object):

    """A split is a pane where commands can be executed"""

    def __init__(self, *args):
        """TODO: to be defined1."""
        self.commands = list()

        if args is not None:
            self.commands = parse_commands(args)

    def debug(self, name="", prefix=""):
        """Prints all information about this window"""
        print(prefix + "- Split " + name + ":")
        if hasattr(self, "commands"):
            print(prefix + "  commands: ")
            print("\t- " + "\n\t- ".join(getattr(self, "commands")))

    def run(self, parent_pane: libtmux.Pane):
        "Executes all configured commands" ""
        for command in self.commands:
            parent_pane.send_keys(command)
