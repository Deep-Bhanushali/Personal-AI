# import psutil

# def is_app_running(app_name):
#     for proc in psutil.process_iter(['name']):
#         if proc.info['name'] and app_name.lower() in proc.info['name'].lower():
#             return True
#     return False

# # Example usage
# if is_app_running("WhatsApp"):
#     print("WhatsApp is running")
# else:
#     print("WhatsApp is not running")
# from hugchat import hugchat

# def chatBot(query):
#     user_input = query.lower()
#     chatbot = hugchat.ChatBot(cookie_path="engine/cookies.json")
#     # id = chatbot.new_conversation()
#     # chatbot.change_conversation(id)
#     response =  chatbot.chat(user_input)
#     print(response)
#     # speak(response)
#     # return response

# chatBot("Hello, how are you?")  # Example usage to test the function

# from hugchat import hugchat

# def chatBot(query):
#     chatbot = hugchat.ChatBot(cookie_path="engine/cookies.json")
#     response = chatbot.chat(query)
#     print("Response from chatbot:\n", response)

# # Example call
# chatBot("Tell me something about Iron Man.")
# from hugchat import hugchat
# from hugchat.login import Login
# import os
# import requests
# import traceback

# # Step 1: Log in and generate cookies
# EMAIL = "time56711@gmail.com"
# PASSWD = "123#Timepass"
# cookie_path_dir = "engine/"

# try:
#     if not os.path.exists(cookie_path_dir):
#         os.makedirs(cookie_path_dir)
#     sign = Login(EMAIL, PASSWD)
#     cookies = sign.login(cookie_dir_path=cookie_path_dir, save_cookies=True)
#     print("Cookies generated successfully:", cookies.get_dict())
# except Exception as e:
#     print(f"Login error: {str(e)}")
#     print(traceback.format_exc())
#     exit(1)

# # Step 2: Chatbot function
# def chatBot(query):
#     try:
#         chatbot = hugchat.ChatBot(cookie_path="engine/cookies.json")
#         print("Available models:", chatbot.get_remote_llms())
#         conversation_id = chatbot.new_conversation()
#         chatbot.change_conversation(conversation_id)
#         response = chatbot.chat(query, max_tokens=200)
#         print(f"JARVIS: {response}")
#         return response
#     except Exception as e:
#         print(f"Chatbot error: {str(e)}")
#         print(traceback.format_exc())
#         return None

# # Step 3: Test the chatbot
# chatBot("Hello, how are you?")

# from hugchat.login import Login
# import os
# import requests
# import traceback

# EMAIL = "time56711@gmail.com"
# PASSWD = "123#Timepass"
# cookie_path_dir = "engine/"

# try:
#     if not os.path.exists(cookie_path_dir):
#         os.makedirs(cookie_path_dir)
#     sign = Login(EMAIL, PASSWD)
#     cookies = sign.login(cookie_dir_path=cookie_path_dir, save_cookies=True)
#     print("Cookies generated successfully:", cookies.get_dict())
# except Exception as e:
#     print(f"Login error: {str(e)}")
#     print(traceback.format_exc())
#     try:
#         response = requests.get("https://huggingface.co/login")
#         print(f"Login endpoint status: {response.status_code}")
#         print(f"Login endpoint response (first 500 chars): {response.text[:500]}")
#     except requests.RequestException as re:
#         print(f"Network error: {re}")

import google.generativeai as genai

genai.configure(api_key="AIzaSyAhM_xGRo3TbjVYnbreSWiQf3I06M-oKPQ")
model = genai.GenerativeModel("gemini-1.5-flash-latest")
res = model.generate_content("tell me about iron man")
print(res)