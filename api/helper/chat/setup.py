from api.helper.db import db
import json

def give_format_for_tour_place(data):
    prompt = "Explore {data['name']} in {data['location']['address']}. "
    prompt += f"{data['description'][0]} "
    prompt += f"Activities include {', '.join(data['category'])}. "
    prompt += f"The weather is {data['Weather']['description']} with an average temperature of {data['Weather']['averageTemp']}°C. "
    return prompt

def give_format_for_event(data):
    prompt = f"Join us for {data['title']}, a {', '.join(data['category'])} event organized by {data['organizer']}. "
    prompt += f"The event will take place on {data['date']} at {data['location']}. "
    prompt += f"{data['description']} "
    prompt += f"Tickets are {data['tickets']['available']} and cost {data['tickets']['price']}. "
    return prompt
    
async def generate_prompt_for_tour_place():
    tours_places = await db['TourPlace'].find().to_list(length=100)
    prompt = []
    prompts_for_tours_places = []
    
    for tour in tours_places:
        prompts_for_tours_places.append({"id": str(tour['_id']), "data": give_format_for_tour_place(tour)})
    prompt.append(json.dumps({"type_of_data": "tour places", "data": prompts_for_tours_places}))
    
    events = await db['events'].find().to_list(length=100)
    prompts_for_events = []
    for event in events:
        prompts_for_events.append({"id": str(event['_id']), "data": give_format_for_event(event)})
    prompt.append(json.dumps({"type_of_data": "events", "data": prompts_for_events}))
    return json.dumps(prompt)
    
