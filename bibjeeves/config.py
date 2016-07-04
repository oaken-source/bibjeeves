
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
    for configfile in configfiles:
        try:
            with open(configfile) as f:
                return json.loads(f.read())
        except:
            pass

    return dict()


def _read_cache(cachefile):
    try:
        with open(cachefile) as f:
            return json.loads(f.read())
    except:
        pass

    return dict()


def update_cache():
    os.makedirs(os.path.dirname(CACHEFILE), exist_ok=True)
    with open(CACHEFILE, "w") as f:
        f.write(json.dumps(CACHE))


CONFIG = _read_config(CONFIGFILES)
CACHE = _read_cache(CACHEFILE)

