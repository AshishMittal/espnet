import random
def filter(source_folder,target_folder, percent):
	vocab=[]
	f=open(source_folder+"/text")
	for line in f:
		liner=line.strip()
		vocab.extend(liner.split()[1:])
	vocab=list(set(vocab))
	f2=open(source_folder+"/text")
	fw=open(target_folder+"/text","w+")
	for liner in f2:
		line=liner.strip()
		words=line.split()[1:]
		words_to_change=random.sample(range(len(words)), int(percent*len(words)))
		new_words=[]
		for word in range(len(words)):
			#word=word.strip()
			if word in words_to_change:
				how_to_change=random.sample([0,1,2], 1)
				orig_word_index=vocab.index(words[word])
				if how_to_change==0:
					select_word=random.choice(vocab)
					new_words.append(select_word)
					new_words.append(words[word])
				elif how_to_change==1:
					select_word=random.choice(vocab)
					while select_word==word:
						select_word=random.choice(vocab)
					new_words.append(select_word)
			else:
				new_words.append(words[word])
		fw.write(line.split()[0]+" ")
		for word in new_words:
			fw.write(word+" ")
		fw.write("\n")
		
filter("espnet/egs/librispeech/asr1/data/train_clean_100","espnet/egs/librispeech/asr1/data/train_3",0.2)
		
