from transformers import AutoTokenizer, AutoModelForSeq2SeqLM


model_name = "facebook/blenderbot-400M-distill"
# Load model (download on first run and reference local installation for consequent runs)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

conversation_history = []

def chat(input_text):
    history_string = "\n".join(conversation_history)

    inputs = tokenizer.encode_plus(history_string, input_text, return_tensors="pt")

    tokenizer.pretrained_vocab_files_map
    outputs = model.generate(**inputs)

    response = tokenizer.decode(outputs[0], skip_special_tokens=True).strip()

    conversation_history.append(input_text)
    conversation_history.append(response)

    return response