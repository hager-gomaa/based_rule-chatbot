def get_response(user_input:str) -> str:
    text = user_input.strip().lower()
    
    if text in ['hi', 'hello', 'hey']:
        return "Hello! How can I assist you today?" 
    elif text in ['bye', 'goodbye', 'see you']:
        return "Goodbye! Have a great day!"
    elif text in ['how are you?', 'how are you doing?']:
        return "I'm just a bot, but I'm here to help you!"
    elif text in ['what is your name?', 'who are you?']:
        return "I am a friendly chatbot created to assist you."
    elif text in ['can you help me?', 'support']:
        return "Sure! I can help you with various tasks. What do you need assistance with?" 
    elif text in ['thank you', 'thanks']:
        return "You're welcome! If you have any more questions, feel free to ask." 
    elif text=="":
        return "It seems you didn't type anything. Please enter a message so I can assist you." 
    else:
        return "I'm sorry, I didn't understand that. Can you please rephrase?"   
    

def chatbot():
    print("Welcome to the Chatbot! Type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye! Have a great day!")
            break
        response = get_response(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    chatbot()