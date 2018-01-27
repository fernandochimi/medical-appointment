# coding: utf-8
import os


def import_env_variables(value):
    return os.environ.get(value)
