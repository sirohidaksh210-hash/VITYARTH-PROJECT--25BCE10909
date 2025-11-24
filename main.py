import module1

#  Main Execution Block -

def run_password_generator():
    """
    The main function to orchestrate the password generation process.
    """
    print("\n Welcome to the *Professional Password Generator!* ")
    

    # 1. Get user input with validation
    # The default min_val=0 allows for passwords with no symbols or numbers if desired.
    nr_letters = module1.get_integer_input("How many *letters* would you like in your password (e.g., 8)?\n> ")
    nr_symbols = module1.get_integer_input("How many *symbols* would you like (e.g., 2)?\n> ")
    nr_numbers = module1.get_integer_input("How many *numbers* would you like (e.g., 2)?\n> ")

    # Check for a total password length of zero and exit gracefully if so.
    if nr_letters + nr_symbols + nr_numbers == 0:
        print("\n Error: The total length of your password is zero. Exiting.")
        module1.sys.exit()

    # 2. Generate the password
    print("\nGenerating your strong password...")
    final_password = module1.generate_strong_password(nr_letters, nr_symbols, nr_numbers)

    # 3. Output the result
   
    print(f" The generated password (Total Length: {len(final_password)}) is: \n*{final_password}*")
    
    print("\nRemember to use a unique password for every service!")


# This standard Python construct ensures the run_password_generator function
# is called only when the script is executed directly, not when it's imported.
 

run_password_generator()

  
