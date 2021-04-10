#utterances=[]
import random
def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

def filter(source_folder,target_folder, percent):
	vocab=[]
	ffur=open(source_folder+"/text")
	for line in ffur:
		liner=line.strip()
		vocab.extend(liner.split()[1:])
	vocab=list(set(vocab))
	num_utterances=file_len(source_folder+"/wav.scp")
	#num_utterances2=file_len(source_folder+"/text")
	num_filtered_utt=int((1-percent)*num_utterances)
	filtered_utt=random.sample(range(num_utterances), num_filtered_utt)
	counter=0
	
	fw=open(target_folder+"/text","w+")
	with open(source_folder+"/text") as f:
		for line in f:
			if counter in filtered_utt:
				fw.write(line)
			else:
				new_words=[]
				parts = line.strip().split()
				id = parts[0]
				words=parts[1:]
				fw.write(id + " ")
				
				for word in words:
					how_to_change = random.sample([0,1,2,3,4,5], 1)[0]
					#insertion of a new word
					if how_to_change == 0:
						select_word=random.choice(vocab)
						new_words.append(select_word)
						new_words.append(word)
					#subsitution of the existing word
					elif how_to_change==1:
						select_word=random.choice(vocab)
						while select_word == word:
							select_word = random.choice(vocab)
						new_words.append(select_word)
					#deletion of the word.
					elif how_to_change == 2:
						None
					#keep the word as is.
					else:
						new_words.append(word)
				
				fw.write(" ".join(new_words) + "\n")
			counter+=1
	#print(num_utterances)
	#print(num_utterances2)
	#wav=open(source_folder+"/wav.scp")
	#text=open(source_folder+"/text")
	
filter("/dccstor/cssblr/ashish/dvrl/espnet/egs/librispeech/asr1/data/train-clean-100","/dccstor/cssblr/ashish/dvrl/espnet/egs/librispeech_0.1/asr1/data/train-clean-100",0.1)
