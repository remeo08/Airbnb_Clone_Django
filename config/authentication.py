import jwt   # 추가
from django.conf import settings
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from user.models import User

class TrustMeBroAuthentication(BaseAuthentication):

    def authenticate(self, request):
        username = request.headers.get('Trust-Me')
        if not username:   # (1) 로그인을 시도한 게 아닐 경우
                return None
        try:   # header에 'Trust-Me'가 있었으므로 username을 찾아봄.
                user = User.objects.get(username=username)
                return (user,None)   # (2) 해당 user를 찾음. 인증 성공. 이 user가 우리가 views에서 보는 user=request.user의 user
        except User.DoesNotExist:   # (3) username 넣고 인증 시도했지만 잘 못된 정보인 경우
                raise AuthenticationFailed(f'No user {username}')


class JWTAuthentication(BaseAuthentication):
    def authenticate(self, request):
        token = request.headers.get('Jwt')
        if not token:
            return None
        decoded = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"],)
        print(decoded)
        pk = decoded.get('pk')
        if not pk:
            raise AuthenticationError("Invalid Token")
        try:
            user = User.objects.get(pk=pk)
            return (user, None)
        except User.DoesNotExist:
            raise AuthenticationError("User Not Found")