endOfWord = "$"

def generateTrieFromWordsArray(words):
	root = {}
	for word in words:
		currentDict = root
		for letter in word:
			currentDict = currentDict.setdefault(letter, {})
		currentDict[endOfWord] = endOfWord
	return root

def isWordPresentInTrie(trie, word):
	currentDict = trie
	for letter in word:
		if letter in currentDict:
			currentDict = currentDict[letter]
		else: 
			return False
	if endOfWord in currentDict:
		return True
	else: 
		return False 


arrayOfWords = ['hello', 'hey', 'what', 'when', 'why']
wordsTrie = generateTrieFromWordsArray(arrayOfWords)
 print wordsTrie
 print isWordPresentInTrie(wordsTrie, 'hello')
 print isWordPresentInTrie(wordsTrie, 'hellow')
