/*
Use TrieNode to solve it(which just implement few days ago).
Because there are many possible, use recursive to solve.
If meet '.', just seperate to some parts.
*/

class WordDictionary {
    TrieNode mTrieRoot;

    public WordDictionary() {
        mTrieRoot = new TrieNode();
    }
    
    public void addWord(String word) {
        TrieNode node = mTrieRoot;
        
        for(char c : word.toCharArray()) {
            if(node.nextNode[c -'a'] == null) {
                node.nextNode[c -'a'] = new TrieNode();
            }
            
            node = node.nextNode[c -'a'];
        }
        
        node.isWordEnd = true;
    }
    
    public boolean search(String word) {
        return searchAdapter(mTrieRoot, word, 0);
    }
    
    public boolean searchAdapter(TrieNode node, String word, int index) {
        if (index == word.length()) {
            return node.isWordEnd;
        }
        
        char c = word.charAt(index);
        
        if(c == '.') {
            for(TrieNode tn : node.nextNode) {
                    if(tn != null && 
                       searchAdapter(tn, word, index + 1)) {
                         return true;
                    }
                }
            
            return false;
        } else {
            if(node.nextNode[c -'a'] == null) {
                return false;
            }
            
            return searchAdapter(node.nextNode[c -'a'], word, index + 1);
        }
    }
}


class TrieNode {
    boolean isWordEnd;
    TrieNode[] nextNode;

    public TrieNode() {
        isWordEnd = false;
        nextNode = new TrieNode[26];
    }
}