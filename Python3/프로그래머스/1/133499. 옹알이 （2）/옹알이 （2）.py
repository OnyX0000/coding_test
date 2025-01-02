def solution(babbling):
    valid_sounds = ["aya", "ye", "woo", "ma"]
    count = 0

    for word in babbling :
        for sound in valid_sounds :
            if sound * 2 in word :  
                break
            word = word.replace(sound, " ")  
        if word.strip() == "" : 
            count += 1

    return count