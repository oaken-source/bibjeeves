
'''
This module provides access classes to research paper databases.
'''

import requests

from bibjeeves.models import Document


class AbstractProvider(object):
    '''
    the provider interface - to be extended by actual providers
    '''

    def query(self, text=None, title=None, author=None):
        raise NotImplementedError('this method must be implemented in the provider')


class CiteSeerxProvider(AbstractProvider):
    '''
    this provider queries CiteSeerx for the requested documents
    '''

    def query(self, text=None, title=None, author=None):
        args = []
        if text is not None:
            args.append('text:(%s)' % text)
        if title is not None:
            args.append('title:(%s)' % title)
        if author is not None:
            args.append('author:(%s)' % author)
        q = ' AND '.join(args)
        r = requests.get('http://citeseerx.ist.psu.edu/search', params=dict(q=q))
