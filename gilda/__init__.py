__version__ = '0.6.1'
import logging

logging.basicConfig(format=('%(levelname)s: [%(asctime)s] %(name)s'
                            ' - %(message)s'),
                    level=logging.INFO, datefmt='%Y-%m-%d %H:%M:%S')


logger = logging.getLogger('gilda')


from .api import *
