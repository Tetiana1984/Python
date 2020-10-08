import random
welcome_msg = "I made up a number. Can you guess it? "
error_msg = "Error: Pleae enter a number"
congration_msg = "Congratulations you won!"
high_msg = "Too high !"
low_msg = "Too low !"
while True:
    try:
        input_number = int(input(welcome_msg))
        random_number = random.randrange(5)
        print(random_number)
        print((input_number > random_number and high_msg) or
             (input_number < random_number and low_msg) or
             (input_number == random_number and congration_msg))
    except Exception as e:
        print(error_msg)
