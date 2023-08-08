from transformers import BertTokenizer, BertForQuestionAnswering, logging
import torch

logging.set_verbosity_warning()
cache_dir = r"C:\Users\shree\Desktop\projects\ML project\cache dir"
model_name = 'bert-large-uncased-whole-word-masking-finetuned-squad'  # Pre-trained BERT model for question answering



tokenizer = BertTokenizer.from_pretrained(model_name, cache_dir=cache_dir)
model = BertForQuestionAnswering.from_pretrained(model_name, cache_dir=cache_dir)