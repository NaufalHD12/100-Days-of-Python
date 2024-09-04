import random
from art import logo, vs
from game_data import data
import os
import subprocess

compare_list = []
against_list = []
current_score = 0


def deal_name():
    compare_list.append(random.choice(data))
    against_list.append(random.choice(data))
    if compare_list == against_list:
        against_list.clear()
        against_list.append(random.choice(data))


def compare_followers(char):
    global current_score
    if char == 'a':
        if int(compare_list[0]['follower_count']) > int(
                against_list[0]['follower_count']):
            current_score += 1
            result = True
            print(f"You're right! Current score: {current_score}")
            return result
        else:
            result = False
            print(f"Sorry, that's wrong. Final score: {current_score}")
            return result

    if char == 'b':
        if int(against_list[0]['follower_count']) > int(
                compare_list[0]['follower_count']):
            current_score += 1
            result = True
            print(f"You're right! Current score: {current_score}")
            return result
        else:
            result = False
            print(f"Sorry, that's wrong. Final score: {current_score}")
            return result


deal_name()
print(logo)


def game_start():
    print(
        f"Compare A: {compare_list[0]['name']}, a {compare_list[0]['description']}, from {compare_list[0]['country']}"
    )
    print(vs)
    print(
        f"Against B: {against_list[0]['name']}, a {against_list[0]['description']}, from {against_list[0]['country']}"
    )
    compare_input = input("Who has more Followers? Type 'A' or 'B': ").lower()
    while True:
        subprocess.run('clear' if os.name == 'posix' else 'cls',
                       shell=True, check=True)
        print(logo)
        if compare_followers(char=compare_input):
            compare_list.clear()
            compare_list.extend(against_list)
            against_list.clear()
            against_list.append(random.choice(data))
        else:
            break
        game_start()


game_start()
