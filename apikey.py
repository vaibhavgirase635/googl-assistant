from transformers import TFAutoModelForQuestionAnswering, AutoTokenizer
from transformers import AutoTokenizer

cache_dir = r"C:\Users\shree\Desktop\projects\ML project\cache"
model_name = "distilbert-base-uncased"

model = TFAutoModelForQuestionAnswering.from_pretrained(model_name, cache_dir=cache_dir)
tokenizer = AutoTokenizer.from_pretrained(model_name, cache_dir=cache_dir)

