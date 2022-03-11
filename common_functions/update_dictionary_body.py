# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 15:30:46 2021

@author: bbalushev
"""

from benedict import benedict


class UpdateDictionaryBody:
    """ UpdateDictionaryBody is a class that merge one dictionary with another """

    # ================================ Initialization method ================================
    def __init__(self, main_dictionary: dict) -> None:
        """ Constructor method

            Method parameters:
                main_dictionary -> dictionary which will be changed

            Return value -> None

        """

        self.dictionary = benedict(main_dictionary)

    # ================================ Dictionary merge method ================================
    def merge_update_dict_with_main_dict(self, update_dictionary: dict) -> None:
        """ merge_update_dict_with_main_dict method merges update dictionary to main dictionary

            Method parameters:
                update_dictionary -> dictionary which will be merged with main_dictionary

            Return value -> None

        """

        self.dictionary.merge(update_dictionary)

    # =========================== Remove keys from dictionary method ===========================
    def remove_multiple_keys_from_the_dict(self, remove_list: list) -> None:
        """ remove_multiple_keys_from_the_dict removes nodes from main_dictionary using remove_list

                Method parameters:
                    remove_list -> list with nodes that must be removed from main_dictionary

                Return value -> None
        """

        self.dictionary.remove(remove_list)
