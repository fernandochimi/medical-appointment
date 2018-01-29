# coding: utf-8
import os
import datetime
import decimal
import json


def import_env_variables(value):
    return os.environ.get(value)


def validate_int_values(value):
    try:
        return int(value)
    except ValueError:
        return False


def error_json(status, msg):
    return {"status": status, "message": msg}


def json_encoder(obj):
    if isinstance(obj, datetime.time):
        return obj.isoformat()
    if isinstance(obj, datetime.datetime):
        return obj.isoformat()
    if isinstance(obj, decimal.Decimal):
        return float(obj)


def json_handler(result):
    return json.loads(json.dumps(result, default=json_encoder))


def _format_string_to_datetime(date):
    return datetime.datetime.strptime(date, "%Y-%m-%dT%H:%M:%S")
