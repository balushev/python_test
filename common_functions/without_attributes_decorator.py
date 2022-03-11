# -*- coding: utf-8 -*-
"""
Created on Sun Jan  2 12:54:23 2022

@author: bbalushev
"""

from data_files.without_attributes import *


class WithoutAttributesDecorator:
    """ WithoutAttributesDecorator class create a new class using some base class but without some class attributes """

    def __init__(self, parent_class):
        """ Constructor method

            Method parameters:
              parent_class -> contains parent class reference

            Return value -> None

       """

        self.parent_class = parent_class
        self.parent_class_list = []

        for index in dir(parent_class):
            if '__' not in index:
                self.parent_class_list.append(index)

    def __call__(self, child_class: object) -> object:
        """ Special(Magic) method

            Method parameters:
              child_class -> contains child class reference

            Return value -> None

       """

        child_class_list = []

        for index in dir(child_class):
            if '__' not in index:
                child_class_list.append(index)

        without_attr_list = risk_dict[child_class.__name__]
        inheritance_attributes_list = list(set(self.parent_class_list) - set(without_attr_list))

        for index in inheritance_attributes_list:
            attr = getattr(self.parent_class, index)
            setattr(child_class, index, attr)

        return child_class
