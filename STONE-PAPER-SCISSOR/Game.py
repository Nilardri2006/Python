import random

'''
1 for Snake
-1 for Water
0 for Gun
'''
print("🎮 >>> SNAKE, WATER, GUN Game <<< 🎮")
name = input("Enter Your Name: ")

youDict = {"s": 1, "w": -1, "g": 0}
revDict = {1: "Snake 🐍", -1: "Water 💧", 0: "Gun 🔫"}

# Get user choice
youStr = input("Enter your Choice (s for Snake 🐍, w for Water 💧, g for Gun 🔫): ").lower()

# Validate input
if youStr not in youDict:
    print("❌ Invalid Input! Please enter only 's', 'w', or 'g'.")
else:
    you = youDict[youStr]
    computer = random.choice([1, -1, 0])

    print(f"\n{name} chose: {revDict[you]}")
    print(f"Computer chose: {revDict[computer]}")

    # Game logic
    if you == computer:
        print("🤝 It's a draw!")
    elif (you == 1 and computer == -1) or (you == -1 and computer == 0) or (you == 0 and computer == 1):
        print(f"🏆 {name} wins!")
    else:
        print("💻 Computer wins!")
