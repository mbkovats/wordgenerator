import torch
from torch.utils.data import Dataset, DataLoader
import torch.nn as nn
import torch.nn.functional as F
import pandas as pd
from wordgenerator import word_generator
from sklearn.model_selection import train_test_split
from torchtext.vocab import build_vocab_from_iterator
from torchtext.data.utils import get_tokenizer
from collections import Counter
from torchtext.vocab import Vocab

class Model(nn.Module):
    def __init__(self, in_features=16, h1=8, h2=8, out_features=8):
        super().__init__()
        self.fc1 = nn.Linear(in_features, h1)
        self.fc2 = nn.Linear(h1, h2)
        self.out = nn.Linear(h2, out_features)
    def forward(self, y):
        y = F.relu(self.fc1(y))
        y = F.relu(self.fc2(y))
        y = self.out(y)
        return y

device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')
torch.manual_seed(41)
model = Model().to(device)
url = 'words.csv/words.csv'
vocab = []
with open(url) as f:
    for line in f:
        vocab.append(line.strip())

# Step 1: Tokenize your text
tokenizer = get_tokenizer('basic_english')
words = tokenizer(' '.join(vocab))

# Step 2: Build a vocabulary from your words
counter = Counter(vocab)
vocab = Vocab(counter)

# Step 3: Convert your words into numerical representations
word_ids = [vocab[word] for word in words]

# Step 4: Convert your numerical representations into tensors
word_tensors = torch.tensor(word_ids)

# Step 5: Use DataLoader to load your data

class WordDataset(Dataset):
    def __init__(self, word_tensors):
        self.word_tensors = word_tensors
    def __len__(self):
        return len(self.word_tensors)
    def __getitem__(self, idx):
        return self.word_tensors[idx]

word_dataset = WordDataset(word_tensors)
word_loader = DataLoader(word_dataset, batch_size=16, shuffle=True)
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)
epochs = 100
losses = []
for i in range(epochs):
    for words in word_loader:
        y = words
        y = y.view(16,1)
        y = y.float()
        y = y.to(device)
        model.zero_grad()
        output = model(y)
        loss = F.cross_entropy(output, y)
        loss.backward()
        optimizer.step()
        losses.append(loss)
    print(f"Epoch: {i} Loss: {loss}")