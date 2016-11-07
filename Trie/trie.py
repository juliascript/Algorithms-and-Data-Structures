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

def offerPossibleCompletionsToStringInTrie(trie, string):
	currentDict = trie
	arrayOfPossibleWords = []
	for letter in string: 
		if letter in currentDict:
			currentDict = currentDict[letter]
		else:
			return "Trie does not offer any completions to %s" % (string)
	# now current dict is at the level which would offer completions. 
	# at this point, it is necessary to step down through all possiblities 
	# grab the values at this level, count them, and then for that many times, go through into the last step. 
	# if there, at any time is more than one value per key (there is more than one possible completion),
	#   that should also be followed, and likewise for following that, if there are other paths, follow them
	# if at any point, do you find the endOfWord, add the path to the array as a string

	for nextLetter in currentDict:
		print nextLetter

	



arrayOfWords = ['hello', 'hey', 'what', 'when', 'why']
wordsTrie = generateTrieFromWordsArray(arrayOfWords)
# print wordsTrie['h']['e']
# print isWordPresentInTrie(wordsTrie, 'hello')
# print isWordPresentInTrie(wordsTrie, 'hellow')
print offerPossibleCompletionsToStringInTrie(wordsTrie, 'he')
