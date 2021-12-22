
@staticmethod
def check_dict_has_none_values(dictionary):
    has_none_value = False
    for key, value in dictionary.items():
        if value is None:
            has_none_value = True

    return has_none_value
