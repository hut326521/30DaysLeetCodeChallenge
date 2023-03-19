"""
Just like a trie.
"""
from collections import defaultdict
from typing import Optional


class WordDictionary:
    next: dict[str, Optional["WordDictionary"]]

    def __init__(self):
        self.next = defaultdict(WordDictionary)

    def addWord(self, word: str) -> None:
        if not word:
            self.next[""] = None
            return
        first = word[0]
        self.next[first].addWord(word[1:])

    def search(self, word: str) -> bool:
        if not word:
            return "" in self.next
        first, remaining = word[0], word[1:]
        if first == ".":
            # search pattern length is over all words
            if not self.next:
                return False
            return any(
                _next.search(remaining)
                for _next in self.next.values()
                if _next is not None
            )
        if first not in self.next:
            return False
        return self.next[first].search(remaining)
