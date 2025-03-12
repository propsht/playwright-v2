def find_largest_and_smallest(items):
    largest = items[0]  # Start with the first element
    smallest = items[0]  # Start with the first element

    for item in items:
        if item > largest:
            largest = item  # Update largest if a bigger number is found
        if item < smallest:
            smallest = item  # Update smallest if a smaller number is found

    return largest, smallest  # Return both values as a tuple

# Test the function
numbers = [1, 2, 3, 4, 55, 6]

largest, smallest = find_largest_and_smallest(numbers)

print("Largest:", largest)   # Output: 55
print("Smallest:", smallest) # Output: 1