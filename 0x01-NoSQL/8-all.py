#!/usr/bin/env python3
"""task 8"""


def list_all(mongo_collection):
    """
    that lists all documents in a collection
    """
    return mongo_collection.find()
