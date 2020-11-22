# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 21:37:15 2020

@author: Eva
"""
import http.client
from kkbox_developer_sdk.auth_flow import KKBOXOAuth
from kkbox_developer_sdk.api import KKBOXAPI

class ClientInfo():
    client_id = "bca3a776e63a2a9813c7c4646980bfba"
    client_secret = "da4e7e8eb8ed3dbb0686ddc5f49784c4"

a = ClientInfo(); 

auth = KKBOXOAuth(a.client_id, a.client_secret)
token = auth.fetch_access_token_by_client_credentials()


#print(token)
kkboxapi = KKBOXAPI(token)
artist_id = '8q3_xzjl89Yakn_7GB'
artist = kkboxapi.artist_fetcher.fetch_artist(artist_id)

conn = http.client.HTTPSConnection("api.kkbox.com")

headers = {
    'accept': "application/json",
    'authorization':  "Bearer o3M1esXZRj9d7GvWUoj2Hg=="
    }

conn.request("GET", "/v1.1/search?q=nopartyforcaodong&type=track&territory=TW&offset=0&limit=50", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))