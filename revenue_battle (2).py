import random
import time

# ASCII Art for the game title
def print_title():
    print(r"""
   ____                                _     _                 _ 
  / ___|___  _ __ ___  _ __   ___  ___| |__ (_)_ __ ___   __ _| |
 | |   / _ \| '_ ` _ \| '_ \ / _ \/ __| '_ \| | '_ ` _ \ / _` | |
 | |__| (_) | | | | | | |_) | (_) \__ \ | | | | | | | | | (_| | |
  \____\___/|_| |_| |_| .__/ \___/|___/_| |_|_|_| |_| |_|\__,_|_|
                      |_|                                        
    """)
    print("Welcome to Courtyard Revenue Manager!
")

# STR Report simulation
def generate_str_report(level):
    base_occ = random.randint(60, 80) + level * 2
    base_adr = random.randint(100, 150) + level * 5
    revpar = round((base_occ / 100) * base_adr, 2)
    market_occ = base_occ + random.randint(-5, 5)
    market_adr = base_adr + random.randint(-10, 10)
    return {
        "Occupancy": base_occ,
        "ADR": base_adr,
        "RevPAR": revpar,
        "Market Occ": market_occ,
        "Market ADR": market_adr
    }

# Evil competitor simulation
def evil_competitor_action(level):
    actions = [
        "undercuts your rate by 10%",
        "launches a flash sale",
        "offers free breakfast",
        "partners with a travel site for discounts",
        "steals your group booking"
    ]
    action = random.choice(actions)
    impact = random.randint(3, 10) + level
    return action, impact

# Display STR report
def display_str_report(report):
    print("
📊 Weekly STR Report:")
    for key, value in report.items():
        print(f"  {key}: {value}")

# Decision making
def get_player_decision():
    print("
What would you like to do this week?")
    print("1. Increase rates by 10%")
    print("2. Decrease rates by 10%")
    print("3. Launch a weekend promotion")
    print("4. Do nothing")
    choice = input("Enter your choice (1-4): ")
    return choice

# Apply decision and simulate outcome
def apply_decision(report, decision, competitor_impact):
    base_occ = report["Occupancy"]
    base_adr = report["ADR"]

    if decision == "1":
        new_adr = int(base_adr * 1.10)
        new_occ = max(40, base_occ - random.randint(5, 10) - competitor_impact)
    elif decision == "2":
        new_adr = int(base_adr * 0.90)
        new_occ = min(100, base_occ + random.randint(5, 10) - competitor_impact)
    elif decision == "3":
        new_adr = int(base_adr * 0.95)
        new_occ = min(100, base_occ + random.randint(8, 15) - competitor_impact)
    else:
        new_adr = base_adr
        new_occ = max(30, base_occ - competitor_impact)

    new_revpar = round((new_occ / 100) * new_adr, 2)
    return {
        "Occupancy": new_occ,
        "ADR": new_adr,
        "RevPAR": new_revpar
    }

# Main game loop
def play_game():
    print_title()
    total_revpar = 0
    levels = 5

    for level in range(1, levels + 1):
        print(f"
🏨 Level {level} - Week {level}")
        report = generate_str_report(level)
        display_str_report(report)

        competitor_action, impact = evil_competitor_action(level)
        print(f"
😈 Evil Competitor {competitor_action}! (Impact: -{impact}% occupancy)")

        owner_goal = report["RevPAR"] + random.randint(5, 15)
        print(f"
📢 Owner expects a RevPAR of at least {owner_goal:.2f} this week!")

        decision = get_player_decision()
        outcome = apply_decision(report, decision, impact)

        print("
📈 Outcome after your decision:")
        for key, value in outcome.items():
            print(f"  {key}: {value}")

        if outcome["RevPAR"] >= owner_goal:
            print("✅ You met the owner's expectations!")
        else:
            print("⚠️ The owner is disappointed...")

        total_revpar += outcome["RevPAR"]
        time.sleep(1)

    avg_revpar = round(total_revpar / levels, 2)
    print("
🏁 Final Boss Battle!")
    print("To win, your average RevPAR must beat the market and the evil competitor!")

    if avg_revpar > 140:
        print(f"
🎉 You win! Your average RevPAR was {avg_revpar}. You're a Revenue Legend!")
    elif avg_revpar > 120:
        print(f"
👍 Solid performance! Your average RevPAR was {avg_revpar}.")
    else:
        print(f"
📉 You lost the battle. Your average RevPAR was {avg_revpar}. Try again!")

# Run the game
if __name__ == "__main__":
    play_game()
