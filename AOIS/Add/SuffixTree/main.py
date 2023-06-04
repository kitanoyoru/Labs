import unittest
from suffix_tree import SuffixTree



if __name__ == '__main__':
    s = SuffixTree("hello world banana bla bla example test")

    print(s.find_substring("wo"))


