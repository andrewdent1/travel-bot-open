from flask import Flask, render_template, request
import openai
import requests

app = Flask(__name__)

# Set up the OpenAI API Key
openai.api_key = "sk-xrXiqFwU2YbxzcOn5Vv2HEDk380KkauWvPW89N-q9dT3BlbkFJ6f77ApysniLb40DqKFQpCSzQw_7v08egMBWnQwiisA"  # Replace with your actual OpenAI API key

# Pinterest API credentials
PINTEREST_ACCESS_TOKEN = "pina_AMAVV4QWAAVJWAQAGAADOCLHYBN4REIBQBIQDQIRF6QMYVZGUDGVYYCRAAWMY5VY5I7GO424R52UD3ATRCP23GKIYVWRNKYA"  # Replace with your Pinterest API token

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

# Function to get Pinterest posts
def get_pinterest_posts(place):
    headers = {
        'Authorization': f'Bearer {PINTEREST_ACCESS_TOKEN}'
    }
    # This is a sample Pinterest API endpoint. You should replace it with the actual endpoint for your use case.
    url = f'https://api.pinterest.com/v1/search/pins/?query={place}&access_token={PINTEREST_ACCESS_TOKEN}'
    response = requests.get(url, headers=headers)
    data = response.json()

    posts = []
    if 'data' in data:
        for pin in data['data'][:10]:  # Get the top 10 posts
            posts.append({
                'image_url': pin['image']['original']['url'],
                'link': pin['url']
            })
    return posts

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

        # Get Pinterest posts related to the place
        pinterest_posts = get_pinterest_posts(place)

        # Return the itinerary and Pinterest posts to the front-end
        return render_template('itinerary.html', itinerary=itinerary, pinterest_posts=pinterest_posts)
    else:
        return "Error: Please fill in all required fields."

if __name__ == '__main__':
    app.run(debug=True)
