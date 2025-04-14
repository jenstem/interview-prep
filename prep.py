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
            currentNode = node
        currentNode.endOfString = True
        print("Successfully inserted!")    

    def searchString(self, word):
        currentNode = self.root
        for i in word:
            node = currentNode.children.get(i)
            if node == None:
                return False 
            currentNode = node

        if currentNode.endOfString == True:
            return True
        else:
            return False    


newTrie = Trie()
newTrie.insertString('App')
newTrie.insertString('Appl')
print(newTrie.searchString('App'))