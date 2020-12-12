###################################
# Return a formatted phone number #
###################################
def format_phone(phone):
    # Slice out Area Code
    area_code_slice = slice(3)
    area_code = phone[area_code_slice]

    # Slice out Prefix
    prefix_slice = slice(3, 6)
    prefix = phone[prefix_slice]

    # Slice out Line Number
    line_number_slice = slice(6, 10)
    line_number = phone[line_number_slice]

    # Return formatted number string
    return "({}){}-{}".format(area_code, prefix, line_number)
