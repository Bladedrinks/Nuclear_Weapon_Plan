# A user-defined function to insert the conjunction of " and " into a string.


def insert_and_in(list_name):
    """Insert the conjunction of " and " into a string (usually between the penultimate word and the last word.
    For example, we got a list:

                                          factors = [1, 3, 7, 21].

    We want to change it into a string without square brackets outside, like this:

                                                1, 3, 7 and 21

    We can pass in the list name "factors" as the parameter by assigning the variable "factors" to the variable
    "list_name" and we will get a list shown above."""
    list_in_str = ""
    # test case: list_name = [45, 98, 45]
    # index:                  -3  -2  -1
    # test case: list_name = [45]
    # index:                  -1
    for i in range(-len(list_name), 0):
        if i == -1:
            list_in_str += f"{list_name[i]}"
        elif i == -2:
            list_in_str += f"{list_name[i]} and "
        else:
            list_in_str += f"{list_name[i]}, "
    print(list_in_str)
# End of the function definition.


