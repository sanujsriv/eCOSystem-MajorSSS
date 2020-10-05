from recombee_api_client.api_client import RecombeeClient
from recombee_api_client.api_requests import *

import json

client=RecombeeClient('ecosystem-post','6FUQahHRFNPmTxHfY280M6WmnkI6OdKYsghdsziBioZ3FxiNboAOtN62tpM7Klqs')
requests = []


with open('user_post_interactions.json') as upi:
    interactions = json.loads(upi.read())
    for interaction in interactions:
        r = AddDetailView(
            user_id=interaction["user_id"],
            item_id=interaction["item_id"],
            timestamp=interaction["timestamp"],
            cascade_create=True
        )
        requests.append(r)

client.send(Batch(requests))

requests=[]

client.send(AddItemProperty('title','string'))
client.send(AddItemProperty('author','string'))
client.send(AddItemProperty('tags','set'))
client.send(AddItemProperty('timestamp','timestamp'))

with open('post_properties.json') as pp:
    interactions = json.loads(pp.read())
    for item_id,values in interactions.items():
        q = SetItemValues(item_id,
                          values,
                          cascade_create=True)
        requests.append(q)

client.send(Batch(requests))
