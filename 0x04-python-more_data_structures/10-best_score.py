#!/usr/bin/python3
def best_score(a_dictionary):
    if isinstance(a_dictionary, dict):
        _key = None
        for k in a_dictionary.keys():
            if _key is None:
                _key = k
            elif a_dictionary[k] > a_dictionary[_key]:
                _key = k
        return _key
