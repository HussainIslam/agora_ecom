import json
from rest_framework.renderers import BrowsableAPIRenderer

class UserLoginJSONRenderer(BrowsableAPIRenderer):
    charset = 'utf-8'
    media_type = 'text/html'
    format='api'
    template = 'rest_framework/api.html'

    def render(self, data, accepted_media_type=None, renderer_context=None):
        refresh = data.get('refresh', None)
        access = data.get('access', None)

        if refresh is not None and isinstance(refresh, bytes):
            data['refresh'] = refresh.decode('utf-8')

        if access is not None and isinstance(access, bytes):
            data['access'] = access.decode('utf-8')

        return json.dumps({
            'user': data
        })