from us_visa.logger import logging
import sys

# logging.info("Welcome to custom log")

from us_visa.exception import USvisaException

try:
    a=1/0
except Exception as e:
    raise USvisaException(e,sys)