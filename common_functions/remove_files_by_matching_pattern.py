# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 11:44:40 2021

@author: bbalushev
"""

import os
import fnmatch


class RemoveFilesByMatchingPattern:
    """ RemoveFilesByMatchingPattern contains a method to remove files by matching pattern
        on the specific directory
    """

    # ================================ Initialization method ================================
    def __init__(self, dir_path: str) -> None:
        """ Constructor method

            Method parameters:
                dir_path -> contains directory path where we want to remove files

            Return value -> None

        """
        self.dir_path = dir_path

    # ================================ Remove files method ================================
    def remove_files(self, pattern: str) -> list:
        """ remove_files method remove files from the specific directory by matching pattern

            Method parameters:
                pattern -> contains the pattern which we will use to remove the files

            Return value -> a list of filenames that have not been removed

        """

        list_of_files_which_was_not_removed = []

        for parent_dir, _, filenames in os.walk(self.dir_path):
            for filename in fnmatch.filter(filenames, pattern):
                try:
                    os.remove(os.path.join(parent_dir, filename))
                except Exception as e:
                    print("An exception occurred: ", e)
                    print("Error while deleting file : ", os.path.join(parent_dir, filename))
                    list_of_files_which_was_not_removed.append(os.path.join(parent_dir, filename))

            return list_of_files_which_was_not_removed
