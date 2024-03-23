def possible_words(s, ans, result):
    if len(s) == 0:
        result.add(ans)
        return
    key = keypad[int(s[0])]
    for char in key:
        possible_words(s[1:], ans + char, result)

if __name__ == "__main__":
    keypad = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
    s = input()
    result = set()
    possible_words(s, "", result)
    for combination in sorted(result):
        print(combination, end=" ")