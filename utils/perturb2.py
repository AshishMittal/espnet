#utterances=[]
import random
def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

def filter(source_folder,target_folder, percent):
	num_utterances=file_len(source_folder+"/wav.scp")
	#num_utterances2=file_len(source_folder+"/text")
	num_filtered_utt=int((1-percent)*num_utterances)
	filtered_utt=random.sample(range(num_utterances), num_filtered_utt)
	counter=0
	fw=open(target_folder+"/wav.scp","w+")
	with open(source_folder+"/wav.scp") as f:
		for line in f:
			if counter in filtered_utt:
				fw.write(line)
			counter+=1
	counter=0
	fw=open(target_folder+"/text","w+")
	with open(source_folder+"/text") as f:
		for line in f:
			if counter in filtered_utt:
				fw.write(line)
			counter+=1
	#print(num_utterances)
	#print(num_utterances2)
	#wav=open(source_folder+"/wav.scp")
	#text=open(source_folder+"/text")
	
filter("espnet/egs/librispeech/asr1/data/train_clean_100","espnet/egs/librispeech/asr1/data/train_2",0.1)
