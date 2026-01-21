# RPG Tracker
import json  # For saving and loading player data
import os  # For checking file existence

# ---------------Configuration-------------------
file_name = "rpg_save.json"
history_file = "rpg_history.csv"


player = {"Name": "Mateusz ",
          "xp": 0,
          "level": 1,
          "rank": "Novice"}

quests = {"1": {"name": "Reading ", "xp": 50},
          "2": {"name": "Cleaning the House ", "xp": 125},
          "3": {"name": "Coding ", "xp": 150},
          "4": {"name": "Exercising ", "xp": 100},
          "5": {"name": "Cooking ", "xp": 75},
          "6": {"name": "Gaming ", "xp": 25},
          "7": {"name": "Learning  ", "xp": 80}
          }


def save_progress():
    with open(file_name, "w") as file:
        json.dump(player, file)  # Save player data to JSON file
    print("Progress saved!")


def load_progress():
    global player
    if os.path.exists(file_name):
        with open(file_name, "r") as file:
            player = json.load(file)  # Load player data from JSON file
        print("Progress loaded!")


def show_status():
    print(f"Player: {player['Name']}")
    print(f"Level: {player['level']}")
    print(f"XP: {player['xp']}")
    print(f"Rank: {player['rank']}")


def level_up():
    required_xp = player['level'] * 100

    while player['xp'] >= required_xp:
        player['level'] += 1
        player['xp'] -= required_xp
        print(f"Congratulations! You've reached level {player['level']}!")
    else:
        print(f"You need {required_xp - player['xp']} more XP to level up.")


def complete_quest():
    print("Available Quests:")
    for k, v in quests.items():  # Display available quests key and value
        print(f"{k}. {v['name']} - {v['xp']} XP")

    choice = input("Select a quest number to complete (or 'q' to cancel): ")
    if choice in quests:
        player['xp'] += quests[choice]['xp']  # Add quest XP to player XP
        print(
            f"You completed the quest '{quests[choice]['name']}' and earned {quests[choice]['xp']} XP!")
    elif choice.lower() == 'q':
        print("Quest cancelled.")
    else:
        print("Invalid quest number.")

    level_up()
    save_progress()


def start():
    load_progress()  # Load progress at the start
    while True:
        print("\n--- RPG Tracker Menu ---")
        print(
            f"\n Player: {player['Name']} | Level: {player['level']} | XP: {player['xp']} | Rank: {player['rank']} |")
        print("1. Complete a Quest")
        print("2. Exit")

        choice = input("Select an option: ")

        if choice == '1':
            complete_quest()
        elif choice == '2':
            print("Exiting the RPG Tracker. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    start()
