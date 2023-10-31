def format_address(address_string):
    house_number = ""
    street_name = ""

    # Separate the house number from the street name.
    address = address_string.split(" ", 1)
    # address_parts = street_name

    for address_part in address:
        # Complete the if-statement with a string method.
        if address:
            house_number = address[0]
        else:
            street_name += address_part + " "
    # Remove the extra space at the end of the last "street_name".
    street_name = address[1]

    # Use a string method to return the required formatted string.
    return "House_number {} on street named {}".format(house_number, street_name)


print(format_address("123 Main Street"))
# Should print: "House number 123 on a street named Main Street"


print(format_address("1001 1st Ave"))
# Should print: "House number 1001 on a street named 1st Ave"


print(format_address("55 North Center Drive"))
# Should print "House number 55 on a street named North Center Drive"


def alpha_length(string):
    character = ""
    count_alpha = 0
    # Complete the for loop sequence to iterate over "string".
    for character in string:
        # Complete the if-statement using a string method.
        if character.isalpha():
            count_alpha += 1
    return count_alpha


print(alpha_length("This has 1 number in it"))  # Should print 17
print(alpha_length("Thisisallletters"))  # Should print 16
print(alpha_length("This one has punctuation!"))  # Should print 21


def combine_lists(list1, list2):
    combined_list = list2  # Initialize an empty list variable

    for i in reversed(range(len(list1))):  # Reverse the order of "list1"
        combined_list.append(list1[i])  # Combine the two lists
    combined_list = list2
    return combined_list


Jaimes_list = ["Alma", "Chika", "Benjamin", "Jocelyn", "Oakley"]
Drews_list = ["Minna", "Carol", "Gunnar", "Malena"]


print(combine_lists(Jaimes_list, Drews_list))
# Should print ['Minna', 'Carol', 'Gunnar', 'Malena', 'Oakley', 'Jocelyn', 'Benjamin', 'Chika', 'Alma']


def increments(start, end):
    return [
        (x + 2) for x in range(start, end + 1)
    ]  # Create the required list comprehension.


print(increments(2, 3))  # Should print [4, 5]
print(increments(1, 5))  # Should print [3, 4, 5, 6, 7]
print(increments(0, 10))  # Should print [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]


def countries(countries_dict):
    result = ""
    # Complete the for loop to iterate through the key and value items
    # in the dictionary.
    for continent, countries in countries_dict.items():
        # Use a string method to format the required string.
        result += str(countries) + "\n"
    return result


print(
    countries(
        {
            "Africa": ["Kenya", "Egypt", "Nigeria"],
            "Asia": ["China", "India", "Thailand"],
            "South America": ["Ecuador", "Bolivia", "Brazil"],
        }
    )
)

# Should print:
# ['Kenya', 'Egypt', 'Nigeria']
# ['China', 'India', 'Thailand']
# ['Ecuador', 'Bolivia', 'Brazil']


def combine_guests(guests1, guests2):
    guests2 = guests2.copy()  # Use a dictionary method to combine the dictionaries.
    guests2.update(guests1)
    return guests2


Ricks_guests = {
    "Adam": 2,
    "Camila": 3,
    "David": 1,
    "Jamal": 3,
    "Charley": 2,
    "Titus": 1,
    "Raj": 4,
}
Tessas_guests = {"David": 4, "Noemi": 1, "Raj": 2, "Adam": 1, "Sakira": 3, "Chidi": 5}

print(combine_guests(Ricks_guests, Tessas_guests))
# Should print:
# {'David': 1, 'Noemi': 1, 'Raj': 4, 'Adam': 2, 'Sakira': 3, 'Chidi': 5, 'Camila': 3, 'Jamal': 3, 'Charley': 2, 'Titus': 1}


def setup_gradebook(old_gradebook):
    # Use a dictionary method to create a new copy of the "old_gradebook".
    new_gradebook = old_gradebook.copy()
    # Complete the for loop to iterate over the new gradebook.
    for old_gradebook in new_gradebook:
        # Use a dictionary operation to reset the grade values to 0.
        new_gradebook[old_gradebook] = 0
    return new_gradebook


fall_gradebook = {"James": 93, "Felicity": 98, "Barakaa": 80}
print(setup_gradebook(fall_gradebook))
# Should output {'James': 0, 'Felicity': 0, 'Barakaa': 0}

car_makes = ["Ford", "Volkswagen", "Toyota"]
car_makes.remove("Ford")

print(car_makes)

speed_limits = {"street": 35, "highway": 65, "school": 15}
speed_limits["highway"]

print(speed_limits)


def is_palindrome(input_string):
    # Two variables are initialized as string date types using empty
    # quotes: "reverse_string" to hold the "input_string" in reverse
    # order and "new_string" to hold the "input_string" minus the
    # spaces between words, if any are found.
    new_string = ""
    reverse_string = ""

    # Complete the for loop to iterate through each letter of the
    # "input_string"
    for letter in input_string:
        # The if-statement checks if the "letter" is not a space.
        if letter != " ":
            # If True, add the "letter" to the end of "new_string" and
            # to the front of "reverse_string". If False (if a space
            # is detected), no action is needed. Exit the if-block.
            new_string += letter.lower()
            reverse_string = letter.lower() + reverse_string

    # Complete the if-statement to compare the "new_string" to the
    # "reverse_string". Remember that Python is case-sensitive when
    # creating the string comparison code.
    if new_string == reverse_string:
        # If True, the "input_string" contains a palindrome.
        return True

    # Otherwise, return False.
    return False


print(is_palindrome("Never Odd or Even"))  # Should be True
print(is_palindrome("abc"))  # Should be False
print(is_palindrome("kayak"))  # Should be True


def convert_distance(miles):
    km = miles * 1.6
    result = "{} miles equals {:.1f} km".format(miles, km)
    return result


print(convert_distance(12))  # Should be: 12 miles equals 19.2 km
print(convert_distance(5.5))  # Should be: 5.5 miles equals 8.8 km
print(convert_distance(11))  # Should be: 11 miles equals 17.6 km
