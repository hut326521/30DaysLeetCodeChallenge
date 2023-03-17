from typing import Union
from unittest import TestCase


class Trie:

    def __init__(self):
        self.next: dict[str, Union[Trie, None]] = {}

    def insert(self, word: str) -> None:
        if not word:
            self.next[""] = None
            return
        first = word[0]
        if first not in self.next:
            self.next[first] = Trie()
        self.next[first].insert(word[1:])

    def search(self, word: str) -> bool:
        if not word:
            return "" in self.next
        first = word[0]
        if first not in self.next:
            return False
        return self.next[first].search(word[1:])

    def startsWith(self, prefix: str) -> bool:
        if not prefix:
            return True
        first = prefix[0]
        if first not in self.next:
            return False
        return self.next[first].startsWith(prefix[1:])


class TestTrie(TestCase):
    def test_insert(self):
        trie = Trie()
        trie.insert("abcd")
        node = trie
        for char in "abcd":
            self.assertIn(char, node.next)
            node = node.next[char]
        self.assertIn("", node.next)

    def test_search(self):
        trie = Trie()
        trie.insert("abcd")
        self.assertTrue(trie.search("abcd"))
        self.assertFalse(trie.search("abc"))

    def test_startsWith(self):
        trie = Trie()
        trie.insert("abcd")
        self.assertTrue(trie.startsWith("abcd"))
        self.assertTrue(trie.startsWith("abc"))
        self.assertFalse(trie.startsWith("abcde"))


