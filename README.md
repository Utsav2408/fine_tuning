# fine-tuning Llama3.2 to answer administrative queries of AgentE
To set this up, follow the steps below -

1. Download the folder "data" from the following GDrive link (consists of 11 PDFs) and keep it at the root directory
https://drive.google.com/drive/folders/1TUfpAyzBVWhjUEm95FD-5Q1rh1n1X8T4?usp=sharing
2. Install uv - pip install uv (If not done already)
3. Install important packages -
For Data Preprocessing: uv add docling litellm colorama
For Training: uv add datasets transformers torch bitsandbytes peft trl colorama
Note - Make sure you have GPU enabled, as this throws unexpected errors sometimes.
4. Data Pre-processing ->
Note - Make sure you have an Open API Key in your .env while running the following files, if not, make sure to use a different model with litellm
-> run synthetic_data_generator.py
-> run preprocessing.py
-> run merge_data.py
-> run dataquality.py
This creates a folder "final" consisting of the final_json with the following structure:
{
    "question": "",
    "answer": ""
}
5. Training with LoRA
Note - Make sure you have a token of Hugging Face in your .env, and access to Llama Models in Hugging Face.
-> run train.py

This will generate a folder with adapter_config.json and adapter_tensors.
This can then be used to create a model.
Here we use Ollama

6. Create Model
Note -> Make sure to update your directory in Modelfile, and Modelfile is in the root directory.
-> ollama create {name} -f Modelfile

This will add the model to your ollama, such that you can infer it.

7. Inference Model
Here we use Langflow to infer.
Create chat input, ollama, and output node.
You can go ahead with a greedy or dynamic approach. We tested it with topk=1, i.e, greedy approach

Finally, you can get a Langflow API token, capture its API, and run it on your machine to test it out 
(Expert tip: If in FastAPI, use httpx; it's better than request.)
