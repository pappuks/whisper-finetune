from datasets import load_dataset

dataset = load_dataset("audiofolder", data_dir=".")

test_index = []
train_index = []

test_set = ["_17.mp3", "_18.mp3", "_19.mp3", "_20.mp3", "_21.mp3"]

for index, item in enumerate(dataset['test']):
    if any(ext in str(item['audio']['path']) for ext in test_set):
        test_index.append(index)
    else :
        train_index.append(index)

print(train_index[:10])
print(test_index[:10])

dataset.train_test_split
