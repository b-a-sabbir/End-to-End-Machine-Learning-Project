from us_visa.logger import logging
from us_visa.exception import USvisaException
import sys

try:
    r = 3/0
    print(r)
except Exception as e:
    raise USvisaException(e, sys) 

# logging.info("This is an info message 02")

