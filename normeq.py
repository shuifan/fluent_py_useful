from unicodedata import normalize
import unicodedata

# 不区分大小写的相等
def nfc_equal(str1, str2):
    return normalize('NFC', str1) == normalize('NFC', str2)

# 区分大小写的相等
def fold_equal(str1, str2):
    return normalize('NFC', str1).casefold() == normalize('NFC', str2).casefold()

def shave_marks(str):
    """取出所有的 变音符号"""
    nfd_str = normalize('NFD', str)
    shaved_str = ''.join(c for c in nfd_str if not unicodedata.combining(c))
    return normalize('NFC', shaved_str)

if __name__ == '__main__':
    # s1 = 'A'
    # s2 = 'a'
    # s3 = 'Zέφupoς, Zéfiro'
    # print(nfc_equal(s1, s2))
    # print(fold_equal(s1, s2))
    # print(shave_marks(s3))
    # print(shave_marks)
    #
    # single_map = str.maketrans({'‰': '<per mille>'})
    # print(type(single_map))
    # print('‰'.translate(single_map))
    # print(1,2)
    # print("1""2")

    # import re
    # re_numbers_str = re.compile(r'\d+')
    # re_words_str = re.compile(r'\w+')
    # re_numbers_bytes = re.compile(rb'\d+')
    # re_words_bytes = re.compile(rb'\w+')
    # text_str = ("Ramanujan saw \u0be7\u0bed\u0be8\u0bef"" as 1729 = 1³ + 12³ = 9³ + 10³.")
    # text_bytes = text_str.encode('utf_8')
    #
    # print(repr(text_str))
    # print(re_numbers_str.findall(text_str), re_numbers_bytes.findall(text_bytes), sep = '\n')
    # print(sep = '\n')
    # print(re_words_str.findall(text_str), re_words_bytes.findall(text_bytes), sep = '\n')

    # print('''
    # a
    # b
    # ''')
    # print("a"
    #       "b")

    import os
    import sys

    print(sys.getfilesystemencoding())

    a = [1,2,3,3]
    print(set(a))
