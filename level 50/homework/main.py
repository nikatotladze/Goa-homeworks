#2

def divide_numbers(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    except TypeError:
        return "Error: Both inputs must be numbers."
    return result


print(divide_numbers(10, 2))  
print(divide_numbers(10, 0))  
print(divide_numbers(10, "2"))  



def read_file(filename):
    try:
        with open(filename, "r") as file:
            return file.read()
    except FileNotFoundError:
        return "Error: File not found."
    except IOError:
        return "Error: An IOError occurred."


print(read_file("existing_file.txt"))  
print(read_file("non_existent_file.txt"))  



def get_value(dictionary, key):
    try:
        return dictionary[key]
    except KeyError:
        return f"Error: Key '{key}' not found in the dictionary."


my_dict = {"name": "Alice", "age": 25}
print(get_value(my_dict, "name"))  
print(get_value(my_dict, "height"))  



#3

def sum_numbers(mixed_list):
    return sum(int(x) for x in mixed_list if isinstance(x, (int, str)) and str(x).isdigit())


print(sum_numbers([10, "10", "abc", 20, "30"]))  
print(sum_numbers([5, "5", "hello", 15, "25"])) 


#4

def strCount(string, letter):
    return string.count(letter)


#5

def is_even(n): 
    return n%2 == 0
