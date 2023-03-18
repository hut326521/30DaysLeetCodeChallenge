/*
We can choose Hashset or TrieNode to solve this problem.
Inserting in Hashset Arch is faster, but startWith() is not. 
I decide to choose TrieNode because it's more fit topic.
Only TrieNode's property need to be thought, other is easy.
*/
class TrieNode {
    boolean isWordEnd;
    TrieNode[] nextNode;

    public TrieNode() {
        isWordEnd = false;
        nextNode = new TrieNode[26]; // 26 English lowercase letters
    }
}

class Trie {
    TrieNode root;

    public Trie() {
        root = new TrieNode();
    }

    public void insert(String word) {
        TrieNode node = root;

        for(char c : word.toCharArray()) {
            int charIndex = c - 'a';

            if(node.nextNode[charIndex] == null) {
                node.nextNode[charIndex] = new TrieNode();
            }
            node = node.nextNode[charIndex];
        }
        node.isWordEnd = true;
    }

    public boolean search(String word) {
        TrieNode node = root;

        for(char c : word.toCharArray()) {
            int charIndex = c - 'a';

            if(node.nextNode[charIndex] == null) {
                return false;
            }
            node = node.nextNode[charIndex];
        }

        return node.isWordEnd;
    }

    public boolean startsWith(String prefix) {
        TrieNode node = root;

        for(char c : prefix.toCharArray()) {
            int charIndex = c - 'a';

            if(node.nextNode[charIndex] == null) {
                return false;
            }
            node = node.nextNode[charIndex];
        }

        return true;
    }
}