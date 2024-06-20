def word_break(s, dictionary):
    n = len(s)
    valid = [False] * (n + 1)
    valid[0] = True

    # Iterate over each position in the string
    for i in range(1, n + 1):
        # Check all substrings ending at position i
        for j in range(i, 0, -1):
            if s[j - 1:i] in dictionary and valid[j - 1]:
                valid[i] = True
                break

    if valid[n-1]:
        # Reconstruct the sequence of valid words
        words = []
        i = n
        while i > 0:
            for j in range(i, 0, -1):
                if s[j - 1:i] in dictionary and valid[j - 1]:
                    words.append(s[j - 1:i])
                    i = j - 1
                    break
        return words[::-1]  # Reverse to get the correct order
    else:
        return None

# Example usage:
s = "ienjoysolvingalgorithmicquestions"
dictionary = {"i", "enjoys", "solving", "algorithmic", "questions"}
print(word_break(s, dictionary))
