from api.helper.chat.setup import generate_prompt_for_tour_place
from api.helper.chat import initialize_messages, add_message, generate_chat_response
import json

async def recommandation(user_prefrence, db):
    prompt = await generate_prompt_for_tour_place(db)
    message = message = "Can you help me find the best places to visit and the best events to attend? Based on my preferences, I would like to visit a place with a beach and a museum. If successful in fetching data, please return the recommendations in the specified JSON format: {\"status\": \"success\", \"summary\": \"Write a summary of the analysis in one hundred words\", \"data\": [{\"_id\": \"123\", \"data_type\": \"tour_place\"}, {\"id\": \"456\", \"data_type\": \"event\"}]}. If there's an error, please return {\"status\": \"failed\"}."

    messages = initialize_messages(message)
    add_message(messages,"user", prompt)
    add_message(messages, "user", user_prefrence + "Please only return in format given above")
    response = generate_chat_response(messages)

    response = generate_chat_response(messages)

    try:
        data = json.loads(response)

        if 'status' not in data or data['status'] == 'failed':
            return {'status': 'failed'}

        if data['status'] == 'success' and 'summary' in data and 'data' in data:
            for d in data['data']:
                if 'data_type' in d and '_id' in d:
                    pass
                else:
                    return {'status': 'failed', 'message': 'Invalid data format.'}
            return data
    except json.JSONDecodeError:
        return {'status': 'failed', 'message': 'Failed to decode JSON response.'}

    except Exception as e:
        return {'status': 'failed', 'message': str(e)}


        
         
    

    