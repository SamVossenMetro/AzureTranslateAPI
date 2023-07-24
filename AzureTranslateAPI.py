import requests

def translate_text_azure(text, source_language, target_language):
    azure_subscription_key = "9f3df45b03754a2a827bb889aa2d571d"
    azure_endpoint = "https://api.cognitive.microsofttranslator.com/"

    headers = {
        "Ocp-Apim-Subscription-Key": azure_subscription_key,
        "Content-type": "application/json",
        "Ocp-Apim-Subscription-Region": "centralus"  
    }

    url = f"{azure_endpoint}/translate?api-version=3.0&from={source_language}&to={target_language}"

    body = [{"text": text}]
    response = requests.post(url, headers=headers, json=body)

    if response.status_code == 200:
        translated_text = response.json()[0]["translations"][0]["text"]
        return translated_text
    else:
        print(f"Translation error: {response.text}")
        return None

# Example usage:
source_text = "Hello, how are you?"
source_language = "en"  # English
target_language = "es"  # Spanish

translated_text = translate_text_azure(source_text, source_language, target_language)
print(f"Translated text: {translated_text}")