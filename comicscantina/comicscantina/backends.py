from oauthlib.oauth2 import BackendApplicationClient
from oauthlib.oauth2 import LegacyApplicationClient
from requests_oauthlib import OAuth2Session
from oauthlib.oauth2 import TokenExpiredError
from django.contrib.auth.backends import ModelBackend
from django.conf import settings


class ComicsCantinaRemoteIAMAuthBackend(ModelBackend):
    token = None

    def get_token(self):
        if self.token is None:
            # http://requests-oauthlib.readthedocs.io/en/latest/oauth2_workflow.html#legacy-application-flow
            client_id = settings.COMICSCANTINA_IAM_CLIENT_ID
            client_secret = settings.COMICSCANTINA_IAM_CLIENT_SECRET
            username = settings.COMICSCANTINA_IAM_USERNAME
            password = settings.COMICSCANTINA_IAM_PASSWORD

            client = BackendApplicationClient(client_id=client_id)
            oauth = OAuth2Session(client=LegacyApplicationClient(client_id=client_id))

            self.token = oauth.fetch_token(
                token_url=settings.COMICSCANTINA_IAM_TOKEN_URL,
                client_id=client_id,
                client_secret=client_secret,
                username=username,
                password=password
            )

        return self.token

    def authenticate(self, username=None, password=None, **kwargs):
        token = self.get_token()

        protected_url = settings.COMICSCANTINA_IAM_BASE_URL + "/api/user/1/" #TODO: CREATE LOGIN API ENDPOINT.

        try:
            # Begin a OAuth2 session.
            client = OAuth2Session(
                settings.COMICSCANTINA_IAM_CLIENT_ID,
                token=token
            )

            # Make our fetch request to the protected resource.
            r = client.get(protected_url)

        except TokenExpiredError as e:
            token = client.refresh_token(settings.COMICSCANTINA_IAM_REFRESH_TOKEN_URL, None)

            self.token = token # token_saver(token)

            # Begin a OAuth2 session.
            client = OAuth2Session(
                settings.COMICSCANTINA_IAM_CLIENT_ID,
                token=token
            )

            # Make another fetch request to the protected resource with
            # our newly refreshed token.
            r = client.get(protected_url)

        print(r.content)

        #TODO: IMPLEMENT DOWNLOADING USER IAM PROFILE TO OUR SERVER.

        return None

        # try:
        #     user = User.objects.get(email=username)
        #     if user.check_password(password):
        #         return user
        # except ObjectDoesNotExist:
        #     # Run the default password hasher once to reduce the timing
        #     # difference between an existing and a non-existing user (#20760).
        #     User().set_password(password)

# http://requests-oauthlib.readthedocs.io/en/latest/oauth2_workflow.html#
