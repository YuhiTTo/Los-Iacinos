import google.generativeai as genai

def configure_model(api_key):
    genai.configure(api_key=api_key)
    
    generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 64,
        "max_output_tokens": 8192,
        "response_mime_type": "text/plain",
    }

    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config=generation_config,
    )
    return model

def start_chat_session(model):
    # Iniciar una nueva sesión de chat con un historial vacío
    chat_session = model.start_chat(history=[])
    return chat_session

def send_message(chat_session, pregunta):
    response = chat_session.send_message(pregunta)
    return response.text

def chat_loop(api_key):
    model = configure_model(api_key)
    chat_session = start_chat_session(model)

    print("¡Hola! Soy un chatbot impulsado por GEMINI. Escribe algo para comenzar:")

    while True:
        user_input = input("Tú: ")
        if user_input.lower() in ["salir", "exit", "quit"]:
            print("¡Adiós!")
            break

        respuesta = send_message(chat_session, user_input)
        print(f"Chatbot: {respuesta}")

# Configura tu clave API aquí
api_key = "AIzaSyBEnFMCSY4csBGAVuBptvXqYicWHkBr8hQ"

# Iniciar el loop del chatbot
chat_loop(api_key)

