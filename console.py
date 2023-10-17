#!/usr/bin/python3
"""Air BnB console application."""
import cmd


class HBNBCommand(cmd.Cmd):
    """Airbnb command interpretor."""
    prompt = "(hbnb) "

    def do_EOF(self, line):
        """Hnadle end of file maker."""
        return True

    def do_quit(self, line):
        """Quit programm."""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
