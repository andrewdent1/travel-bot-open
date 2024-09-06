from flask import Flask, render_template, request
import openai

app = Flask(__name__)

# Set up the OpenAI API Key
openai.api_key = "sk-InN9XJHbFcucdJhJA6QfBMl6Irn25UCvT8PWiuTodlT3BlbkFJKugXtXrCllL9l5vZQV7LYAVounloJnRNYwQidwdZwA"  # Replace with your actual OpenAI API key

# Function to send the prompt to OpenAI and get the travel itinerary
def get_chatgpt_response(place, duration, activities, extra_info):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Choose the appropriate GPT model
        messages=[
            {"role": "system", "content": "You are a helpful assistant that provides travel itineraries."},
            {"role": "user", "content": f"""
            I want to plan a trip to {place} for {duration}. 
            Here are some activities I want to do: {activities}.
            Additional information: {extra_info if extra_info else "No additional info."}
            
            Can you provide a detailed travel itinerary, including suggestions for things to do and see based on my preferences?
            """}
        ],
        max_tokens=500,  # Adjust based on how much information you want in the response
        temperature=0.7  # Adjust for creativity level
    )

    return response.choices[0].message['content'].strip()

# Route for the home page where the form is located
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle form submission and generate the itinerary
@app.route('/generate_itinerary', methods=['POST'])
def generate_itinerary():
    place = request.form.get('place')
    duration = request.form.get('duration')
    activities = request.form.get('activities')
    extra_info = request.form.get('extra')

    if place and duration and activities:
        # Generate itinerary using OpenAI GPT
        itinerary = get_chatgpt_response(place, duration, activities, extra_info)

        # Return the itinerary to the front-end
        return render_template('itinerary.html', itinerary=itinerary)
    else:
        return "Error: Please fill in all required fields."

if __name__ == '__main__':
    app.run(debug=True)
