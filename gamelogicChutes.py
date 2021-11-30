from MotorLogic import StrightLine
import numpy as np

#Deans calculations are crap

chutes_mappings_game = { '0' : (0, -1),
'1' : (0,0), '2' : (1,0), '3' : (2,0), '4' : (3,0), '5' : (4,0), '6' : (5,0), '7' : (6,0), '8' : (7,0), '9' : (8,0), '10' : (9,0),
'20': (0,1), '19': (1,1), '18': (2,1), '17': (3,1), '16': (4,1), '15': (5,1), '14': (6,1), '13': (7,1), '12': (8,1), '11' : (9,1), 
'21': (0,2), '22': (1,2), '23': (2,2), '24': (3,2), '25': (4,2), '26': (5,2), '27': (6,2), '28': (7,2), '29': (8,2), '30': (9,2), 
'40': (0,3), '39': (1,3), '38': (2,3), '37': (3,3), '36': (4,3), '35': (5,3), '34': (6,3), '33': (7,3), '32': (8,3), '31': (9,3), 
'41': (0,4), '42': (1,4), '43': (2,4), '44': (3,4), '45': (4,4), '46': (5,4), '47': (6,4), '48': (7,4), '49': (8,4), '50': (9,4), 
'60': (0,5), '59': (1,5), '58': (2,5), '57': (3,5), '56': (4,5), '55': (5,5), '54': (6,5), '53': (7,5), '52': (8,5), '51': (9,5), 
'61': (0,6), '62': (1,6), '63': (2,6), '64': (3,6), '65': (4,6), '66': (5,6), '67': (6,6), '68': (7,6), '69': (8,6), '70': (9,6), 
'80': (0,7), '79': (1,7), '78': (2,7), '77': (3,7), '76': (4,7), '75': (5,7), '74': (6,7), '73': (7,7), '72': (8,7), '71': (9,7), 
'81': (0,8), '82': (1,8), '83': (2,8), '84': (3,8), '85': (4,8), '86': (5,8), '87': (6,8), '88': (7,8), '89': (8,8), '90': (9,8), 
'100': (0,9), '99': (1,9), '98': (2,9), '97': (3,9), '96': (4,9), '95': (5,9), '94': (6,9), '93': (7,9), '92': (8,9), '91': (9,9)
}

previousmove = []
magnet_location = '1'
boy_location = '1'        # we will have to do some collision detection
girl_location = '0'

def get_key(val):
    for key, value in chutes_mappings_game.items():
        if val == value:
            return key

def SameRowCollision(gender, num):
    if gender == 'b':
        for i in range(num):
            if int(boy_location) + i == int(girl_location):
                return 'collides'
    elif gender == 'g':
        for i in range(num):
            if int(girl_location) + i == int(boy_location):
                return 'collides'
    else:
        return 'no'

def changeBoard_chutes(move):
    if move[0] == 'move':
        if move[1] == 'boy':
            piece = 'b'
        elif move[1] == 'girl':
            piece = 'g'
        
        if move[3] == 'to':
            if piece == 'b':
                if girl_location == move[4]:
                    coords = chutes_mappings_game[girl_location]
                    either = get_key( (coords[0] - 1, coords[1]))
                elif boy_location == move[4]:
                    coords = chutes_mappings_game[boy_location]
                    either = get_key( (coords[0] - 1, coords[1]))
                else:
                    either = move[4]
            StrightLine(move[2],either,magnet_location, 'chutes')
            previousmove.clear()
            previousmove.append(move[2])    # start
            previousmove.append(move[4])    # end
            if piece == 'b':
                boy_location = either
            elif piece == 'g':
                girl_location = either

        elif move[3] == 'spots':                     # will probababily change this based on how google reads numbers
            num = int(move[2])                       # assuming input string is '5'
            if piece == 'b':
                start = chutes_mappings_game[boy_location]
                if (start[0] + num) >= 9:
                    newx =  9 - ((start[0] + num)-10)
                    end = ( newx, start[1] + 1)
                    StrightLine (get_key(start), get_key(end), magnet_location, 'chutes')
                    previousmove.clear()
                    previousmove.append(get_key(start))    # start
                    previousmove.append(get_key(end))    # end
                else:
                    if SameRowCollision(piece, num) == 'no':
                        newx = start[0] + num
                        end = (newx, start[1])
                        StrightLine (get_key(start), get_key(end), magnet_location, 'chutes')
                        previousmove.clear()
                        previousmove.append(get_key(start))    # start
                        previousmove.append(get_key(end))    # end
                    elif SameRowCollision(piece, num) == 'collides':
                        end1 = (start[0], start[1]+1)
                        StrightLine (get_key(start), get_key(end1), magnet_location, 'chutes')
                        end2 = (start[0] + num, end1[1])
                        StrightLine (get_key(end1), get_key(end2), magnet_location, 'chutes')
                        end3 = (end2[0], start[1])
                        StrightLine (get_key(end2), get_key(end3), magnet_location, 'chutes')

            elif piece == 'g':
                start = chutes_mappings_game[girl_location]
                if (start[0] + num) >= 9:
                    newx =  9 - ((start[0] + num)-10)
                    end = ( newx, start[1] + 1)
                else:
                    newx = start[0] + num
                    end = (newx, start[1])
                StrightLine (get_key(start), get_key(end), magnet_location, 'chutes')
                previousmove.clear()
                previousmove.append(get_key(start))    # start
                previousmove.append(get_key(end))    # end                              

    elif move[0] == "spin":
        if move[1] == "the":
            if move[2] == "wheel":
                spin = np.random.randint(1,6)
                #speaker say out load function
            else:
                return "invalid command"
        else:
            return "invalid command"
    
    elif move[0] == 'start':
        boy_location = '1'        # we will have to do some collision detection
        girl_location = '0'

    elif move[0] == "undo":
        if move[1] == "move":
            if len(previousmove) ==2:
                StrightLine(previousmove[1], previousmove[0], magnet_location, 'chutes')
        else:
            return "invalid command"

    else:
        return "invalid command"

