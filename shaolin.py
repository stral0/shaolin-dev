import os
import time
import pickle
from tqdm import tqdm


def read_words():
	begin = {}
	end = {}
	with open('rijeci.txt', 'r') as f:
		words = f.read()
		words = words.split('\n')

		for word in words:
			begin[word] = word[:2]
			end[word] = word[-2:]
	return begin, end

def frequency(begin, end):
	begin_values = list(begin.values())
	end_values = list(end.values())

	freq = {}
	for ev in tqdm(end_values):
		points = begin_values.count(ev)
		if ev not in freq:
			freq[ev] = points
		else:
			if points > freq[ev]:
				freq[ev] = points

	return freq


def sort_version():
	begin, end = read_words()
	freq = frequency(begin, end)
	words = begin.keys()

	word_fitness = {}
	for word in words:
		begin_of_the_word = begin[word]
		if begin_of_the_word in freq:
			word_fitness[word] = freq[begin_of_the_word]
		else:
			word_fitness[word] = 0

	with open('word_fitness.pkl', 'wb') as wf:
		pickle.dump(word_fitness, wf)

def print_dict(dic, last = -1):
	i = 0
	for word in dic:
		print(word + ' ' * (20 - len(word)) + str(dic[word]))
		i += 1
		if i == last:
			return
def load_shaolin(file_path):
	with open(file_path, 'rb') as f:
		unpickled = pickle.load(f)
		return unpickled

def main():
	#sort_version()
	print_dict(load_shaolin('word_fitness.pkl'), 30)

if __name__ == '__main__':
	main()