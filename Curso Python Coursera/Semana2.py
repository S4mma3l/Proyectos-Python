"""Terms

    expression - a combination of numbers, symbols, or other values that produce a result when evaluated

    data types - classes of data (e.g., string, int, float, Boolean, etc.), which include the properties and behaviors of instances of the data type (variables)

    variable - an instance of a data type class, represented by a unique name within the code, that stores changeable values of the specific data type

    implicit conversion - when the Python interpreter automatically converts one data type to another

    explicit conversion - when code is written to manually convert one data type to another using a data type conversion function:

        str() - converts a value (often numeric) to a string data type

        int() - converts a value (usually a float) to an integer data type

        float() - converts a value (usually an integer) to a float data type"""

# The following lines assign the variable to the left of the =
# assignment operator with the values and arithmetic expressions
# on the right side of the = assignment operator.
hotel_room = 100
tax = hotel_room * 0.08
total = hotel_room + tax
room_guests = 4
share_per_person = total / room_guests

# This line outputs the result of the final calculation stored
# in the variable "share_per_person"
print("Each person needs to pay: ", str(share_per_person))  # change a data type

# The following 5 lines assign strings to a list of variables.
salutation = "Dr."
first_name = "Prisha"
middle_name = "Jai"
last_name = "Agarwal"
suffix = "Ph.D."

print(
    salutation + " " + first_name + " " + middle_name + " " + last_name + ", " + suffix
)
# The comma as a string ", " adds the conventional use of a comma plus a
# space to separate the last name from the suffix.

# Alternatively, you could use commas in place of the + connector:
print(salutation, first_name, middle_name, last_name, ",", suffix)
# However, you will find that this produces a space before a comma within a string.

print("5 * 3 = " + str(5 * 3))

# Resolution:
# print("5 * 3 = " + str(5*3))
#
# To avoid a type error between the string and the integer within the
# print() function, you can make an explicit data type conversion by
# using the str() function to convert the integer to a string.
#
numerator = 7
denominator = 1  # Possible resolution: Change the denominator value
result = numerator / denominator
print(result)

# One possible assumption for a number divided by zero error might
# include the issue of a null value as a denominator (could happen when
# using a loop to iterate over values in a database). In such cases, the
# desired outcome may be to leave the numerator value intact. The
# numerator value can be preserved by reassigning the denominator with
# the integer value of 1. The result would then equal the numerator.


bill = 47.28
tip = bill * 0.15
total = bill + tip
share = total / 2
print("each person needs to pay: " + str(share))


word1 = "How"
word2 = "do"
word3 = "you"
word4 = "like"
word5 = "Python"
word6 = "so"
word7 = "far?"

print(word1, word2, word3, word4, word5, word6, word7)
