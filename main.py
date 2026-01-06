def lambda_handler(event, context):
    intent = event['request']['intent']['name']
    slots = {k: v.get('value') for k, v in event['request']['intent']['slots'].items()}
    user_id = event['session']['user']['userId']

    from functions.handlers import run_intent
    result = run_intent(intent, slots, user_id)
    return {
        "version": "1.0",
        "response": {
            "outputSpeech": {
                "type": "PlainText",
                "text": f"{result}"
            },
            "shouldEndSession": True
        }
    }
