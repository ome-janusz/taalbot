"""
Custom-defined exceptions.
"""


class Error(Exception):
    pass

class MissingConfigKeyError(Error):
    """
    Exception raised on incomplete/incorrect configuration file

    Attributes:
      parameter -- name of the missing required parameter
    """

    def __init__(self, parameter):
        self.parameter = parameter

    def __str__(self):
        return "Missing required configuration parameter: {}".format(self.parameter)