def count_vowels(word):
    count=0
    for char in word:
        if char.lower() in 'aeiou':
            count+=1
    return count

print(count_vowels('Aouy'))