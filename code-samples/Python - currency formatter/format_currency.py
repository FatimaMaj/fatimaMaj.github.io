def format_currency(number):
    # First turn the number into a string, so that we can easily access the separate digits: 123456.78 -> "123456.78"
    number_string = str(number)

    # if number is integer add ".00" to the end of integer
    if '.' not in number_string:
        number_string += ".00"
    # if number is float round the float two digits after the decimal point
    else:
        number_string = str(round(number, 2))
    # separate the number to 'before' and 'after' decimal point
    before_point = number_string.split(".", 1)[0]
    after_point = number_string.split(".", 1)[1]

    if (len(after_point) == 1):
        after_point = after_point + "0"

    # Create an empty string that we will gradually add characters to and return at the end.
    result = ''

    current_position = 0
    # Loop through every digit in the string.
    # Loop walk through the before_point digits from right to the left (reverse direction)
    for i in reversed(range(len(before_point))):
        # Add the digit to the result string.
        result = before_point[i] + result

        # we need current_position to figure out where to put comma (every three digit)
        current_position += 1
        # In the following condition add commas:
        # If the current_position is divisible by three (3, 6, 9, etc.), add a comma as well.
        # if loop still not in the the first index (first digit)
        if (current_position % 3 == 0 and i != 0):  # i != first_index
            result = ','+result

    result += '.' + after_point

    return result
