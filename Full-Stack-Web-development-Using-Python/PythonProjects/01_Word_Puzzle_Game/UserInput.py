
def User_Input(Shuffle_RandomWord,num):
    print()
    print(f">>> Attempt {num}: Arrange the letters to form a valid word.")
    print()
    print(f"    {Shuffle_RandomWord}")
    User_Input = input(">>> ").lower()
    return User_Input
