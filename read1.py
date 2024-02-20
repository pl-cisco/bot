file = open("output2.txt", "r")
content = file.read()
#count number of words in content
word_count = len(content.split())
print(f"Word count: {word_count}")
#print(content)
word_count = len(content)
print(f"letter count: {word_count}")
#print(content)
DEFAULT_SYSTEM_PROMPT0 = """\
You are an assistant. Your answers should be based on your following the data.
If a question does not make any sense, or is not factually coherent, explain why instead of answering something not correct. If you don't know the answer to a question, please don't share false information."""

#concatenate text in DEFAULT_SYSTEM_PROMPT with content
new_content = DEFAULT_SYSTEM_PROMPT0 + content
#print(new_content[:1000])   #print first 1000 characters of new_content


file.close()