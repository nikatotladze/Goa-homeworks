#2

def remove_duplicates(input_string):
    # set() შლის დუპლიკატებს
    unique_characters = set(input_string)
    # set-დან უკან string-ის შექმნა, ნაგულისხმევი რიგითობა შეიძლება შეიცვალოს
    result = ''.join(unique_characters)
    return result

# ფუნქციის გამოყენება
text = "hello world"
print(remove_duplicates(text))


#3

def feast(beast, dish):
    # შევადაროთ სიმების პირველი და ბოლო ასოები
    return beast[0] == dish[0] and beast[-1] == dish[-1]


#4

def array_plus_array(arr1, arr2):
    # ორი სიის ელემენტების ჯამის გამოთვლა
    return sum(arr1) + sum(arr2)


#5

def get_average(marks):
    return sum(marks) // len(marks)


#6

def reverseWords(str):
    return " ".join(str.split(" ")[::-1])


#7

def check_for_factor(base, factor):
    return base % factor == 0