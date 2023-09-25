from fastapi import Request, HTTPException
from fastapi.routing import APIRoute

from api.helper.auth import authenticate_user_by_token

async def check_user_role(request: Request, allowed_roles: list):
    user = request.state.user
    if user.role not in allowed_roles:
        raise HTTPException(status_code=403, detail="Not enough permissions")

class RoleBasedMiddleware(APIRoute):
    def get_route_handler(self):
        original_route_handler = super().get_route_handler()

        async def custom_route_handler(request):
            allowed_roles = self.allowed_roles
            await check_user_role(request, allowed_roles)
            return await original_route_handler(request)

        return custom_route_handler
    
async def check_user_auth(request: Request):
    try:
        await authenticate_user_by_token(request)
    except HTTPException:
        raise HTTPException(status_code=401, detail="Invalid token")
    
class AuthMiddleware(APIRoute):
    def get_route_handler(self):
        original_route_handler = super().get_route_handler()

        async def custom_route_handler(request):
            await check_user_auth(request)
            return await original_route_handler(request)

        return custom_route_handler
