import re
from fastapi import Request
from fastapi.responses import JSONResponse
from app.infrastructure.config.app import settings

cors = f"{settings.cors}"

allowed_origin_pattern = re.compile(fr"{cors}")

async def cors_regex_middleware(request: Request, call_next):
    origin = request.headers.get("origin")
    if origin and allowed_origin_pattern.match(origin):
        if request.method == "OPTIONS":
            # Gérer les requêtes préliminaires (OPTIONS)
            response = JSONResponse(content="OK", status_code=200)
            response.headers["Access-Control-Allow-Origin"] = origin
            response.headers["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE, OPTIONS"
            response.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
            response.headers["Access-Control-Allow-Credentials"] = "true"
            return response

        # Pour les autres requêtes, appliquer les en-têtes après `call_next`
        response = await call_next(request)
        response.headers["Access-Control-Allow-Origin"] = origin
        response.headers["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE, OPTIONS"
        response.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
        response.headers["Access-Control-Allow-Credentials"] = "true"
        return response
        # response = await call_next(request)
        # response.headers["Access-Control-Allow-Origin"] = origin
        # response.headers["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE, OPTIONS"
        # response.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
        # response.headers["Access-Control-Allow-Credentials"] = "true"
        
        # return response
    
    elif origin:
        return JSONResponse(content={"error": "CORS not allowed"}, status_code=403)
    
    return await call_next(request)