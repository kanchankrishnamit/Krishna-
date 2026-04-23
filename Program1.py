numbers = [10, 5, 8, 2, 15]

print("Original List:", numbers)
print("First element:", numbers[0])
print("Last element:", numbers[-1])

numbers.append(20)
numbers.insert(2, 12)
print("List after adding elements:", numbers)

numbers.remove(8)
numbers.pop()
print("List after removing elements:", numbers)

numbers.sort()
print("Sorted List:", numbers)

numbers.reverse()
print("Reversed List:", numbers)
