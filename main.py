# Create an empty list
my_list = []

while True:
    # Display the menu
    print("\nChoose an action:")
    print("1. Add a word to the list")
    print("2. Remove a word from the list")
    print("3. View the list")
    
    choice = input("Enter the action number (or 'stop' to exit): ")
    
    # Check if the user wants to exit
    if choice.lower() == 'stop':
        print("Program terminated.")
        break
    
    # Process the user's choice
    elif choice == '1':
        word = input("Enter a word to add: ")
        my_list.append(word)
        print(f"Word '{word}' has been added to the list.")
        
    elif choice == '2':
        if len(my_list) == 0:
            print("The list is empty!")
        else:
            word = input("Enter a word to remove: ")
            if word in my_list:
                my_list.remove(word)
                print(f"Word '{word}' has been removed from the list.")
            else:
                print("This word is not in the list!")
                
    elif choice == '3':
        if len(my_list) == 0:
            print("The list is empty!")
        else:
            print("Current list:")
            for i, word in enumerate(my_list, 1):
                print(f"{i}. {word}")
                
    else:
        print("Invalid choice! Please choose 1, 2, or 3.")
