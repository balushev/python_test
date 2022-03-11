# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 16:40:56 2021

@author: bbalushev
"""

from jsonschema import validate


# ============================= JSON schema validator function =============================
def validate_schema(json_body: object, json_schema: dict) -> None:
    """ validate_schema function compare json_body with json_schema

        Function parameters:
            json_body -> contains json body which must be validated
            json_schema -> contains a json schema for validation

        Return value -> None

    """
    validate(json_body, json_schema)
