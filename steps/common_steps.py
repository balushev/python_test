# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 09:29:38 2022

@author: bbalushev
"""

import re
import time
from behave import step


def step_name_convertor(step_name: str) -> str:
    """ This function normalized the step name """
    spaces_regex = u'[^\S]+'
    underscore_regex = u'^_|_$'

    spaces_normalized = re.sub(spaces_regex, '_', step_name.replace('=>', ' ').replace('"', ' ').lower())
    return re.sub(underscore_regex, '', spaces_normalized)


@step(u'Set resource name for locators {name}')
def step_impl(context: object, name: str) -> None:
    context.web.resource_name_for_locators = step_name_convertor(name)


@step(u'Choose {option} for {dropdown_name} drop-down menu')
def step_impl(context: object, option: str, dropdown_name: str) -> None:

    dropdown_lists = context.web.fetch_element_from_vendor_locators('dropdown_lists')
    context.web.verify_element_not_present(locator='loading_page_element')

    dropdown_key = step_name_convertor(dropdown_name)
    option_lowercase = option.lower().replace('"', '')

    if 'do not execute' in option_lowercase:
        pass
    else:
        if option_lowercase in dropdown_lists[dropdown_key]:
            option_index = dropdown_lists[dropdown_key].index(option_lowercase)
            context.web.click_on_element(locator=f'{dropdown_key}_dropdown')
            context.web.click_on_element(locator=f'{dropdown_key}_dropdown_tuple', list_index=option_index)
            if hasattr(context, 'records_dict'):
                context.records_dict[context.records_marker_name].append(option)

        else:
            raise Exception(f'The {option} is not an existing option')


@step(u'Choose {option} for {option_name} options area')
def step_impl(context: object, option: str, option_name: str) -> None:

    options_area_lists = context.web.fetch_element_from_vendor_locators('options_area_lists')
    context.web.verify_element_not_present(locator='loading_page_element')

    options_area_key = step_name_convertor(option_name)
    option_lowercase = option.lower().replace('"', '')

    if 'do not execute' in option_lowercase:
        pass
    else:
        if option_lowercase in options_area_lists[options_area_key]:
            option_index = options_area_lists[options_area_key].index(option_lowercase)
            context.web.click_on_element(locator=f'{options_area_key}_options_tuple', list_index=option_index)
            if hasattr(context, 'records_dict'):
                context.records_dict[context.records_marker_name].append(option)

        else:
            raise Exception(f'The {option} is not an existing option')


@step(u'Click {element_name}')
def step_impl(context: object, element_name: str) -> None:
    context.web.verify_element_not_present(locator='loading_page_element')

    if 'do not execute' in element_name:
        pass
    else:
        context.web.click_on_element(locator=step_name_convertor(element_name))


@step(u'Fill {data} in {field_name} field')
def step_impl(context: object, data: str, field_name: str) -> None:
    context.web.verify_element_not_present(locator='loading_page_element')

    if 'do not execute' in data:
        pass
    else:
        context.web.fill_field(locator=f'{step_name_convertor(field_name)}_input', text=data)
        if hasattr(context, 'records_dict'):
            context.records_dict[context.records_marker_name].append(data)


@step(u'Fill {data} in {field_name} field and press enter')
def step_impl(context: object, data: str, field_name: str) -> None:
    context.web.verify_element_not_present(locator='loading_page_element')

    if 'do not execute' in data:
        pass
    else:
        context.web.fill_field(locator=f'{step_name_convertor(field_name)}_input', text=data, press_enter=True)
        if hasattr(context, 'records_dict'):
            context.records_dict[context.records_marker_name].append(data)


@step(u'Wait for {element}')
def step_impl(context: object, element: str) -> None:
    context.web.verify_element_not_present(locator='loading_page_element', timeout=30)
    context.web.verify_element_present(locator=step_name_convertor(element))


@step(u'Verify {element} contains {text} text')
def step_impl(context: object, element: str, text: str) -> None:
    context.web.verify_element_not_present(locator='loading_page_element')
    if re.match(u'\[(.*?)\]', text):
        marker_list = text.replace('[', '').replace(']', '').replace('"', '').split(',')
        for marker in marker_list:
            for recorded_parameter in context.records_dict[marker]:
                context.web.verify_element_text(locator=step_name_convertor(element), text=recorded_parameter.replace('"', ''), contains_in_text=True)

    else:
        context.web.verify_element_text(locator=step_name_convertor(element), text=text.replace('"', ''), contains_in_text=True)


@step(u'Verify {element} have {text} text')
def step_impl(context: object, element: str, text: str) -> None:
    context.web.verify_element_not_present(locator='loading_page_element')
    context.web.verify_element_text(locator=step_name_convertor(element), text=text.replace('"', ''))


@step(u'Pause for {number_str} seconds')
def step_impl(context: object, number_str: str) -> None:
    try:
        number = int(number_str)
    except Exception as e:
        raise Exception(e)

    time.sleep(number)


@step(u'Pause')
def step_impl(context: object) -> None:
    time.sleep(1)


@step(u'Error')
def step_impl(context: object) -> None:
    time.sleep(3)
    assert False, "For demonstration purposes, this test failed!"


@step(u'Start recording')
def step_impl(context: object) -> None:
    context.records_dict = {}
    context.records_marker_name = 'unmarked'
    context.records_dict[context.records_marker_name] = []


@step(u'Stop recording')
def step_impl(context: object) -> None:
    try:
        del context.records_dict
    except Exception as e:
        print(e)


@step(u'Marking records with {marker_name}')
def step_impl(context: object, marker_name: str) -> None:
    if hasattr(context, 'records_dict'):
        context.records_marker_name = marker_name.lower()
        if hasattr(context, f'records_dict'):
            if context.records_marker_name in context.records_dict.keys():
                pass
            else:
                context.records_dict[context.records_marker_name] = []
    else:
        raise Exception('First, you need to start recording !!!')


@step(u'Unmarked records')
def step_impl(context: object) -> None:
    if hasattr(context, 'records_dict'):
        context.records_marker_name = 'unmarked'
    else:
        raise Exception('First, you need to start recording !!!')

