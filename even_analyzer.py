number = int(input("Enter a number: "))

if number < 0:
    print("Please enter a positive number")
else:
    total = 0
    count = 0
    largest_even = 0

    for i in range(1, number + 1):
        if i % 2 == 0:
            total += i
            count += 1
            largest_even = i

    print(f"\nResults for numbers from 1 to {number}:")
    print(f"Total of even numbers: {total}")
    print(f"Count of even numbers: {count}")
    print(f"Largest even number: {largest_even}")
