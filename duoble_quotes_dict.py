import json
import ast

class doubleQuoteDict(dict):
    def __str__(self):
        return json.dumps(self)

    # def __repr__(self):
    #     return json.dumps(self)

# couples = [
#            ['jack', 'ilena'],
#            ['arun', 'maya'],
#            ['hari', 'aradhana'],
#            ['bill', 'samantha']]
couples = {'TP_Finance': {'Department': {'Default_value': 'IT-Security', 'Required': '', 'Placeholder': 'Enter valid department', 'options': ['IT-Security', 'IT-Infrastructure'], 'data_type': 'list'}, 'Date of Joining': {'Default_value': '', 'Required': '', 'Placeholder': 'Enter valid date', 'options': '', 'data_type': 'date'}, 'Designation': {'Default_value': 'CEO', 'Required': 1, 'Placeholder': 'Enter valid designation', 'options': '', 'data_type': 'text'}}, 'TP_Corporate': {'Department': {'Default_value': 'IT-Security', 'Required': '', 'Placeholder': 'Enter valid department', 'options': ['IT-Security', 'IT-Infrastructure'], 'data_type': 'list'}, 'Date of Joining': {'Default_value': '', 'Required': '', 'Placeholder': 'Enter valid date', 'options': '', 'data_type': 'date'}, 'Designation': {'Default_value': 'CEO', 'Required': 0, 'Placeholder': 'Enter valid designation', 'options': '', 'data_type': 'text'}}}
pairs = doubleQuoteDict(couples)
print type(json.dumps(pairs['TP_Finance']))
