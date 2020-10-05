from recombee_api_client.api_client import RecombeeClient
from recombee_api_client.api_requests import *

client=RecombeeClient('sa-games-post','YQdgn1kUr1c8jFuYaL3WXth8FQO7HI23ugQ92jUtKGjm8JiKntxvSFEloshzU0CJ')
# recommendation=client.send(RecommendUsersToItem('5ce15a139a88125d88acd479',6))
# recommendation=client.send(RecommendItemsToUser('kathrynhernandez@yahoo.com',5))
# recommendation=client.send(RecommendItemsToItem('5ccff42f9a88124d5cb72268','fullerrebecca@gmail.com',10, filter=" \"GATE\" in 'tags'"))
recommendation=client.send(RecommendUsersToUser('sanujsriv@gmail.com',6,return_properties=True))

print(recommendation)
print()
print()
print()
print(len(recommendation['recomms']))
