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
content1=content[:10000]
DEFAULT_SYSTEM_PROMPT0 = """\
You are an assistant. Your answers should be based on your following the data.
If a question does not make any sense, or is not factually coherent, explain why instead of answering something not correct. If you don't know the answer to a question, please don't share false information."""

#concatenate text in DEFAULT_SYSTEM_PROMPT with content
new_content = DEFAULT_SYSTEM_PROMPT0 + content1
#print(new_content[:1000])   #print first 1000 characters of new_content


file.close()

DEFAULT_SYSTEM_PROMPT=new_content


def format_to_llama_chat_style(history) -> str:
    # history has the following structure:
    # - dialogs
    # --- instruction
    # --- response (None for the most recent dialog)
    prompt = ""
    for i, dialog in enumerate(history[:-1]):
      instruction, response = dialog[0], dialog[1]
      # prepend system instruction before first instruction
      if i == 0:
        instruction = f"{B_SYS}{DEFAULT_SYSTEM_PROMPT}{E_SYS}" + instruction
      else:
        # the tokenizer automatically adds a bos_token during encoding,
        # for this reason the bos_token is not added for the first instruction
        prompt += BOS
      prompt += f"{B_INST} {instruction.strip()} {E_INST} {response.strip()} " + EOS

    # new instruction from the user
    new_instruction = history[-1][0].strip()

    # the tokenizer automatically adds a bos_token during encoding,
    # for this reason the bos_token is not added for the first instruction
    if len(history) > 1:
      prompt += BOS
    else:
      # prepend system instruction before first instruction
      new_instruction = f"{B_SYS}{DEFAULT_SYSTEM_PROMPT}{E_SYS}" + new_instruction

    prompt += f"{B_INST} {new_instruction} {E_INST}"

    #prompt1=prompt [:4000] #
    return prompt