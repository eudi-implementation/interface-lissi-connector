import requests
import os
import time
from dotenv import load_dotenv
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')

# Load environment variables from ..env file
load_dotenv()

# Read from environment
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
RESOURCE = os.getenv("RESOURCE")
TOKEN_URL = os.getenv("TOKEN_URL")
LISSI_API_BASE = os.getenv("LISSI_API_BASE")

# Token cache
_token_cache = {
    "access_token": None,
    "expires_at": 0
}

def get_access_token():
    now = int(time.time())
    if _token_cache["access_token"] and now < _token_cache["expires_at"] - 60:  # 60s buffer
        logging.info('Using cached access token (expires at %d, now %d)', _token_cache["expires_at"], now)
        return _token_cache["access_token"]
    logging.info('Requesting access token from %s', TOKEN_URL)
    if not CLIENT_ID or not CLIENT_SECRET:
        logging.error('CLIENT_ID and/or CLIENT_SECRET not set in environment')
        raise ValueError("CLIENT_ID and CLIENT_SECRET must be set in ..env")

    data = {
        "grant_type": "client_credentials",
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "resource": "api://"+RESOURCE
    }

    try:
        response = requests.post(TOKEN_URL, data=data)
        logging.info('Token endpoint response status: %d', response.status_code)
        if response.status_code != 200:
            logging.error('Failed to get token: %s %s', response.status_code, response.text)
            raise Exception(f"Failed to get token: {response.status_code} {response.text}")
        token_json = response.json()
        _token_cache["access_token"] = token_json["access_token"]
        _token_cache["expires_at"] = int(token_json.get("expires_on", now + int(token_json.get("expires_in", 3600))))
        logging.info('Access token received successfully, expires at %d', _token_cache["expires_at"])
        return _token_cache["access_token"]
    except Exception as e:
        logging.exception('Exception occurred while getting access token')
        raise

def get_lissi_credential_templates():
    logging.info('Requesting Lissi credential-templates from API')
    try:
        token = get_access_token()
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }

        url = f"{LISSI_API_BASE}credential-templates"
        logging.info('Sending GET request to %s', url)

        response = requests.get(url, headers=headers)
        logging.info('Lissi credential-templates endpoint response status: %d', response.status_code)
        if response.status_code != 200:
            logging.error('Error response from Lissi credential-templates endpoint: %s', response.text)
            return {"error": response.text}
        logging.info('Lissi credential-templates received successfully')
        return response.json()
    except Exception as e:
        logging.exception('Exception occurred while getting Lissi credential-templates')
        return {"error": str(e)}

def issue_credential_hoeger():
    logging.info('Issuing credential via Lissi API (pre-authorized flow) for Hoeger, Hollis')
    try:
        token = get_access_token()
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }
        url = f"{LISSI_API_BASE}issuance-sessions"
        payload = {
            "flow":{
                "preAuthorizedCode": {
                "oneTimePassword": "false"
                },
            },
            "credentialTemplateName": "ID-Card-min",
            "revocable": True,
            "validFrom": "2024-01-29T15:38:01.569Z",
            "validUntil": "2030-01-30T15:38:01.569Z",
            "subjectClaims": {
                "first_name": "Hollis",
                "last_name": "Hoeger",
                "nationality": "AT",
                "authentic_source_person_id": "24",
                "birth_date": "1983-05-05"
            }
        }
        logging.info('Sending POST request to %s', url)
        response = requests.post(url, headers=headers, json=payload)
        logging.info('Issuance-sessions endpoint response status: %d', response.status_code)
        logging.info('Lissi response: %s', response.text)
        if response.status_code not in (200, 201):
            logging.error('Error response from issuance-sessions endpoint: %s', response.text)
            return {"error": response.text}
        logging.info('Credential offer created successfully')
        return response.json()
    except Exception as e:
        logging.exception('Exception occurred while creating credential offer')
        return {"error": str(e)}

def issue_credential_castaneda():
    logging.info('Issuing credential via Lissi API (pre-authorized flow) for Castaneda, Carlos')
    try:
        token = get_access_token()
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }
        url = f"{LISSI_API_BASE}issuance-sessions"
        payload = {
            "flow":{
                "preAuthorizedCode": {
                "oneTimePassword": "false"
                },
            },
            "credentialTemplateName": "ID-Card-min",
            "revocable": True,
            "validFrom": "2024-01-29T15:38:01.569Z",
            "validUntil": "2030-01-30T15:38:01.569Z",
            "subjectClaims": {
                "first_name": "Carlos",
                "last_name": "Castaneda",
                "authentic_source_person_id": "10",
                "nationality": "SE",
                "birth_date": "1970-01-10"
            }
        }
        logging.info('Sending POST request to %s', url)
        response = requests.post(url, headers=headers, json=payload)
        logging.info('Issuance-sessions endpoint response status: %d', response.status_code)
        logging.info('Lissi response: %s', response.text)
        if response.status_code not in (200, 201):
            logging.error('Error response from issuance-sessions endpoint: %s', response.text)
            return {"error": response.text}
        logging.info('Credential offer created successfully')
        return response.json()
    except Exception as e:
        logging.exception('Exception occurred while creating credential offer')
        return {"error": str(e)}

def issue_credential_gm():
    logging.info('Issuing credential via Lissi API (pre-authorized flow) for Goeppert Mayer, Maria')
    try:
        token = get_access_token()
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }
        url = f"{LISSI_API_BASE}issuance-sessions"
        payload = {
            "flow":{
                "preAuthorizedCode": {
                "oneTimePassword": "false"
                },
            },
            "credentialTemplateName": "ID-Card-min",
            "revocable": True,
            "validFrom": "2024-01-29T15:38:01.569Z",
            "validUntil": "2030-01-30T15:38:01.569Z",
            "subjectClaims": {
                "first_name": "Maria",
                "last_name": "Goeppert Mayer",
                "authentic_source_person_id": "10000",
                "nationality": "DE",
                "birth_date": "1906-06-28"
            }
        }
        logging.info('Sending POST request to %s', url)
        response = requests.post(url, headers=headers, json=payload)
        logging.info('Issuance-sessions endpoint response status: %d', response.status_code)
        logging.info('Lissi response: %s', response.text)
        if response.status_code not in (200, 201):
            logging.error('Error response from issuance-sessions endpoint: %s', response.text)
            return {"error": response.text}
        logging.info('Credential offer created successfully')
        return response.json()
    except Exception as e:
        logging.exception('Exception occurred while creating credential offer')
        return {"error": str(e)}

def issue_credential_lm():
    logging.info('Issuing credential via Lissi API (pre-authorized flow) for Meitner, Lise')
    try:
        token = get_access_token()
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }
        url = f"{LISSI_API_BASE}issuance-sessions"
        payload = {
            "flow":{
                "preAuthorizedCode": {
                "oneTimePassword": "false"
                },
            },
            "credentialTemplateName": "ID-Card-min",
            "revocable": True,
            "validFrom": "2024-01-29T15:38:01.569Z",
            "validUntil": "2030-01-30T15:38:01.569Z",
            "subjectClaims": {
                "first_name": "Lise",
                "last_name": "Meitner",
                "authentic_source_person_id": "20000",
                "nationality": "AT",
                "birth_date": "1878-11-17"
            }
        }
        logging.info('Sending POST request to %s', url)
        response = requests.post(url, headers=headers, json=payload)
        logging.info('Issuance-sessions endpoint response status: %d', response.status_code)
        logging.info('Lissi response: %s', response.text)
        if response.status_code not in (200, 201):
            logging.error('Error response from issuance-sessions endpoint: %s', response.text)
            return {"error": response.text}
        logging.info('Credential offer created successfully')
        return response.json()
    except Exception as e:
        logging.exception('Exception occurred while creating credential offer')
        return {"error": str(e)}

def issue_ehic_credential():
    logging.info('Issuing EHIC credential via Lissi API (authorization code flow)')
    try:
        token = get_access_token()
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }
        url = f"{LISSI_API_BASE}issuance-sessions"
        payload = {
            "flow": {"authorizationCode": True},
            "credentialTemplateName": "EHIC2",
            "revocable": True
        }
        logging.info('Sending POST request to %s', url)
        response = requests.post(url, headers=headers, json=payload)
        logging.info('Issuance-sessions endpoint response status: %d', response.status_code)
        logging.info('Lissi response: %s', response.text)
        if response.status_code not in (200, 201):
            logging.error('Error response from issuance-sessions endpoint: %s', response.text)
            return {"error": response.text}
        logging.info('EHIC credential offer created successfully')
        return response.json()
    except Exception as e:
        logging.exception('Exception occurred while creating EHIC credential offer')
        return {"error": str(e)}

def issue_pda1_credential():
    logging.info('Issuing PDA1 credential via Lissi API (authorization code flow)')
    try:
        token = get_access_token()
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }
        url = f"{LISSI_API_BASE}issuance-sessions"
        payload = {
            "flow": {"authorizationCode": True},
            "credentialTemplateName": "PDA1-3",
            "revocable": True
        }
        logging.info('Sending POST request to %s', url)
        response = requests.post(url, headers=headers, json=payload)
        logging.info('Issuance-sessions endpoint response status: %d', response.status_code)
        logging.info('Lissi response: %s', response.text)
        if response.status_code not in (200, 201):
            logging.error('Error response from issuance-sessions endpoint: %s', response.text)
            return {"error": response.text}
        logging.info('PDA1 credential offer created successfully')
        return response.json()
    except Exception as e:
        logging.exception('Exception occurred while creating PDA1 credential offer')
        return {"error": str(e)}


####    VERIFIER    ####
def create_pid_presentation_session():
    logging.info('Creating PID presentation session via Lissi API')
    try:
        token = get_access_token()
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-type": "application/json"
        }
        url = f"{LISSI_API_BASE}presentation-sessions"
        payload = {
            "presentationTemplateName": "PidPresentation2",
        }
        logging.info('Sending POST request to %s', url)
        response = requests.post(url, headers=headers, json=payload)
        logging.info('Issuance-sessions endpoint response status: %d', response.status_code)
        logging.info('Lissi response: %s', response.text)
        if response.status_code not in (200, 201):
            logging.error('Error response from issuance-sessions endpoint: %s', response.text)
            return {"error": response.text}
        logging.info('PidPresentation session created successfully')
        return response.json()
    except Exception as e:
        logging.exception('Exception occurred while creating PidPresentation session')
        return {"error": str(e)}

def create_ehic_presentation_session():
    logging.info('Creating EHIC presentation session via Lissi API')
    try:
        token = get_access_token()
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-type": "application/json"
        }
        url = f"{LISSI_API_BASE}presentation-sessions"
        payload = {
            "presentationTemplateName": "EhicPresentation",
        }
        logging.info('Sending POST request to %s', url)
        response = requests.post(url, headers=headers, json=payload)
        logging.info('Issuance-sessions endpoint response status: %d', response.status_code)
        logging.info('Lissi response: %s', response.text)
        if response.status_code not in (200, 201):
            logging.error('Error response from issuance-sessions endpoint: %s', response.text)
            return {"error": response.text}
        logging.info('EhicPresentation session created successfully')
        return response.json()
    except Exception as e:
        logging.exception('Exception occurred while creating EhicPresentation session')
        return {"error": str(e)}

def create_pda1_presentation_session():
    logging.info('Creating PDA1 presentation session via Lissi API')
    try:
        token = get_access_token()
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-type": "application/json"
        }
        url = f"{LISSI_API_BASE}presentation-sessions"
        payload = {
            "presentationTemplateName": "Pda1Presentation",
        }
        logging.info('Sending POST request to %s', url)
        response = requests.post(url, headers=headers, json=payload)
        logging.info('Issuance-sessions endpoint response status: %d', response.status_code)
        logging.info('Lissi response: %s', response.text)
        if response.status_code not in (200, 201):
            logging.error('Error response from issuance-sessions endpoint: %s', response.text)
            return {"error": response.text}
        logging.info('Pda1Presentation session created successfully')
        return response.json()
    except Exception as e:
        logging.exception('Exception occurred while creating Pda1Presentation session')
        return {"error": str(e)}

def get_presentation_session_status(presentation_session_id):
    logging.info(f'Getting status for presentation session: {presentation_session_id}')
    try:
        token = get_access_token()
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }
        url = f"{LISSI_API_BASE}presentation-sessions/{presentation_session_id}"
        logging.info('Sending GET request to %s', url)
        response = requests.get(url, headers=headers)
        logging.info('Presentation session status endpoint response status: %d', response.status_code)
        if response.status_code != 200:
            logging.error('Error response from presentation session status endpoint: %s', response.text)
            return {"error": response.text}
        logging.info('Presentation session status retrieved successfully')
        return response.json()
    except Exception as e:
        logging.exception('Exception occurred while getting presentation session status')
        return {"error": str(e)}