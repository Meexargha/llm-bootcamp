
!pip install transformers

from transformers import pipeline

generator = pipeline("text-generation", model="gpt2")

output = generator("Bharat ka AI future", max_length=50, num_return_sequences=1)

print(output[0]["generated_text"])
