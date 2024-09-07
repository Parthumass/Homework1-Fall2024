"""
ECE241 Fall 2024 - Homework1 Question1
"""

# Use the following constants if you need
below_20 = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve',
            'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
tens = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
thousands = ['', 'thousand', 'million']


def stringify(number):
    """

    :param number:
    :return:
    """
    pass

if __name__ == "__main__":
    print(stringify(1))         # Excepted: one
    print(stringify(10))        # Excepted: ten
    print(stringify(2024))      # Excepted: two thousand, twenty four
    print(stringify(20242024))  # Excepted: twenty million, two hundred and forty two thousand, twenty four
    print(stringify(202420242024)) # Excepted: four hundred and twenty million, two hundred and forty two thousand, twenty four
