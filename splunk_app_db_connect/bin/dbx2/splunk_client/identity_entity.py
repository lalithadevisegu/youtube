import os, sys
import json
import splunklib.client as client

PATH_IDENTITY_PATH = 'db_connect/dbxproxy/identities/%s'


class IdentityEntity(client.Entity):
    def __init__(self, service, name, **kwargs):
        path = PATH_IDENTITY_PATH % name
        client.Entity.__init__(self, service, path, **kwargs)


