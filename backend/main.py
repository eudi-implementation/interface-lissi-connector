from fastapi import FastAPI, Request, Body
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, JSONResponse

from backend.lissi_api import get_lissi_credential_templates, issue_credential_hoeger, issue_credential_castaneda, \
    issue_credential_gm, issue_credential_lm, issue_ehic_credential, issue_pda1_credential, \
    create_pid_presentation_session, create_ehic_presentation_session, create_pda1_presentation_session, \
    get_presentation_session_status
from backend.datastore_api import ehic_from_datastore, pda1_from_datastore, upload_to_datastore
from backend.utils import load_session_map, save_session_map, SESSION_MAP_LOCK


app = FastAPI()

# Serve frontend
app.mount("/static", StaticFiles(directory="static"), name="static")



@app.get("/")
def index():
    return FileResponse("frontend/index.html")


@app.get("/api/credential-templates")
def credential_templates():
    return get_lissi_credential_templates()


@app.post("/api/issue-credential-hoeger")
def issue_credential_endpoint():
    return issue_credential_hoeger()


@app.post("/api/issue-credential-castaneda")
def issue_credential_endpoint():
    return issue_credential_castaneda()


@app.post("/api/issue-credential-gm")
def issue_credential_endpoint():
    return issue_credential_gm()


@app.post("/api/issue-credential-lm")
def issue_credential_endpoint():
    return issue_credential_lm()


@app.post("/api/add-hardcoded-document")
def add_hardcoded_document():
    return upload_to_datastore()


@app.post("/api/issue-ehic")
def issue_ehic_credential_endpoint(payload: dict = Body(...)):
    collect_id = payload.get("collectId")
    print(f"Collect ID: {collect_id}")
    result = issue_ehic_credential()
    session_id = result.get("id")
    if session_id and collect_id:
        with SESSION_MAP_LOCK:
            session_map = load_session_map()
            session_map[session_id] = collect_id
            save_session_map(session_map)
    return result


@app.post("/api/issue-pda1")
def issue_pda1_credential_endpoint(payload: dict = Body(...)):
    collect_id = payload.get("collectId")
    print(f"Collect ID: {collect_id}")
    result = issue_pda1_credential()
    session_id = result.get("id")
    if session_id and collect_id:
        with SESSION_MAP_LOCK:
            session_map = load_session_map()
            session_map[session_id] = collect_id
            save_session_map(session_map)
    return result


@app.post("/api/clear-session-map")
def clear_session_map():
    with SESSION_MAP_LOCK:
        try:
            save_session_map({})
            return {"success": True}
        except Exception as e:
            return {"success": False, "error": str(e)}


@app.get("/api/view-session-map")
def view_session_map():
    with SESSION_MAP_LOCK:
        try:
            session_map = load_session_map()
            return session_map
        except Exception as e:
            return {"error": str(e)}


@app.post("/EHIC")
async def ehic_webhook(request: Request):
    data = await request.json()
    session_id = data.get("issuance").get("sessionId")
    with SESSION_MAP_LOCK:
        session_map = load_session_map()
        collect_id = session_map.get(session_id)
    result = ehic_from_datastore(data, collect_id)
    if isinstance(result, dict) and "error" in result:
        return JSONResponse(result, status_code=400)
    return JSONResponse(result, status_code=200)


@app.post("/PDA1")
async def pda1_webhook(request: Request):
    data = await request.json()
    session_id = data.get("issuance").get("sessionId")
    with SESSION_MAP_LOCK:
        session_map = load_session_map()
        collect_id = session_map.get(session_id)
    print(collect_id)
    result = pda1_from_datastore(data, collect_id)
    if isinstance(result, dict) and "error" in result:
        print("ERROR")
        return JSONResponse(result, status_code=400)
    return JSONResponse(result, status_code=200)


####    VERIFIER    ####
@app.get("/verifier")
def verifier():
    return FileResponse("frontend/verifier.html")


@app.post("/api/verifier/pid-presentation-session")
def create_verifier_presentation_session():
    return create_pid_presentation_session()


@app.post("/api/verifier/ehic-presentation-session")
def create_verifier_presentation_session():
    return create_ehic_presentation_session()


@app.post("/api/verifier/pda1-presentation-session")
def create_verifier_presentation_session():
    return create_pda1_presentation_session()


@app.get("/api/verifier/presentation-session-status/{presentation_session_id}")
def verifier_presentation_session_status(presentation_session_id: str):
    return get_presentation_session_status(presentation_session_id)


@app.get("/verifier/result")
def verifier_result():
    return FileResponse("frontend/callback.html")