# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 17:44:09 2021

@author: bbalushev
"""


import js2py


# ================================ Executing javascript function ================================
def js_to_python(js_context: str) -> None:
    """js_to_python function execute javascript commands

        Function parameters:
            js_context -> contains javascript command which must be executed

        Return value -> None

    """

    return js2py.eval_js(js_context)
