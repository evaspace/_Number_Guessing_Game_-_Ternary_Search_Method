from random import randint
import time

def guess_number_with_thirds(target):
    min_val = 1
    max_val = 1000
    attempt_count = 0

    start_time = time.time()  # Start time measurement

    while min_val <= max_val:
        attempt_count += 1
        # Calculate the cut points (1/3 and 2/3 of the current range)
        cut1 = min_val + (max_val - min_val) // 3
        cut2 = min_val + 2 * (max_val - min_val) // 3
        
        # Make a guess based on the target position
        if target < cut1:
            guess = cut1
            print(f"My guess is {guess}.")
            response = "less"
        elif target > cut2:
            guess = cut2
            print(f"My guess is {guess}.")
            response = "greater"
        else:
            guess = (cut1 + cut2) // 2
            print(f"My guess is {guess}.")
            response = "between"

        # Check the response and update the range
        if guess < target:
            print("The number is greater.")
            min_val = guess + 1
        elif guess > target:
            print("The number is smaller.")
            max_val = guess - 1
        else:
            print(f"Congratulations, I found the number {target} in {attempt_count} attempt(s)!")
            end_time = time.time() 
            print(f"Time taken: {end_time - start_time:.4f} seconds")
            return

    print("The number was not found.")

# Uncomment the following function to use binary search method


def guess_number_with_binary(target):
    min_val = 1
    max_val = 1000
    attempt_count = 0

    start_time = time.time()  # Start time measurement

    while min_val <= max_val:
        attempt_count += 1
        guess = (min_val + max_val) // 2
        print(f"My guess is {guess}.")

        if guess < target:
            print("The number is greater.")
            min_val = guess + 1
        elif guess > target:
            print("The number is smaller.")
            max_val = guess - 1
        else:
            print(f"Congratulations, I found the number {target} in {attempt_count} attempt(s)!")
            end_time = time.time()  # End time measurement
            print(f"Time taken: {end_time - start_time:.4f} seconds")
            return

    print("The number was not found.")


if __name__ == "__main__":
    target = randint(1, 1000)
    print("I have chosen a number between 1 and 1000. Try to guess it!")  
    #guess_number_with_thirds(target)
    ####### Uncomment the following line to use the binary search method
    # guess_number_with_binary(target)

what_your_method = int(input("Choose your method (1 for thirds, 2 for binary): "))
if what_your_method == 1:
    guess_number_with_thirds(target)
elif what_your_method == 2:
    guess_number_with_binary(target)