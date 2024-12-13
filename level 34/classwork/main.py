#1

#1

def count_positives_sum_negatives(arr):
    if not arr:  # Check if the list is empty
        return []  # Return an empty list if input is empty
    count_positives = sum(1 for x in arr if x > 0)  # Count positive numbers
    sum_negatives = sum(x for x in arr if x < 0)   # Sum negative numbers
    return [count_positives, sum_negatives]


#2

def dna_to_rna(dna):
    return dna.replace("T", "U")

#3

def zero_fuel(distance_to_pump, mpg, fuel_left):
    return mpg * fuel_left >= distance_to_pump

#4

def bmi(weight, height):
    # Calculate BMI
    bmi_value = weight / (height ** 2)
    
    # Determine category
    if bmi_value <= 18.5:
        return "Underweight"
    elif bmi_value <= 25.0:
        return "Normal"
    elif bmi_value <= 30.0:
        return "Overweight"
    else:
        return "Obese"


#5

def minimum(arr):
    return min(arr)  # Use the built-in `min` function to find the smallest value

def maximum(arr):
    return max(arr)  # Use the built-in `max` function to find the largest value
