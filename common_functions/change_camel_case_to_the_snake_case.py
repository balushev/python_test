# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 16:40:56 2021

@author: bbalushev
"""

import re


# =========================== Camel case to Snake case convertor function ===========================
def change_camel_case_to_the_snake_case(self, camel_case_string: str) -> str:
    """ change_camel_case_to_the_snake_case function convert 'Camel case' string in to the  'Snake case'

        Function parameters:
            camel case string -> string which will be changed  from 'Camel case' to 'Snake case'

        Return value -> converted string from 'Camel case' to 'Snake case'

    """

    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', camel_case_string)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()
