from llama_cpp import Llama
import time
BOS, EOS = "<s>", "</s>"
B_INST, E_INST = "[INST]", "[/INST]"
B_SYS, E_SYS = "<<SYS>>\n", "\n<</SYS>>\n\n"
DEFAULT_SYSTEM_PROMPT = """\
You are a helpful, respectful and honest assistant. Always answer as helpfully as possible, while being safe. Your answers should not include any harmful, unethical, racist, sexist, toxic, dangerous, or illegal content. Please ensure that your responses are socially unbiased and positive in nature.

If a question does not make any sense, or is not factually coherent, explain why instead of answering something not correct. If you don't know the answer to a question, please don't share false information."""
file = open("output2.txt", "r")
content = file.read()
#count number of words in content
word_count = len(content.split())
letter_count = len(content)
print(f"Word count: {word_count}")
print(f"letter count: {letter_count}")
#print(content)
content1=content[:18000]
DEFAULT_SYSTEM_PROMPT0 = """\
You are an assistant. Your answers should be based on your following the data.
If a question does not make any sense, or is not factually coherent, explain why instead of answering something not correct. If you don't know the answer to a question, please don't share false information."""

#concatenate text in DEFAULT_SYSTEM_PROMPT with content
new_content = DEFAULT_SYSTEM_PROMPT0 + content1
#print(new_content[:1000])   #print first 1000 characters of new_content
word_count = len(new_content.split())
letter_count = len(new_content)
print(f"in cut Word count: {word_count}")
print(f"in cut letter count: {letter_count}")
file.close()
