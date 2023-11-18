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
input_text = "WIAOOSFzMjXXBC0KoSKBbJ8puQm5lIEi"
shift_amount = -13
encrypted_text = caesar_shift(input_text, shift_amount)
print("Original text:", input_text)
print("Encrypted text:", encrypted_text)
