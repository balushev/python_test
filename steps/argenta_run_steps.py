# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 12:10:08 2022

@author: bbalushev
"""

from behave import step


@step(u'Log in to the application')
def step_impl(context: object) -> None:
    context.web.window_maximize()
    context.web.fill_field(locator='login_username', text=context.env['login_username'], encrypted=True)
    context.web.fill_field(locator='login_password', text=context.env['login_password'], encrypted=True)
    context.web.click_on_element(locator='login_button')


@step(u'Select a distributor with id {number}')
def step_impl(context: object, number: str) -> None:
    context.web.verify_element_not_present(locator='loading_page_element')

    if number.isnumeric():
        context.web.fill_field(locator='distributor_search_page_distributor_id_field', text=number)
        context.web.click_on_element(locator='distributor_search_page_distributor_button_search')

    context.web.verify_element_not_present(locator='loading_page_element')
    context.web.click_on_element(locator='distributor_search_page_distributor_id_tuple', list_index=0)
    context.web.click_on_element(locator='distributor_search_page_distributor_button_ok')
