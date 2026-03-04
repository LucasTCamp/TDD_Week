def add_points(game, amount):
    if amount < 0:
        raise ValueError
    elif game["active"] == False:
        return game
    else:
        game["score"] += (amount * game["multiplier"])
        return game

def apply_multiplier(game, multiplier):
    if multiplier < 1:
        raise ValueError
    elif game["active"] == False:
        return game
    else:
        game["multiplier"] = multiplier
        return game

def reset_score(game):
    game["score"] = 0
    game["multiplier"] = 1
    return game

def is_high_score(game, threshold):
    if game["score"] < 0:
        raise ValueError
    elif game["score"] == threshold:
        return False
    else:
        return True
