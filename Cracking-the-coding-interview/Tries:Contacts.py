#!/bin/python3

import math
import os
import random
import re
import sys

from collections import defaultdict


class TrieNode:

    # Trie node class
    def __init__(self):
        self.children = [None] * 26
        self.count = 0

        # isEndOfWord is True if node represent the end of the word
        self.isEndOfWord = False


class Trie:

    # Trie data structure class
    def __init__(self):
        self.root = self.getNode()

    def getNode(self):

        # Returns new trie node (initialized to NULLs)
        return TrieNode()

    def _charToIndex(self, ch):

        # private helper function
        # Converts key current character into index
        # use only 'a' through 'z' and lower case

        return ord(ch) - ord('a')

    def insert(self, key):

        # If not present, inserts key into trie
        # If the key is prefix of trie node,
        # just marks leaf node
        pCrawl = self.root
        pCrawl.count += 1
        length = len(key)
        for level in range(length):
            index = self._charToIndex(key[level])

            # if current character is not present
            if not pCrawl.children[index]:
                pCrawl.children[index] = self.getNode()
            pCrawl = pCrawl.children[index]
            pCrawl.count += 1

        # mark last node as leaf
        pCrawl.isEndOfWord = True

    def search(self, key):

        pCrawl = self.root
        length = len(key)
        for level in range(length):
            index = self._charToIndex(key[level])
            if not pCrawl.children[index]:
                return 0
            pCrawl = pCrawl.children[index]

        return pCrawl.count


if __name__ == '__main__':
    n = int(input())
    t = Trie()

    for n_itr in range(n):
        opContact = input().split()

        op = opContact[0]

        contact = opContact[1]

        if op[0] == 'a':
            t.insert(contact)
        elif op[0] == 'f':
            print(t.search(contact))
