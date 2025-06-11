from streamlit_app.api.service import Auth

client = Auth()
token = client.get_token(username='jonh', password='123')
print(token['refresh'])
