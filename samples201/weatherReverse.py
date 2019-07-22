import samples101
def weatherReverse(text, appid):
    return(samples101.reverse(samples101.weather(text, appid)))
