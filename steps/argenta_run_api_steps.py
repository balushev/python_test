# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 12:10:08 2022

@author: bbalushev
"""

import json
from behave import step
from common_functions.rest_api import rest_api
from common_functions.random_data import random_number


def access_header(context: object, header: dict) -> dict:
    header['x-auth-username'] = context.crypto.decrypt(context.env['auth_username'])
    header['x-api-key'] = context.crypto.decrypt(context.env['auth_key'])

    return header


@step(u'Get distributor')
def step_impl(context: object) -> None:
    response_body = rest_api(url=f"{context.env['API_URL']}/distributors", headers=access_header(context, {}))

    if context.table[0][0].lower() == 'random':
        position = random_number(min_value=0, max_value=int(response_body['_count']) - 1)
    else:
        position = int(context.table[0][0])

    if type(response_body['_links']['item']) is list:
        context.distributor_id = response_body['_links']['item'][position]['summary']['distributor_detail:identifier']
    elif type(response_body['_links']['item']) is dict:
        context.distributor_id = response_body['_links']['item']['summary']['distributor_detail:identifier']
    else:
        raise Exception("Distributors das not exist !!!")


@step(u'Create quotes')
def step_impl(context: object) -> None:
    attr_arr = getattr(context, "_stack", None)
    json_body = json.loads(attr_arr[0]["text"])

    response_body = rest_api(url=f"{context.env['API_URL']}/quotes", headers=access_header(context, {}),
                             json_body=json_body, request_method='POST', status_code=201)

    context.quote_uri = response_body['_links']['self']['href']
    context.quote_identifier = response_body['quote:identifier']


@step(u'Get owner')
def step_impl(context: object) -> None:
    response_body = rest_api(url=f"{context.quote_uri}/owners", headers=access_header(context, {}))

    if context.table[0][0].lower() == 'random':
        position = random_number(min_value=0, max_value=int(response_body['_count']) - 1)
    else:
        position = int(context.table[0][0])

    if type(response_body['_links']['item']) is list:
        context.owner_uri = response_body['_links']['item'][position]['href']
    elif type(response_body['_links']['item']) is dict:
        context.owner_uri = response_body['_links']['item']['href']
    else:
        raise Exception("Owner das not exist !!!")


@step(u'Get person')
def step_impl(context: object) -> None:
    params = {}

    if 'skip' not in context.table[0][0]:
        params['person:first_name_normalized'] = context.table[0][0]

    if 'skip' not in context.table[0][1]:
        params['person:last_name'] = context.table[0][1]

    if 'skip' not in context.table[0][2]:
        params['person:client_number'] = context.table[0][2]

    if 'skip' not in context.table[0][3]:
        params['person:birth_date'] = context.table[0][3]

    # params['person:referential'] = False

    response_body = rest_api(url=f"{context.env['API_URL']}/persons", headers=access_header(context, {}), params=params)

    if context.table[0][4].lower() == 'random':
        position = random_number(min_value=0, max_value=int(response_body['_count']) - 1)
    else:
        position = int(context.table[0][4])

    if type(response_body['_links']['item']) is list:
        context.person_uri = response_body['_links']['item'][position]['href']
        context.person_display_id1 = response_body['_links']['item'][position]['summary']['person:display_id1']
    elif type(response_body['_links']['item']) is dict:
        context.person_uri = response_body['_links']['item']['href']
        context.person_display_id1 = response_body['_links']['item']['summary']['person:display_id1']
    else:
        raise Exception("Person das not exist !!!")


@step(u'Update quote owner person link')
def step_impl(context: object) -> None:
    attr_arr = getattr(context, "_stack", None)
    body = {"quote_owner:person_link": context.person_uri}
    json_body = json.loads(body)

    response_body = rest_api(url=context.owner_uri, headers=access_header(context, {}),
                             json_body=json_body, request_method='PATCH')
