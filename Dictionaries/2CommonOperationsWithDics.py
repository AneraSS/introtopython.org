# adding:
python_words = {}
python_words['key1'] ='value1'

# modifying values:
python_words['key1'] = 'new_value1'

# modifying values:
python_words['new_key1'] = python_words['key1'] # you make a copy with a new key
del python_words['key1'] # here you delete the previous (old) key

# Removing key-value pairs:
del python_words['key1']
