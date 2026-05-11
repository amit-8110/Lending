
# ------------------ libraries ------------------

# from fastapi import FastAPI

# # -------------------- files --------------------
# from modules.auth.api.router import auth_router



# fastapi - app
# app = FastAPI()

# app.include_router(auth_router, prefix='/api/auth')


'''
    only pc: uvicorn main:app --reload
    across LN: uvicorn main:app --host 0.0.0.0 --port 8000 --reload
'''

from datetime import datetime, UTC, timezone, timedelta


print(datetime.now(timezone.utc) + timedelta(days=10))