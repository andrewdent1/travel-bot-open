from flask import Flask, render_template, request
import openai

app = Flask(__name__)

# Set up the OpenAI API Key
openai.api_key = "proj_o6NF0xKQALraFXSjqnBKyU4a"

# Function to send the prompt to OpenAI and get the travel itinerary
def get_chatgpt_response(place, duration, activities, extra_info):
    prompt = f"""
    I want to plan a trip to {place} for {duration}. 
    Here are some activities I want to do: {activities}.
    Additional information: {extra_info if extra_info else "No additional info."}

    Can you provide a detailed travel itinerary, including suggestions for things to do and see based on my preferences?
    """

    response = openai.Completion.create(
        engine="text-davinci-003",  # Choose the appropriate GPT model (text-davinci-003 or GPT-4)
        prompt=prompt,
        max_tokens=500,  # Adjust based on how much information you want in the response
        temperature=0.7  # Adjust for creativity level
    )

    return response.choices[0].text.strip()

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
