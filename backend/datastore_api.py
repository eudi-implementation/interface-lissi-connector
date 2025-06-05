import requests
import os
from dotenv import load_dotenv
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')

# Load environment variables from ..env file
load_dotenv()

# Read from environment
DC4EU_API_BASE = os.getenv("DC4EU_API_BASE")

def ehic_from_datastore(webhook_data, collect_id):
    """
    Calls the dc4eu datastore API to collect the EHIC using the data from the webhook of the Lissi connector.
    """
    claims_dict = webhook_data.get("presentation").get("extracted")
    logging.info(f'Extracted claims: {claims_dict}')

    payload = {
        "authentic_source": "authentic_source_" + claims_dict["nationality"].lower(),
        "collect_id": collect_id,
        "document_type": "EHIC",
        "identity": {
            "authentic_source_person_id": claims_dict["authentic_source_person_id"],
            "birth_city": "",
            "birth_country": "",
            "birth_date": claims_dict["birth_date"],
            "birth_place": "",
            "birth_state": "",
            "family_name": claims_dict["last_name"],
            "family_name_at_birth": "",
            "gender": "",
            "given_name": claims_dict["first_name"],
            "given_name_at_birth": "",
            "nationality": "",
            "resident_address": "",
            "resident_city": "",
            "resident_country": "",
            "resident_house_number": "",
            "resident_postal_code": "",
            "resident_state": "",
            "resident_street": "",
            "schema": {
                "name": "DefaultSchema",
                "version": "1.0.0"
            }
        }
    }

    try:
        logging.info('Calling dc4eu datastore API')
        url = f"{DC4EU_API_BASE}document/collect_id"
        response = requests.post(url, json=payload)
        response.raise_for_status()

        logging.info(f'dc4eu datastore call successful: {response.json()}')

        api_data = response.json()
        document_data = api_data["data"]["document_data"]

        mapped_form = {
            'validFrom': '2024-01-29T15:38:01.569Z',
            'validUntil': '2030-01-30T15:38:01.569Z',
            'subjectClaims': document_data
        }

        logging.info(f'Mapping successful: {mapped_form}')

        return mapped_form
    except Exception as e:
        logging.exception('Exception occurred while calling dc4eu datastore API')
        return {"error": str(e)}

def pda1_from_datastore(webhook_data, collect_id):
    """
    Calls the dc4eu datastore API to collect the EHIC using the data from the webhook of the Lissi connector.
    """
    claims_dict = webhook_data.get("presentation").get("extracted")
    logging.info(f'Extracted claims: {claims_dict}')

    payload = {
        "authentic_source": "authentic_source_" + claims_dict["nationality"].lower(),
        "collect_id": collect_id,
        "document_type": "PDA1",
        "identity": {
            "authentic_source_person_id": claims_dict["authentic_source_person_id"],
            "birth_city": "",
            "birth_country": "",
            "birth_date": claims_dict["birth_date"],
            "birth_place": "",
            "birth_state": "",
            "family_name": claims_dict["last_name"],
            "family_name_at_birth": "",
            "gender": "",
            "given_name": claims_dict["first_name"],
            "given_name_at_birth": "",
            "nationality": "",
            "resident_address": "",
            "resident_city": "",
            "resident_country": "",
            "resident_house_number": "",
            "resident_postal_code": "",
            "resident_state": "",
            "resident_street": "",
            "schema": {
                "name": "DefaultSchema",
                "version": "1.0.0"
            }
        }
    }

    try:
        logging.info('Calling dc4eu datastore API')
        url = f"{DC4EU_API_BASE}document/collect_id"
        response = requests.post(url, json=payload)
        response.raise_for_status()

        logging.info(f'dc4eu datastore call successful: {response.json()}')

        api_data = response.json()
        document_data = api_data["data"]["document_data"]

        mapped_form = {
            'validFrom': '2024-01-29T15:38:01.569Z',
            'validUntil': '2030-01-30T15:38:01.569Z',
            'subjectClaims': document_data
        }

        logging.info(f'Mapping successful: {mapped_form}')

        return mapped_form
    except Exception as e:
        logging.exception('Exception occurred while calling dc4eu datastore API')
        return {"error": str(e)}

def upload_to_datastore():
    """
    Calls the dc4eu datastore API to collect the EHIC using the data from the webhook of the Lissi connector.
    """

    payload = {
        "document_data": {
            "decision_legislation_applicable": {
                "ending_date": '2038-01-19',
                "member_state_which_legislation_applies": 'AT',
                "starting_date": '1878-11-17',
                "transitional_rule_apply": False
            },
            "details_of_employment": [
                {
                    "ids_of_employer": [{"employer_id": 'f7c317dc', "type_of_id": '01'}],
                    "name": 'Corp inc.',
                    "type_of_employment": '01',
                    "address": {
                        "country": 'AT',
                        "post_code": '4810',
                        "street": 'Franz-Josef-Platz 3',
                        "town": 'Gmunden'
                    }
                }
            ],
            "nationality": ['AT'],
            "places_of_work": [
                {
                    "a_fixed_place_of_work_exist": False,
                    "country_work": 'AT',
                    "place_of_work": [
                        {
                            "flag_state_home_base": 'AT',
                            "ids_of_company": [{"company_id": '3615c840', "type_of_id": '01'}],
                            "address": {
                                "post_code": '1060',
                                "street": 'Stumpergasse 48/8',
                                "town": 'Wien'
                            },
                            "company_vessel_name": 'vessel_name_at'
                        }
                    ]
                }
            ],
            "social_security_pin": '315-95-2501',
            "status_confirmation": '01',
            "unique_number_of_issued_document": 'asd123',
            "competent_institution": {
                "country_code": 'AT',
                "institution_id": 'AT:1234',
                "institution_name": 'institution_name_at'
            }
        },
        "document_data_version": '1.0.0',
        "document_display": {
            "version": '1.0.0',
            "type": 'PDA1',
            "description_structured": {"at": 'aussteller', "en": 'issuer'}
        },
        "identities": [
            {
                "authentic_source_person_id": '20000',
                "schema": {"name": 'DefaultSchema', "version": '1.0.0'},
                "family_name": 'Meitner',
                "given_name": 'Lise',
                "birth_date": '1878-11-17',
                "family_name_at_birth": '',
                "given_name_at_birth": '',
                "birth_place": '',
                "gender": '',
                "birth_country": '',
                "birth_state": '',
                "birth_city": '',
                "resident_address": '',
                "resident_country": '',
                "resident_state": '',
                "resident_city": '',
                "resident_postal_code": '',
                "resident_street": '',
                "resident_house_number": '',
                "nationality": ''
            }
        ],
        "meta": {
            "authentic_source": 'authentic_source_at',
            "document_version": '1.0.0',
            "document_type": 'PDA1',
            "document_id": 'document_id_20000',
            "real_data": False,
            "collect": {"id": 'collect_id_20000', "valid_until": 2147520172},
            "revocation": {
                "id": '9da40dc0',
                "revoked": False,
                "reference": {
                    "authentic_source": 'authentic_source_at',
                    "document_type": 'PDA1',
                    "document_id": 'document_id_20000'
                },
                "revoked_at": 0,
                "reason": ''
            },
            "valid_from": 1,
            "valid_to": 2147520172,
            "document_data_validation": ''
        },
    }

    try:
        logging.info('Uploading to dc4eu datastore API')
        url = f"{DC4EU_API_BASE}upload"
        response = requests.post(url, json=payload)
        response.raise_for_status()

        logging.info(f'dc4eu datastore call successful: {response.json()}')

        return response.json()
    except Exception as e:
        logging.exception('Exception occurred while calling dc4eu datastore API')
        return {"error": str(e)}