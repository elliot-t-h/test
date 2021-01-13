##Test upload of random function that counts duplicate characters in single words
def duplicate_count(text):
    counts = {}
    for letter in text:
        letter = letter.lower()
        if letter in counts:
            counts[letter] += 1
        else:
            counts[letter] = 1         
    
    repeats = []
    for key, value in counts.items():
        if value > 1:
            repeats.append(key)
    return len(repeats) 
