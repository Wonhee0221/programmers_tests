def solution(players, callings):
    players_dict = {}
    for i in range(len(players)):
        players_dict[players[i]] = i
    
    for i in callings:
        player_index = players_dict[i]
        if player_index > 0: 
            prev_index = players[player_index-1]
            players[player_index-1], players[player_index] = players[player_index], players[player_index-1]
            players_dict[i] -= 1
            players_dict[prev_index] += 1
        
            
    return players