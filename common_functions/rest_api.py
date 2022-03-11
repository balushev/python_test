# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 17:08:27 2022

@author: bbalushev
"""


import json
import requests
from pydoc import locate


def rest_api(url: str, headers=None, params=None, json_body=None, request_method: str = 'GET', status_code: int = 200,
             with_options: bool = True) -> dict:
    """ rest_api function returns json response

        Method parameters:
             url -> contains Host url
             headers -> contain header parameters
             params -> contains url parameters
             json_body -> contains JSON body for our request
             request_method -> contains request method
             status_code -> contains expected status code
             with_options -> flag for using options request before real

        Return value -> result from our request execution

    """

    if json_body is not None:
        json_body = json.loads(json.dumps(json_body))

    method = request_method.upper()

    if method in ['GET', 'OPTIONS', 'POST', 'PATCH', 'DELETE']:
        if with_options:
            try:
                response = requests.request(method='OPTIONS', url=url, headers=headers, params=params, json=json_body)
            except Exception as e:
                print(e)

            assert response.status_code == 200, \
                f"Response code for OPTIONS was {response.status_code}"

        try:
            response = requests.request(method=method, url=url, headers=headers, params=params, json=json_body)
        except Exception as e:
            print(e)
    else:
        raise Exception('Unsupported method !!!')

    assert response.status_code == status_code, \
        f"Response code on {request_method} was {response.status_code}"

    # validate(response.json(), json_schema[api_method])

    return response.json()
