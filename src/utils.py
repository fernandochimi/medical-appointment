# coding: utf-8
import os


def import_env_variables(value):
    return os.environ.get(value)


def validate_int_values(value):
    try:
        return int(value)
    except ValueError:
        return False


def error_json(status, msg):
    return {"status": status, "message": msg}
