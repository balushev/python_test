# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 14:48:34 2021

@author: bbalushev
"""


from pywinauto.application import Application


class WinInteractions:
    """ WinInteractions is a class that providing all methods for interacting with Windows app """

    # ================================ Initialization method ================================
    def __init__(self) -> None:
        """ Constructor method

            Method parameters:


            Return value -> None
        """
        self.app = Application()
