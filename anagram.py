from urllib import request

if __name__ == "__main__":

    anagram_map = {}

    data = request.urlopen("http://andrew.cmu.edu/course/15-121/dictionary.txt")

    for word in data:
        cleaned_word = word.decode().strip()
        sorted_word = "".join(sorted(cleaned_word))
        matching_words = anagram_map.get(sorted_word, [])
        matching_words.append(cleaned_word)

        anagram_map[sorted_word] = matching_words

    for k in anagram_map.keys():
        print(k)
        print(anagram_map[k])
