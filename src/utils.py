# coding: utf-8
import os


def import_env_variables(value):
    return os.environ.get(value)


def int_values(value):
    try:
        return int(value)
    except ValueError:
        return False
