# Trie

class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfString = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insertString(self, word):
        currentNode = self.root
        for i in word:
            ch = i
            node = currentNode.children.get(ch)
            if node is None:
                node = TrieNode()
                currentNode.children.update({ch:node})   
            current = node
        current.endOfString = True
        print("Successfully inserted!")    

newTrie = Trie()
newTrie.insertString("App")
newTrie.insertString("Appl")
