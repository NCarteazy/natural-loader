import national_parks as np
from national_parks.models.park import Park
from natural_loader.parker.constants import API_KEY

config = np.Configuration()
config.api_key["api_key"] = API_KEY
api_instance = np.ParksApi(np.ApiClient(config))
parks = api_instance.get_park(limit=1)
# print(Park(parks[0]))
print(parks)
