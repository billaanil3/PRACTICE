import collections
def nested_dict_iter(nested):
    for key, value in nested.iteritems():
        if isinstance(value, collections.Mapping):
            for inner_key, inner_value in nested_dict_iter(value):
                yield inner_key, inner_value
        else:
            yield key, value

value = nested_dict_iter({'label': {'incident': {'Recipient Type': 'Recipient/Respondent Entity', 'Recipient': 'SCI Managing Director/Contact'}}})
print list(value)