# задача с собеса

# будет ли строка полиндромом, если мы выборочно удалим один символ

def is_polindrome(s, start, end):
    n = (end - start) // 2
    for i in range(n):
        if s[start + i] != s[end - i]:
            return False, start + i, end - i
    return True, None, None


def pre_prolindrom(s: str) -> bool:
    is_pol, start, end = is_polindrome(s, 0, len(s) - 1)
    if is_pol and len(s) % 2 == 1:
        return True
    if is_pol:
        return False

    is_pol2, _, _ = is_polindrome(s, start + 1, end)
    is_pol3, _, _ = is_polindrome(s, start, end - 1)
    return is_pol2 or is_pol3


print(pre_prolindrom("abba"))
print(pre_prolindrom("ababa"))
print(pre_prolindrom("acbba"))
print(pre_prolindrom("acbmba"))
print(pre_prolindrom("abbac"))
print(pre_prolindrom("arbbac"))
