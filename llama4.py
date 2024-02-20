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
#print(content)
#content1=content[:15000]

content1=content[:10000]

DEFAULT_SYSTEM_PROMPT0 = """\
You are an assistant. Your answers should be based on your following the data.
If a question does not make any sense, or is not factually coherent, explain why instead of answering something not correct. If you don't know the answer to a question, please don't share false information."""

#concatenate text in DEFAULT_SYSTEM_PROMPT with content
new_content = DEFAULT_SYSTEM_PROMPT0 + content1
#print(new_content[:1000])   #print first 1000 characters of new_content


file.close()

DEFAULT_SYSTEM_PROMPT=new_content

word_count = len(new_content.split())
letter_count = len(new_content)
print(f"in cut Word count: {word_count}")
print(f"in cut letter count: {letter_count}")


#model_path = "C:\gguf1\llama-2-7b-chat.Q2_K.gguf"
model_path ="C:\gguf1\llama-2-7b-chat.ggmlv3.q4_K_M.bin"
# Create a llama model
model = Llama(model_path=model_path, n_ctx=4096)

# Prompt creation
system_message = new_content

user_message = "what is Catalyst 9200 ?"

questions = ["what is Catalyst 9200 ?", " What is Fast PoE ?", "What are Flexible downlink options ?", "what are uplinks ?", "does it have encryption ?", "what is the power supply ?", "what is the warranty?"]
# Model parameters
max_tokens = 4096
file1 = open('answers4.txt', 'w')
# Run the model
kwargs = dict(temperature=0.6, top_p=0.9)
kwargs["max_tokens"] = max_tokens
start0 = time.time()
print(f"model :\t start 0: {(start0):.03f}ms   ")
endp=start0
for question in questions:
    user_message = question    
    prompt = f"""<s>[INST] <<SYS>>
    {system_message}
    <</SYS>>
    {user_message} [/INST]"""
    start = time.time()
    #output = model(prompt,  max_tokens=max_tokens, echo=True)
    output = model(prompt,  stream=True, **kwargs)
    # Print the model output
    end = time.time()
    print('output')
    print('----------------------------------------------------')
    print(f"model :\tTime : {(end):.03f}ms   ")
    file1.write(f"model :\tTime : {(end):.03f}ms   ")
    print(output)
    file1.write(question)
    file1.write('\n')
    file1.write(f"Time taken in loop {(end-start0)*10**3:.03f}ms   \n")
    file1.write(f"Time taken in question {(end-endp)*10**3:.03f}ms  \n")
    endp=end
    answer = ""
    for chunk in output:
        token = chunk["choices"][0]["text"]
        answer += token

    print('----------------------------------------------------')
    print('answer---------------------------------------------')
    print(answer)
    file1.write(answer)
    file1.write('\n')

file1.close()
