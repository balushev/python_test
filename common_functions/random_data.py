# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 10:54:52 2021

@author: bbalushev
"""

from random import shuffle
from faker import Faker

faker_obj = Faker(['en_GB'])


# ================================ Rndom phone number function ================================
def phone_number(number_prefix: int = 77, min_limit: int = 10000000, max_limit: int = 99999999) -> str:
    """ phone_number function generates random phone number which start with number_prefix

        Function parameters:
            number_prefix -> contains the prefix of the phone number
            min_limit -> contains min limitation of phone number
            max_limit -> contains max limitation of phone number

        Return value -> randomly generated phone number

    """

    return str(number_prefix) + random_number(min_limit, max_limit)


# ================================ Random number function ================================
def random_number(min_value: int = 10000000, max_value: int = 99999999) -> str:
    """ random_number function generates random number between min_value and max_value

        Function parameters:
          min_value -> contains min limitation of generated number
          max_value -> contains max limitation of generated number

        Return value -> randomly generated number

    """

    return str(faker_obj.random_int(min_value, max_value))


# ================================ Random email function ================================
def email() -> str:
    """ email function generates random email

      Function parameters -> None
      Return value -> randomly generated email

    """

    return faker_obj.email()


# =========================== Random email function (advanced) ===========================
def email_with_added_digits(prefix: str = '', postfix: str = '') -> str:
    """ email_with_added_digits function generates random email and added prefix, postfix and additional digits

        Function parameters:
            prefix -> contains prefix which will be added in to beginning of generated email
            postfix -> contains postfix which will be added after '@' symbol

        Return value -> randomly generated email with additional digits

    """

    email_value = faker_obj.email()
    email_split_arr = email_value.split('@')
    email_postfix = email_split_arr[-1]

    if postfix != '':
        email_postfix = postfix

    return prefix + email_split_arr[0] + '_' + random_number() + '@' + email_postfix


# ================================ Random first name function ================================
def first_name(gender: str = '') -> str:
    """ first_name function generates random first name

        Function parameters:
            gender -> contains the gender of the person whose first name will be generated

        Return value -> randomly generated first name

    """

    if gender.lower() == 'male':
        return faker_obj.first_name_male()
    elif gender.lower() == 'female':
        return faker_obj.first_name_female()
    else:
        return faker_obj.first_name()


# ================================ Random middle name function ================================
def middle_name(gender: str = '') -> str:
    """ middle_name function generates random middle name

        Function parameters:
            gender -> contains the gender of the person whose middle name will be generated

        Return value -> randomly generated middle name

    """

    if gender.lower() == 'male':
        return faker_obj.middle_name_male()
    elif gender.lower() == 'female':
        return faker_obj.middle_name_female()
    else:
        return faker_obj.middle_name()


# ================================ Random last name function ================================
def last_name(gender: str = '') -> str:
    """ last_name function generates random last name

        Function parameters:
            gender -> contains the gender of the person whose last name will be generated

        Return value -> randomly generated last name

    """

    if gender.lower() == 'male':
        return faker_obj.last_name_male()
    elif gender.lower() == 'female':
        return faker_obj.last_name_female()
    else:
        return faker_obj.last_name()


# ================================ Random full name function ================================
def full_name(gender: str = '') -> str:
    """ full_name function generates random full name

        Function parameters:
            gender -> contains the gender of the person whose full name will be generated

        Return value -> randomly generated full name

    """

    if gender.lower() == 'male':
        return faker_obj.name_male()
    elif gender.lower() == 'female':
        return faker_obj.name_female()
    else:
        return faker_obj.name()


# ================================ Random birthday function ================================
def birthday(birthday_format: str = '%Y-%m-%d', min_age: int = 20, max_age: int = 80) -> str:
    """ birthday function generates random birthday date

        Function parameters:
          birthday_format -> contains the format of birthday
          min_age -> contains the minimum age of the person
          max_age -> contains the maximum age of the person

        Return value -> randomly generated birthday date with necessary format

    """

    fake_birthday = faker_obj.date_of_birth(tzinfo=None, minimum_age=min_age, maximum_age=max_age)
    formatted_birthday = fake_birthday.strftime(birthday_format)
    return formatted_birthday


# ================================ Random street function ================================
def street() -> str:
    """ street function generates random street address

        Function parameters -> None
        Return value -> randomly generated street address

    """

    fake_street = str(random_number(1, 999)) + ' ' + faker_obj.street_name()
    return fake_street.replace("'", "")


# ================================ Random town function ================================
def town() -> str:
    """ town function generates random town name

        Function parameters -> None
        Return value -> randomly generated town name

    """

    fake_town = faker_obj.city()
    return fake_town.replace("'", "")


# ================================ Random postcode function ================================
def postcode() -> str:
    """ postcode function generates random postcode

        Function parameters -> None
        Return value -> randomly generated postcode

    """

    return faker_obj.postcode()


# ================================ Random sentence function ================================
def random_sentence(nb_words: int = 5) -> str:
    """ random_sentence function generates a random sentence with a number of words
        equal to the number contained in the 'nb_words' parameter

        Function parameters:
            nb_words -> contains the number of words in our sentence

        Return value -> randomly generated postcode

    """

    return faker_obj.sentence(nb_words, variable_nb_words=True, ext_word_list=None)


# ================================ Random company function ================================
def random_company() -> str:
    """ random_company function generates a random company name

        Function parameters -> None
        Return value -> randomly generated company name

    """

    return faker_obj.company()


# =========================== Random string function (advanced) ===========================
def random_str_zip_by_int_and_str(zip_str: str = 'abcdefgh', zip_num: str = '') -> str:
    """ random_str_zip_by_int_and_str function generates a random string using string
        and number and zips it together

            Function parameters:
                zip_str -> contains a string that will be zipped
                zip_num -> contains a number that will be zipped

            Return value -> randomly generated string

        """

    random_string_list = list(zip_str)

    if zip_num == '':
        random_integer_list = list(random_number())
    else:
        random_integer_list = list(zip_num)

    final_random_string = ''
    shuffle(random_string_list)
    shuffle(random_integer_list)
    edge_list = zip(random_integer_list, random_string_list)

    for tuple_item_1, tuple_item_2 in edge_list:
        final_random_string += tuple_item_1
        final_random_string += tuple_item_2

    return final_random_string
