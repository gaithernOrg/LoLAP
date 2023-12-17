import requests
import json

versions_url = "https://ddragon.leagueoflegends.com/api/versions.json"
maps_url = "https://static.developer.riotgames.com/docs/lol/maps.json"
most_recent_version = requests.get(versions_url).json()[0]
items_url = "https://ddragon.leagueoflegends.com/cdn/" + str(most_recent_version) + "/data/en_US/item.json"
sr_items = {}
aram_items = {}
arena_items = {}
for map in requests.get(maps_url).json():
    if map["mapName"] == "Summoner's Rift" and map["notes"] == "Current Version":
        sr_map_id = map["mapId"]
    if map["mapName"] == "Howling Abyss":
        aram_map_id = map["mapId"]
    if map["mapName"] == "Rings of Wrath":
        arena_map_id = map["mapId"]

item_data = requests.get(items_url).json()["data"]
for item_id in item_data.keys():
    if "into" not in item_data[item_id].keys() and item_data[item_id]["gold"]["purchasable"] and item_data[item_id]["gold"]["total"] > 1000:
        if item_data[item_id]["maps"][str(sr_map_id)]:
            sr_items[item_id] = item_data[item_id]["name"]
        if item_data[item_id]["maps"][str(aram_map_id)]:
            aram_items[item_id] = item_data[item_id]["name"]
        if item_data[item_id]["maps"][str(arena_map_id)]:
            arena_items[item_id] = item_data[item_id]["name"]