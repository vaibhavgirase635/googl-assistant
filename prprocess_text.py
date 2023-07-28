import random
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

# Download NLTK resources (you can skip if you have already downloaded)
nltk.download()


# Sample questions and answers
data = {
    "what is your name": "My name is Chatbot.",
    "how are you": "I'm doing well, thank you!",
    "what is the weather today": "I'm sorry, I cannot provide real-time weather information.",
    "who is the president of the United States": "The current president of the United States is Joe Biden.",
    "tell me a joke": "Why don't scientists trust atoms? Because they make up everything!",
    "goodbye": "Goodbye! Have a nice day!",
}



# Text processing functions
def preprocess(text):
    tokens = word_tokenize(text.lower())
    tokens = [t for t in tokens if t.isalpha()]
    stop_words = set(stopwords.words('english'))
    tokens = [t for t in tokens if t not in stop_words]
    stemmer = PorterStemmer()
    tokens = [stemmer.stem(t) for t in tokens]
    return tokens


# Q-learning parameters
gamma = 0.8  # Discount factor
alpha = 0.5  # Learning rate

# Q-learning table
Q = {}

# Initialize Q-values for each state-action pair
for state in data.keys():
    Q[state] = {action: 0 for action in data.keys()}

# Q-learning function
def q_learning(state, next_state, action, reward):
    max_next_action = max(Q[next_state].values())
    Q[state][action] = (1 - alpha) * Q[state][action] + alpha * (reward + gamma * max_next_action)


# Training the chatbot
def train_chatbot(num_episodes=100):
    for episode in range(num_episodes):
        state = random.choice(list(data.keys()))
        done = False

        while not done:
            action = max(Q[state], key=Q[state].get)
            next_state = random.choice(list(data.keys()))
            reward = 1 if state == next_state else 0  # Reward is 1 for correct answer, 0 otherwise
            q_learning(state, next_state, action, reward)
            state = next_state

train_chatbot()

# Chatbot function
def chatbot(text):
    tokens = preprocess(text)
    state = " ".join(tokens)
    action = max(Q[state], key=Q[state].get)
    return data[action]

# Test the chatbot
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        break
    response = chatbot(user_input)
    print("Chatbot:", response)
