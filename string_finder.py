"""String Finder"""

class Finder:
    """
    To find a string match in array of strings

    :param string_list: (list) List of the strings
    """
    def __init__(self, string_list):
        if not isinstance(string_list, list):
            print("Invalid argument passed. Required datatype is list not {}".format(type(string_list)))
        self.string_list = string_list

    def find(self, test_string):
        """
        Used to find the strings having same characters from the string_list
        :param test_string: (str) String to be matched
        :return: (list) List of matching strings
        """
        if not isinstance(test_string, str):
            print("Invalid argument passed. Required datatype is string not {}".format(type(test_string)))

        test_string_len = len(test_string)

        test_string_ascii = 0
        for character in test_string:
            test_string_ascii += ord(character)

        matched_strings = []
        for string in self.string_list:
            if len(string) != test_string_len:
                continue
            ascii_value = 0
            for character in string:
                ascii_value += ord(character)
            if ascii_value == test_string_ascii:
                matched_strings.append(string)

        return matched_strings


finder_obj = Finder(['asd', 'asdd', 'fre', 'das', 'sad ', 'sddda'])
matched_string = finder_obj.find('sad')
print(matched_string)

"""
Assumptions
1. String could be case insensitive.
2. String could contain spaces.
3. Character frequency should also be same. As asdd is not returned in the given example
"""
