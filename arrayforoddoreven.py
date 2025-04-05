def odd_even(numbers):
    odd_numbers = []
    even_numbers = []
    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
        else:
            odd_numbers.append(num)
    return odd_numbers, even_numbers
num = list(map(int, input("Enter numbers separated by spaces: ").split()))
odd, even = odd_even(num)
print("Odd numbers:", odd)
print("Even numbers:", even)
