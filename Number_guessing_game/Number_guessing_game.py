import random
comp_guess = random.randint(1, 100)
number_of_attempts = 0
while True:
    try:
        user_guess = int(input("Please Input The Number:"))


        if comp_guess == user_guess:
            number_of_attempts = number_of_attempts + 1
            print(f'you won in {number_of_attempts} attempts.')
            break
        elif user_guess < comp_guess:
            print("Too Low!")
            number_of_attempts = number_of_attempts + 1
        else:
            print("Too High!")
            number_of_attempts = number_of_attempts + 1

    except:
        print("Choose a Number Between 1 to 100!")