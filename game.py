import requests
import time
URL = "http://upe.42069.fun/U2wTI"
email = {"email":"stvnguan@ucla.edu"}
requests.post(url = URL + '/reset', data = email)

def dict(file):
    dictionary = {}
    with open(file, 'r') as file:
        for lines in file:
            l = lines.rstrip()
            if len(l) not in d:
                dictionary[len(l)] = [1]
            else:
                dictionary[len(l)].append(l)
    return d

    
def wordSearch(let, size, dict):
        words = []
        allWords = dict[size]
        for l in let:
            if len(words) == 0:
                for w in allWords:
                    if w[int(l[1]) - 1].count(l[0]):
                        words.append(w)
                    elif w in words:
                        words.remove(w)
            else:
                words = [w for w in words
                            if w[int(l[1]) - 1].count(pair[0])]
        return words
        
        
def main():
    dictionary = dict('finalwords.txt')
    
        
    while (True):
        r = requests.get(url = URL)

        data = r.json()

        state = data['state']
        status = data['status']
        remaining_guesses = data['remaining_guesses']
        time.sleep(0.5)
        print(state)

        letters = 'esi'

        while (status == 'ALIVE'):
            for x in range(0, 3):
                guess = {"guess":letters[x]}
                data = requests.post(url = URL, data = guess).json()
                time.sleep(0.5)
            
            state = data['state']
            words = state.split(' ')
            max = 0
            word = 'w'
            for w in words:
                if len(w) > max:
                    max = w
            
        
        print("Win rate: ")
        print(data['win_rate'])
        print("Games played: ")
        print(data['games'])
        print(data['state']);
        print('\n')