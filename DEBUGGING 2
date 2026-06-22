def string_match(text, pattern):
    n = len(text)
    m = len(pattern)

    for i in range(n - m + 1):   # Corrected loop condition
        j = 0

        while j < m and text[i + j] == pattern[j]:
            j += 1

        if j == m:
            return i   # Pattern found at index i

    return -1   # Pattern not found


# Example
text = "ABCDE"
pattern = "DE"

result = string_match(text, pattern)

if result != -1:
    print("Pattern found at index", result)
else:
    print("Pattern not found")
