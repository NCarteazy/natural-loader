from enum import Enum

from natural_loader.parker.models.activity_data import ActivityData
from natural_loader.parker.models.activity_park_data import ActivityParkData
from natural_loader.parker.models.alert_data import AlertData
from natural_loader.parker.models.base_document import BaseDocument
from natural_loader.parker.models.campground_data import CampgroundData
from natural_loader.parker.models.event_data import EventData
from natural_loader.parker.models.fees_passes_data import FeesPassesData
from natural_loader.parker.models.mapdata_parkboundary import MapdataParkboundary
from natural_loader.parker.models.park_data import ParkData
from natural_loader.parker.models.person_data import PersonData
from natural_loader.parker.models.place_data import PlaceData

BASE_URL = "https://developer.nps.gov/api/v1/"
Parameters = dict[str, str | list[str | int] | int]


class Resource(Enum):
    ACTIVITIES = "activities"
    ACTIVITES_PARKS = "activities/parks"
    ALERTS = "alerts"
    AMENITIES = "amenities"
    PARKSPLACES = "amenities/parksplaces"
    PARKSVISITORCENTERS = "amenities/parksvisitorcenters"
    ARTICLES = "articles"
    CAMPGROUNDS = "campgrounds"
    EVENTS = "events"
    FEESPASSES = "feespasses"
    LESSONPLANS = "lessonplans"
    PARKBOUNDARIES = "mapdata/parkboundaries/{sitecode}"
    AUDIO = "multimedia/audio"
    GALLERIES = "multimedia/galleries"
    ASSETS = "multimedia/galleries/assets"
    VIDEOS = "multimedia/videos"
    NEWSRELEASES = "newsreleases"
    PARKINGLOTS = "parkinglots"
    PARKS = "parks"
    PASSPORTSTAMPLOCATIONS = "passportstamplocations"
    PEOPLE = "people"
    PLACES = "places"
    ROADEVENTS = "roadevents"
    THINGSTODO = "thingstodo"
    TOPICS = "topics"
    PARKSTOPICS = "topics/parks"
    TOURS = "tours"
    VISITORCENTERS = "visitorcenters"
    WEBCAMS = "webcams"


resource_to_model: dict[Resource, BaseDocument] = {
    Resource.ACTIVITIES: ActivityData,
    Resource.ACTIVITES_PARKS: ActivityParkData,
    Resource.ALERTS: AlertData,
    Resource.PARKSPLACES: PlaceData,
    Resource.CAMPGROUNDS: CampgroundData,
    Resource.EVENTS: EventData,
    Resource.FEESPASSES: FeesPassesData,
    Resource.PARKS: ParkData,
    Resource.PARKBOUNDARIES: MapdataParkboundary,
    Resource.PEOPLE: PersonData,
}
