import pymongo
databases = pymongo.MongoClient("mongodb://localhost:27017/")
EvolutionaryGames_database = databases["EvolutionaryGames"]
game_collection = EvolutionaryGames_database["Game"]


