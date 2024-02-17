
import transformers

t = transformers.pipeline("sentiment-analysis")

prompt = "We hope you don't hate this amazing thing!"
prompt_sentiment = t(prompt)

print(f"\n{prompt}")
print(prompt_sentiment)
