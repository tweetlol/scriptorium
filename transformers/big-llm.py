
from transformers import GPT2LMHeadModel, GPT2Tokenizer

prompt = "For the continuation of spacetime is to be found"

# load model and it's token encoder
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2", pad_token_id=tokenizer.eos_token_id)

# encode the context
input_ids = tokenizer.encode(prompt, return_tensors="pt")

# generate text using random sampling on iterations
sample_outputs = model.generate(
	input_ids,
	max_length=300,
	do_sample=True,
	top_k=50,
    top_p=0.95,
#	temperature=0.9,
    num_return_sequences=3
	)


def remove_unfinished_sentence(text):
    # List of punctuation marks
    punctuation_marks = [".", "!", "?"]
    
    # Find the index of the last occurrence of a punctuation mark
    last_punctuation_index = max(text.rfind(p) for p in punctuation_marks)
    
    # If a punctuation mark is found, truncate the string up to that point
    if last_punctuation_index != -1:
        return text[:last_punctuation_index + 1]  # Include the punctuation mark
    else:
        return text  # Return the original string if no punctuation mark is found
    

print(f"Output: \n" + 100 * "-")
for i, sample_output in enumerate(sample_outputs):
#  print(f"{i}: {tokenizer.decode(sample_output, skip_special_tokens=True)}\n")
  print(f"{i}: {remove_unfinished_sentence(tokenizer.decode(sample_output, skip_special_tokens=True))}\n")
