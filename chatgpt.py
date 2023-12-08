import urequests
import time

# Información para la API de OpenAI
api_key = "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"
url = "https://api.openai.com/v1/engines/text-davinci-002/completions"

# Función para enviar el prompt a ChatGPT
def send_prompt_to_chatgpt(prompt):
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + api_key
    }

    body = {
        "prompt": prompt,
        "max_tokens": 50
    }

    response = urequests.post(url, headers=headers, json=body)
    return response.text

# Función principal
def main():
    print("Accediendo a ChatGPT desde PicoW")

    # Prompt de ejemplo
    prompt = "¿Cómo está el clima hoy?"
    
    # Enviar el prompt y obtener la respuesta
    response = send_prompt_to_chatgpt(prompt)

    # Mostrar la respuesta
    print("Respuesta de ChatGPT:", response)

if __name__ == "__main__":
    main()
