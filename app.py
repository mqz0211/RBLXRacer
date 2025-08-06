import random
import string
import sys

def generate_code():
    # Define the characters to choose from (A-Z and 0-9)
    characters = string.ascii_uppercase + string.digits
    
    # Generate four groups of four random characters
    groups = []
    for _ in range(4):
        group = ''.join(random.choice(characters) for _ in range(4))
        groups.append(group)
    
    # Join groups with hyphens and add RI prefix
    code = f"RI-{'-'.join(groups)}"
    return code

def main():
    print("Generating codes (press Enter for new code, 'q' + Enter to quit):")
    try:
        while True:
            user_input = input()  # Waits for Enter key press
            if user_input.lower() == 'q':
                break
            print(generate_code())
    except KeyboardInterrupt:
        print("\nExiting...")
        sys.exit(0)

if __name__ == "__main__":
    main()
