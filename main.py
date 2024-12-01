import google.generativeai as genai
import pyttsx3 



def speak_text(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
# Configure the Generative AI API with your API key
genai.configure(api_key="Your_API_KEY")

# Initialize the model
model = genai.GenerativeModel("gemini-1.5-flash")
# Function to generate AI response
def generate_ai_response(query):
    # Generate content based on the user's query
    response = model.generate_content(query)
    return response.text

if __name__ == "__main__":
    print("Welcome to the AI prompt generator!")
    while True:
        user_query = input("\nYou: ")
        if user_query.lower() == 'exit':
            print("Goodbye!")
            break
        
        
        try:
            ai_response = generate_ai_response(user_query)
            print(f"\nAI: {ai_response}")
            speak_text(ai_response)
        except Exception as e:
            print(f"An error occurred: {e}")