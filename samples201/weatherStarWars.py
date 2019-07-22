import samples101
def weatherStarWars(text, appid):
    return(samples101.starwars(samples101.weather(text, appid)))
