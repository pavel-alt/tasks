class SoccerPlayer:
    def __init__(self, name: str, surname: str) -> None:
        self.name = name
        self.surname = surname
        self.all_goals = 0
        self.all_assists = 0

    def score(self, goals: int = 1) -> None:
        self.all_goals += goals

    def make_assist(self, assists: int = 1) -> None:
        self.all_assists += assists

    def statistics(self) -> None:
        print(f'{self.name} {self.surname} - голы: {self.all_goals}, передачи: {self.all_assists}')


leo = SoccerPlayer('Leonel', 'Messi')
leo.score(50)
leo.score(50)
leo.score(50)
leo.make_assist(20)
leo.statistics()
