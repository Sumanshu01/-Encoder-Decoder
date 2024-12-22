# Function to encode text to numbers (A=1, B=2, ..., Z=26)
def encode(text):
    encoded_text = []
    for char in text.upper():  # Convert to uppercase to match A=1, B=2, ...
        if char.isalpha():  # Check if it's a letter
            encoded_text.append(str(ord(char) - ord('A') + 1))
        else:
            encoded_text.append(char)  # If it's not a letter, keep it as is
    return " ".join(encoded_text)

# Function to decode numbers back to text (1=A, 2=B, ..., 26=Z)
def decode(encoded_text):
    decoded_text = []
    for item in encoded_text.split():  # Split the encoded text into parts
        if item.isdigit():  # Check if it's a number
            decoded_text.append(chr(int(item) + ord('A') - 1))  # Convert number to letter
        else:
            decoded_text.append(item)  # If it's not a number, keep it as is
    return "".join(decoded_text)

# Main part of the program
if __name__ == "__main__":
    print("1. Encode")
    print("2. Decode")
    choice = input("Choose an option (1 or 2): ")

    if choice == '1':
        text = input("Enter the text to encode: ")
        encoded = encode(text)
        print(f"Encoded text: {encoded}")
    
    elif choice == '2':
        encoded_text = input("Enter the encoded text to decode: ")
        decoded = decode(encoded_text)
        print(f"Decoded text: {decoded}")
    
    else:
        print("Invalid choice! Please choose 1 or 2.")
