def build_shift_table(pattern):
    shift_table = {}
    pattern_len = len(pattern)
    for i in range(pattern_len - 1):
        shift_table[pattern[i]] = pattern_len - i - 1
    return shift_table

def search(haystack, needle):
    haystack_len = len(haystack)
    needle_len = len(needle)
    shift_table = build_shift_table(needle)
    i = needle_len - 1
    while i < haystack_len:
        match = True
        for j in range(needle_len):
            if haystack[i - j] != needle[needle_len - 1 - j]:
                match = False
                break
        if match:
            return i - needle_len + 1
        if haystack[i] in shift_table:
            i += shift_table[haystack[i]]
        else:
            i += needle_len
    return -1
def boyer_moore(haystack, needle):
    return search(haystack, needle)
