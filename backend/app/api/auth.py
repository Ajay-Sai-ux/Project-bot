from fastapi import APIRouter, Request
from fastapi.responses import RedirectResponse
from app.core.kite import kite, api_secret

router = APIRouter()

@router.get("/login-url")
def get_login_url():
    login_url = kite.login_url()
    return RedirectResponse(login_url)


@router.get("/callback")
def callback(request: Request):
    request_token = request.query_params.get("request_token")
    if not request_token:
        return {"error": "Missing request_token"}

    try:
        session = kite.generate_session(request_token, api_secret)
        access_token = session["access_token"]

        with open("access_token.txt", "w") as f:
            f.write(access_token)

        # ✅ After saving token, redirect to frontend dashboard
        return RedirectResponse("http://localhost:3000/dashboard")

    except Exception as e:
        return {"error": str(e)}