from high_or_low import data
import random

lifes = 5

class Game:
    def __init__(self, lifes, data):
        self.data = data
        self.lifes = lifes
        self.score_count = 0
        self.info_score_and_lifes = [self.lifes, self.score_count]

        while self.info_score_and_lifes[0] != 0:

            numbers_list = self.get_random_number(self.data)
            self.info_score_and_lifes = self.play_game(self.data, numbers_list, self.info_score_and_lifes)

        else:
            print(f'Your score is {self.info_score_and_lifes[1]}')
            print("End game ")

    def get_random_number(self, data):
        indices = random.sample(range(len(data)), 2)
        return indices

    def get_user_input(self):
        user_input = input('1 or 2: ')
        user_choices = ("1", "2")

        while user_input not in user_choices:
            user_input = input('1 or 2: ')
        return user_input
    def play_game(self, data, numbers_list, info_score_and_lifes):
        first_player = data[numbers_list[0]]
        second_player = data[numbers_list[1]]

        print(f'Who has more followers {first_player["name"]} or {second_player["name"]}')

        user_input = self.get_user_input()

        if user_input == '1' and first_player["follower_count"] > second_player["follower_count"]:
            print('You are correct')
            info_score_and_lifes[1] += 1
            return info_score_and_lifes
        elif user_input == '2' and second_player["follower_count"] > first_player["follower_count"]:
            print('You are correct')
            info_score_and_lifes[1] += 1
            return info_score_and_lifes
        else:
            print('Wrong')
            info_score_and_lifes[0] -= 1
            return info_score_and_lifes

game = Game(lifes, data)
