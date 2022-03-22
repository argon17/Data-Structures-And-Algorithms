from __future__ import annotations
from typing import List

from collections import defaultdict

class TrieNode:
    def __init__(self, letter = '') -> None:
        self.letter = letter
        self.children = defaultdict(TrieNode)
        self.isEnd = False

class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()
    
    def insert(self, word : str) -> None:
        cur = self.root
        for letter in word:
            if letter not in cur.children:
                child = TrieNode(letter)
                cur.children[letter] = child
            cur = cur.children[letter]
        cur.isEnd = True
    
    def search(self, word : str) -> None:
        cur = self.root
        for letter in word:
            if letter not in cur.children:
                return False
            cur = cur.children[letter]
        return cur.isEnd
    
    def getAllWordsWithPrefix(self, prefix : str) -> List[str]:
        words = []
        cur = self.root
        for letter in prefix:
            if letter not in cur.children:
                return words
            cur = cur.children[letter]
        suffixes = self.getAllWordsFromNode(cur)
        for suffix in suffixes:
            words.append(prefix[:-1] + suffix)
        return words
        
    def getAllWordsFromNode(self, node : TrieNode) -> List[str]:
        words = []
        def dfs(cur : TrieNode, path : List[str] = []):
            path.append(cur.letter)
            if cur.isEnd:
                words.append(''.join(path))
            for letter in cur.children:
                dfs(cur.children[letter], path)
            path.pop()
        dfs(node)
        return words
    
def main():
    trie = Trie()
    trie.insert('toy')
    trie.insert('top')
    trie.insert('temporary')
    trie.insert('tool')
    trie.insert('trie')
    trie.insert('hello')
    print(trie.getAllWordsWithPrefix('to'))

if __name__ == '__main__':
    main()
    