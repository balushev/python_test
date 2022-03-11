# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 14:45:18 2021

@author: bbalushev
"""

from cx_Oracle import connect
from common_functions.crypto import Crypto


class OracleDBInteractions:
    """ OracleDBInteractions class provides all the necessary methods for interactions with Oracle DB """

    cursor = None

    # ================================ Initialization method ================================
    def __init__(self, connection_string: bytes) -> None:
        """ Constructor method

            Method parameters:
               connection_string -> contains connection string for OracleDB

            Return value -> None

        """

        self.crypto = Crypto()
        self.client = connect(self.crypto.decrypt(connection_string))

    # ================================ Execution script method ================================
    def execute_script(self, script: str = '') -> None:
        """ execute_script method execute a script and store result in cursor attribute

            Method parameters:
               script -> contains the script which we want to be executed

            Return value -> None

        """

        self.cursor = self.client.cursor()
        self.cursor.execute(script)

        if any(x in script.lower() for x in ('insert', 'update', 'delete')):
            self.client.commit()

    # ================================ Close cursor method ================================
    def close_cursor(self) -> None:
        """ close_cursor method closing the cursor attribute

            Method parameters -> None
            Return value -> None

        """

        self.cursor.close()
