'''

Authentication
    POST   /auth/register
    POST   /auth/login
    POST   /auth/logout
    POST   /auth/refresh
    GET    /auth/me


Password
    POST   /auth/forgot-password
    POST   /auth/reset-password
    POST   /auth/change-password


Verification
    POST   /auth/send-verification
    POST   /auth/verify-email
    POST   /auth/verify-otp


Session/Device
    GET    /auth/sessions
    DELETE /auth/sessions/{id}
    DELETE /auth/sessions/all


OAuth
    GET    /auth/google
    GET    /auth/google/callback


'''
