"""
rediswrapper
------------
A pythonic wrapper for redis client.

Author: Frost Ming<mianghong@gmail.com>
"""

__version__ = "0.3.0"
__all__ = ["RedisDict"]

from .storage import RedisDict
