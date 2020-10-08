exit_from_program = "stop"
welcome_msg = "Enter a number or Stop to finish: "
error_msg = "Error: Pleae enter a number or Stop to finish"
while True:
    try:
        input_number = (input(welcome_msg))
        if input_number.lower().strip() == exit_from_program:
            break
        else:
            print((-15 < float(input_number) <= 12) or (14 < float(input_number) < 17) or (float(input_number) >= 19))
    except Exception as e:
        print(error_msg)
