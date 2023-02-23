def attack_choice() -> str:    
    
    print("Select your attack:\n"
        + "\t'R' - Regular attack\n"
        + "\t'S' - Special attack: more powerful against certain types\n"
        + "\t\tbut less accurate."
        )

    while True:
        try:
            attack_choice = str(input().upper())
        except ValueError:
            print("\nInvalid selection! Try again.\nPlease enter 'R', or 'S'.")
            continue
    
        if attack_choice not in ['R','S']:
            print("\nInvalid selection! Try again.\nPlease enter 'R', or 'S'.")
            continue


        else:
            break
    return attack_choice