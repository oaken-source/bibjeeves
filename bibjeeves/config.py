
'''
This module provides config and cache for bibjeeves.
'''

import os
import json


HOME = os.path.expanduser('~')

CONFIGFILES = [
    HOME + '/.config/bibjeeves/bibjeeves.conf',
    HOME + '/.bibjeeves.conf',
    '/etc/bibjeeves.conf',
]

CACHEFILE = HOME + '/.cache/bibjeeves/bibjeeves.cache'


def _read_config(configfiles):
    '''
    read the config from the config files in order, use the first one you find
    '''
    for configfile in configfiles:
        try:
            with open(configfile) as config:
                return json.loads(config.read())
        except IOError:
            pass

    return dict()


def _read_cache(cachefile):
    '''
    read the cache from the cachefile, if it exists
    '''
    try:
        with open(cachefile) as cache:
            return json.loads(cache.read())
    except IOError:
        pass

    return dict()


def update_cache():
    '''
    this function is called from main before exit to write a changed cach back
    '''
    os.makedirs(os.path.dirname(CACHEFILE), exist_ok=True)
    with open(CACHEFILE, "w") as cache:
        cache.write(json.dumps(CACHE))


CONFIG = _read_config(CONFIGFILES)
CACHE = _read_cache(CACHEFILE)

