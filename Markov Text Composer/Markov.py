import random

class MarkovTextComposer:
    def __init__(self, order=2):
        self.order = order
        self.start_words = []
        self.transitions = {}
    
    def train(self, text):
        words = text.split()
        
        if len(words) < self.order + 1:
            return
        
        for i in range(len(words) - self.order):
            ngram = tuple(words[i:i + self.order])
            next_word = words[i + self.order]
            
            if i == 0:
                self.start_words.append(ngram)
            
            if ngram not in self.transitions:
                self.transitions[ngram] = []
            
            self.transitions[ngram].append(next_word)
    
    def generate_text(self, length=100):
        if not self.transitions:
            raise ValueError("No training data available.")
        
        current_ngram = random.choice(self.start_words)
        generated_text = list(current_ngram)
        
        for _ in range(length - self.order):
            if current_ngram in self.transitions:
                next_word = random.choice(self.transitions[current_ngram])
                generated_text.append(next_word)
                current_ngram = tuple(generated_text[-self.order:])
            else:
                break
        
        return ' '.join(generated_text)

# Example usage:
if __name__ == "__main__":
    # Create a MarkovTextComposer instance with an order of 2 (bi-grams).
    composer = MarkovTextComposer(order=2)
    
    # Provide some sample training text.
    training_text = "This is a sample text. This text is used for training the Markov chain text composer."
    
    # Train the composer with the sample text.
    composer.train(training_text)
    
    # Generate new text.
    generated_text = composer.generate_text(length=50)
    
    print(generated_text)
