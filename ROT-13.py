def caesar_shift(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            # Determine whether the character is upper or lower case
            is_upper = char.isupper()          
            # Shift the character within the range of its case (A-Z or a-z)
            shifted_char = chr((ord(char) - ord('A' if is_upper else 'a') + shift) % 26 + ord('A' if is_upper else 'a'))            
            result += shifted_char
        else:
            result += char
    return result

# Example usage
INPUT_TEXT = "WIAOOSFzMjXXBC0KoSKBbJ8puQm5lIEi"
SHIFT_AMOUNT = -13
encrypted_text = caesar_shift(INPUT_TEXT, SHIFT_AMOUNT)
print("Original text:", INPUT_TEXT)
print("Encrypted text:", encrypted_text)
