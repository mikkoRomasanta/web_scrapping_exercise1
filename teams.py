class TeamInfo(object):
    def __init__(self, position, name, points):
        self.position = self.add_spaces(1,str(position).strip())
        self.name = self.add_spaces(2,str(name).strip())
        self.points = self.add_spaces(3,str(points).strip())

    def add_to_table(self):
        return f'{self.position}| {self.name}| {self.points}'

    def add_spaces(self, num, string): #fix formatting for the table
        space = ' '

        if num == 1:  #1 for position 
            max_len = 3 #max length for string
            add_space = space*(max_len - len(string))
            new_string = f'{string}{add_space}'

        elif num == 2:  #2 for name
            max_len = 25
            add_space = space*(max_len - len(string))
            new_string = f'{string}{add_space}'
        
        elif num == 3:  #3 for points
            max_len = 4 
            add_space = space*(max_len - len(string))
            new_string = f'{string}{add_space}'

        return new_string

class TeamHeader(object): #displays the table header
    def __init__(self):
        position = TeamInfo.add_spaces(self, 1, '#')
        name = TeamInfo.add_spaces(self, 2, 'Teams')
        points = TeamInfo.add_spaces(self, 3, 'Pts')

        print(f'{position}| {name}| {points}')