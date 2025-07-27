import chromadb
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
from dotenv import load_dotenv
import os
import google.generativeai as genai

chroma_client = chromadb.PersistentClient()
collection = chroma_client.get_or_create_collection("quotes")

user_said = "Tenemos un alma inmortal"

result = collection.query(
    query_texts=[user_said],
    n_results=5
)

context = ""
for doc_list, meta_list in zip(result["documents"], result["metadatas"]):
    for quote, meta in zip(doc_list, meta_list):
        quote = quote.strip()
        author = meta.get("author", "Autor desconocido").strip()
        context += f"\"{quote}\", {author}. "

prompt = (
    f"Una persona dice: \"{user_said}\"\n"
    f"Reflexiona sobre esta frase, con un tono elegante y académico, usando estas citas relevantes:\n"
    f"{context}\n"
    f"No olvides de mencionar a alguno de los autores de estas frases."
)

load_dotenv()
genai.configure(api_key=os.environ["GG_TOKEN"])
model = genai.GenerativeModel(model_name='gemini-2.5-flash')
response = model.generate_content(prompt)

print("Prompt del usuario:\n", user_said)
print("\nCitas usadas como contexto:\n", context)
print("\nRespuesta del modelo Gemini:\n", response.text, "\n")


hf_token = os.getenv("HF_TOKEN")
model_id = "HuggingFaceTB/SmolLM2-360M"
tokenizer = AutoTokenizer.from_pretrained(model_id, token=hf_token)
model = AutoModelForCausalLM.from_pretrained(model_id, token=hf_token)

generator = pipeline("text-generation", model=model, tokenizer=tokenizer, device=-1)

responseHF = generator(
    prompt,
    max_new_tokens=200,
    do_sample=True,
    temperature=0.7,
    top_p=0.9,
    num_return_sequences=1,
    repetition_penalty=1.1
)[0]["generated_text"]

print("Respuesta del modelo Hugging Face: \n", responseHF)
