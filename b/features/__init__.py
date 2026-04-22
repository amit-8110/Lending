'''
specific feature a complete package, that use core or services.

(use when apk grows bigger)

features/: (Payment, Login, Auth)
├── payment/
│   ├── payment.py

services/
├── external/
│   ├── payment_gateway_api.py

Now flow becomes:

    `API → feature(this use: service (inside payment) → DB/external`


Early stage:
    don't need feature/

    `api/ → services/`

Later stage (refactor):

    `api/ -> features/

'''


'''
app/
├── core/                 # config, auth infra, logging, User
├── db/                   # DB engine, session, base
├── shared/               # reusable logic (optional)
│
├── features/
│   ├── payment/
│   │   ├── api.py
│   │   ├── service.py
│   │   ├── models.py
│   │   └── schemas.py
│   │
│   ├── auth/
│   │   ├── api.py
│   │   ├── service.py
│   │   ├── models.py
│   │   └── schemas.py


'''