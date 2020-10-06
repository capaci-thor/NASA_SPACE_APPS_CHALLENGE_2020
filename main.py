from ibm_watson import AssistantV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('TWp-7b3YlrtvtJh0Fnf2CE1c0MF1W6m4BuEtumpFRa0y')
assistant = AssistantV2(
    version='2020-09-24',
    authenticator=authenticator
)

assistant.set_service_url('https://api.us-south.assistant.watson.cloud.ibm.com/instances/d318f6c6-6ed7-4ef8-87f6-24f14bbc3242/v2/assistants/634f7da3-f275-4ac5-974d-cfc0391a2a29/sessions')

response = assistant.message(
    assistant_id='634f7da3-f275-4ac5-974d-cfc0391a2a29',
    session_id='{session_id}',
    input={
        'message_type': 'text',
        'text': 'Hello'
    }
).get_result()

print(json.dumps(response, indent=2))