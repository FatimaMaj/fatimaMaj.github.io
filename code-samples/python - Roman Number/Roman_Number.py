
def decimal_to_roman_converter(integer):
    romans = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    decimals = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    
    roman_string = ''
    # loop through decimals list
    romans_and_decimals = list(zip(romans, decimals))
    for roman, decimal in romans_and_decimals:
        # find the highest decimal value (from decimals list) that is less than or equal to the integer (The number that we want to convert to roman)
        # for example if we want to convert 36 to roman number:
        # 36-10 = 26; 26-10 = 16; 16-10 = 6
        # in this case we need to subtract the integer(i,e 36) several times from 10, utill it will be less than 10. after that the loop, goes through to the next value in decimals which is 9
        while decimal <= integer:
            # subtract decimal value from integer
            integer = integer - decimal
            roman_string = roman_string + roman
    return roman_string 

# Code review comments:
#
# 1.
# 
# I think we can simplify a little with startswith:
# 
# https://www.tutorialspoint.com/python/string_startswith.htm
# 
# Then we should be able to remove the first_component_of_input variable and use "roman" instead.
# 
# 2. If we use "break", we don't need this line:
#
# first_component_of_input = ''
# 
# 3. Usually we simplify this:
# 
# decimal_int = decimal + decimal_int
# 
# to this:
# 
# decimal_int += decimal
# 
# 4. Some variables can be renamed to be more distinct. For example:
# 
#             roman -> roman_part
# romanNumber_input -> roman
#           decimal -> decimal_part
#       decimal_int -> decimal

def roman_to_decimal_converter(roman):
    romans = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    decimals = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    
    decimal = 0
    # loop through romans list
    romans_and_decimals = list(zip(romans, decimals))
    for roman_part, decimal_part in romans_and_decimals:
        # for example roman is: MCMXCVI    
        while roman is not None or roman_part == roman:
            # get the first element from romans list which 'M'
            # if element in roman_part is equal to the roman
            if roman.startswith(roman_part):
                # get decimal related to that roman number and added to the previouse decimal
                decimal += decimal_part
                # remove the first component from input
                roman = roman[len(roman_part): len(roman)]
            # else if roman_part was not matched with romans, move to the next element in the roman list    
            else: 
                break
        
    return decimal 


# class RomanTests(unittest.TestCase):
#     def test_three(self):
#         integer = 3
#         roman_number = decimal_to_roman_converter(integer)
#         self.assertEqual('III', roman_number)
    
#     def test_four_need_subtract(self):
#         integer = 4
#         roman_number = decimal_to_roman_converter(integer)
#         self.assertEqual('IV', roman_number)
    
#     def test_9(self):
#         integer = 9
#         roman_number = decimal_to_roman_converter(integer)
#         self.assertEqual('IX', roman_number)
    
#     def test_58(self):
#         integer = 58
#         roman_number = decimal_to_roman_converter(integer)
#         self.assertEqual('LVIII', roman_number)
    
#     def test_1994(self):
#         integer = 1994
#         roman_number = decimal_to_roman_converter(integer)
#         self.assertEqual('MCMXCIV', roman_number)

#     def test_more_than_3999(self):
#         integer = 4500
#         roman_number = decimal_to_roman_converter(integer)
#         self.assertEqual('MMMMD', roman_number)

# #testing convert roman to decimal
#     def test_XXXVI(self):
#         roman_string = 'XXXVI'
#         decimal = roman_to_decimal_converter(roman_string)
#         self.assertEqual(36, decimal)
    
#     def test_MMXII(self):
#         roman_string = 'MMXII'
#         decimal = roman_to_decimal_converter(roman_string)
#         self.assertEqual(2012, decimal)
    
#     def test_MCMXCVI(self):
#         roman_string = 'MCMXCVI'
#         decimal = roman_to_decimal_converter(roman_string)
#         self.assertEqual(1996, decimal)

#         # Extra tests after version 8: every Roman numeral up to 4999, on a separate line in a text file.
#     def test_file(self):
#         path = os.path.dirname(__file__) + "/first-4999.txt"
#         with open(path) as f:
#             lines = f.readlines()
#             for index, line in enumerate(lines):
#                 expected = line.strip()
#                 # creates a test (a "subtest" in Python) for each of them
#                 # By passing the line number (+1) into the Roman function and checking that the result is the same as the line in the file (which I downloaded from the internet)
#                 result_to_roman = decimal_to_roman_converter(index + 1)
                
#                 with self.subTest():
#                     self.assertEqual(result_to_roman, expected)

#                 result_to_decimal = roman_to_decimal_converter(line)
#                 with self.subTest():
#                     self.assertEqual(result_to_decimal, index + 1)

# unittest.main() 