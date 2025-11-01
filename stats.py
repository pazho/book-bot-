def count_words(content):
    word_count = content.split()
    words = len(word_count)
    return f"Found {words} total words"

def word_counter(content):
    chars = {}
    for ch in content.lower():
        if "a" <= ch <= "z":
            chars[ch] = chars.get(ch, 0) + 1
    return chars

def sort_it(item):
    return item["num"]

def sorting(counts):
    results = []
    for ch, num in counts.items():
        if ch.isalpha():
            results.append({"char": ch, "num": num})
    results.sort(reverse=True, key=sort_it)
    return results