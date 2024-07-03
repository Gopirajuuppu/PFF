Python version: 3.11.0
 
create creds.env file in the root folder 
Actual OpenAI Key (Not Azure OpenAI)
Azure Key and Azure Region is needed for STT and TTS
```bash
MODEL_NAME="gpt-3.5-turbo-1106"
OPENAI_API_KEY = "sk-.."
AZURE_KEY = "..."
AZURE_REGION = "eastus"
```
 
python3 -m pip install -r requirements.txt --no-cache-dir
 
streamlit run MedGPT.py