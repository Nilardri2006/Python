# a= """harry is agood boy
# but not a bad boy"""
# print(a)


a = "harry is agood boy \n but not a bad\tboy"
print(a)#using backslash n we can print in new line


a = "harry is a \'good\' boy \n but not a bad \"boy\""
print(a)#when need to print double quote

# Demonstrating various escape sequences in Python

# 1. Backslash (\\) – used to insert a literal backslash
print("1. Backslash: Roney\\Pramanick")       # Output: Roney\Pramanick

# 2. Single quote (\') – allows single quote inside single-quoted string
print("2. Single quote: It\'s Python")        # Output: It's Python

# 3. Double quote (\") – allows double quote inside double-quoted string
print("3. Double quote: He said, \"Hello\"")  # Output: He said, "Hello"

# 4. New line (\n) – breaks the line
print("4. New line:\nNext line here")         # Output:
# 4. New line:
# Next line here

# 5. Tab (\t) – inserts a horizontal tab (like a big space)
print("5. Tab:\tTab space added")             # Output: Tab:    Tab space added

# 6. Carriage return (\r) – returns cursor to start of the line, overwrites text
print("6. Carriage return: 12345\rRONEY")     # Output: RONEY5 (RONEY overwrites 12345)

# 7. Backspace (\b) – deletes the character before it
print("7. Backspace: Helloo\b")               # Output: Hello (removes extra 'o')

# 8. Form feed (\f) – rarely used, may act like a newline
print("8. Form Feed: Line1\fLine2")           # Output varies by system; acts like new line or spacing

# 9. Vertical tab (\v) – also rarely used, separates text vertically
print("9. Vertical Tab: Line1\vLine2")        # Output varies; prints with vertical spacing

# 10. Bell sound (\a) – system beep (if supported)
print("10. Bell Sound (Beep): \a")            # Output: Beep sound (may or may not play depending on system)

# 11. Octal value (\ooo) – represents ASCII character using octal
print("11. Octal (\\101):", "\101")           # Output: A (octal 101 = ASCII 65 = 'A')

# 12. Hexadecimal value (\xhh) – represents ASCII character using hex
print("12. Hex (\\x41):", "\x41")             # Output: A (hex 41 = ASCII 65 = 'A')
