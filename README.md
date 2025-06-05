# Interface for Lissi Connector

This repository offers an interface for the [Lissi Connector](https://www.lissi.id/de/eudi-wallet-connector).
Furthermore, it pulls the data for credentials from the [DC4EU datastore](https://github.com/dc4eu/vc).

Note that this repo will only run if you have access to a Lissi Connector Tenant.
The tenant has to be configured correctly (credential & presentation templates; see [Lissi Docu](https://help.lissi.id)).

## Running the Lissi Interface

#### 1. Set up environment variables
First, you need to set up an `.env` file that contains:

- `CLIENT_ID`
- `CLIENT_SECRET`
- `RESOURCE`
- `TOKEN_URL`
- `LISSI_API_BASE`
- `DC4EU_API_BASE`

`.env.example` contains an example setup.

#### 2. Change appearance (if desired)

- `static/corporate.css` contains all CD-related styling (especially colors).
- If you replace the Logos, change the files in `frontend/` accordingly.

#### 3. Run the Interface

- Create a virtual environment:
    ```bash
    python3 -m venv .venv
    ```
- Activate virtual environment:
    ```bash
    . .venv/bin/activate
    ```
- Install or upgrade _pip_:
    ```bash
    python -m pip install --upgrade pip
    ```
- Install requirements:
    ```bash
    pip install -r requirements.txt
    ```
- Run interface:
    ```bash
    uvicorn backend.main:app --host 0.0.0.0 --port 8000
    ```
  
With this, the interface is running on `http://your.local.ip.address:8000`.
A verifier is available on `http://your.local.ip.address:8000/verifier`.

## Available Credentials

The interface currently offers the following credentials:

- Pre-configured PIDs for 4 example personas (using the pre-authorized code flow).
    If you want to change them, you can do so in `backend/lissi_api.py`.
- EHICs (authorization flow with PID authentication).
- PDA1 (authorization flow with PID authentication).

To receive an EHIC or PDA1 credential, you need to specify the Collect ID of the specific document in the DC4EU datastore.
Furthermore, the authorization flow with PID requires you to hold the right PID in your wallet.
The pre-configured PIDs contain the minimal required information to collect the following credentials:

- Hoeger:
  - PDA1 w/ Collect ID: "collect_id_24"
- Castaneda:
  - EHIC w/ Collect ID: "collect_id_10"
- Goeppert Mayer:
  - EHIC w/ Collect ID: "collect_id_10000"
  - EHIC w/ Collect ID: "collect_id_10001"
  - EHIC w/ Collect ID: "collect_id_10002"
  - EHIC w/ Collect ID: "collect_id_10003"
- Meitner:
  - PDA1 w/ Collect ID: "collect_id_20000"

Note that "Goeppert Mayer" and "Meitner" aren't in the initial example dataset of the DC4EU datastore (i.e. the documents they can collect aren't initially present and have to be added manually).

## Add Documents to DC4EU datastore

The button "Add Hardcoded Document" allows you to add document to the DC4EU datastore.
The document to be added is hardcoded in `backend/datastore_api.py`.
Change the hardcoded payload there according to your needs.

The payload to add a PDA1 document for "Meitner" looks like:
```python
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
```
The payload to add an EHIC document for "Goeppert Mayer" looks like:
```python
payload = {
        "document_data": {
            "competent_institution": {
                "institution_country": 'DE',
                "institution_id": 'DE:1234',
                "institution_name": 'institution_name_de'
            },
            "document_id": 'document_id_10000',
            "period_entitlement": { "ending_date": '2038-01-19', "starting_date": '1833-10-21' },
            "social_security_pin": '12345',
            "subject": {
                "date_of_birth": '1906-06-28',
                "family_name": 'Goeppert Mayer',
                "forename": 'Maria'
            }
        },
        "document_data_version": '1.0.0',
        "document_display": {
            "version": '1.0.0',
            "type": 'EHIC',
            "description_structured": {"de": 'aussteller', "en": 'issuer'}
        },
        "identities": [
            {
                "authentic_source_person_id": '10000',
                "schema": {"name": 'DefaultSchema', "version": '1.0.0'},
                "family_name": 'Goeppert Mayer',
                "given_name": 'Maria',
                "birth_date": '1906-06-28',
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
            "authentic_source": 'authentic_source_de',
            "document_version": '1.0.0',
            "document_type": 'EHIC',
            "document_id": 'document_id_10000',
            "real_data": False,
            "collect": {"id": 'collect_id_10000', "valid_until": 2147520172},
            "revocation": {
                "id": '9da40dc0',
                "revoked": False,
                "reference": {
                    "authentic_source": 'authentic_source_de',
                    "document_type": 'EHIC',
                    "document_id": 'document_id_10000'
                },
                "revoked_at": 0,
                "reason": ''
            },
            "valid_from": 1,
            "valid_to": 2147520172,
            "document_data_validation": ''
        },
    }
```

## Session -> Collect ID Map

To realize the binding of Collect IDs to a specific credential offer, we had to store the Session ID (which is created when starting the credential offer process) together with the respective Collect ID.
The resulting map is persistent across restarts and can be manually emptied by pressing the "Clear Session -> Collect ID Map" button.

## Verification of Credentials

The verifier is running on `http://your.local.ip.address:8000/verifier`.
The verifier can generate presentation requests for PIDs, EHICs, and PDA1s.
The button "Show Last Verification Result" displays the status of the last verification/presentation session that was initialized by the verifier.
The result of the verification is also always shown on the wallet's device afterward.