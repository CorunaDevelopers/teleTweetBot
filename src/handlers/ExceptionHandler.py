#!/usr/bin/env python
# _*_ coding:utf-8 _*

import inspect


class ExceptionHandler:
    @staticmethod
    def handle_exception(ex, exit_program):
        print '[!]Exception: {0} {1}'.format(inspect.stack()[1][3], ex)

        if exit_program:
            exit(0)
