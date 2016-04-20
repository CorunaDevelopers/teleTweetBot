#!/usr/bin/env python
# _*_ coding:utf-8 _*

import inspect
import os


class ExceptionHandler:
    @staticmethod
    def handle_exception(ex, exit_program):
        calling_module = os.path.basename(inspect.stack()[1][1])
        calling_method = inspect.stack()[1][3]
        print '[!]Exception in {0}${1}: {2}'.format(calling_module, calling_method, ex)

        if exit_program:
            exit(0)
