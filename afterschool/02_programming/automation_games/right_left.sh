#!/bin/bash

# Left-Right Challenge Game

# Ask for player's name
echo "Welcome to the Left-Right Challenge Game!"
read -p "Enter your name: " player_name
echo "Hello, $player_name! Let's begin!"
echo "Each round, I'll show 'left' or 'right' - input the opposite to earn points."
echo "First to 100 points wins the flag!"
echo ""

points=0
round=1

while [ $points -lt 100 ]; do
    # Randomly choose left or right (0=left, 1=right)
    choice=$((RANDOM % 2))
    
    if [ $choice -eq 0 ]; then
        comp_choice="left"
        correct_answer="right"
    else
        comp_choice="right"
        correct_answer="left"
    fi
    
    echo ""
    echo "--- Round $round ---"
    echo "Direction: $comp_choice"
    read -p "Your answer: " player_answer
    
    # Convert to lowercase and trim whitespace
    player_answer=$(echo "$player_answer" | tr '[:upper:]' '[:lower:]' | xargs)
    
    # Check answer
    if [ "$player_answer" = "$correct_answer" ]; then
        points=$((points + 1))
        echo "Correct! Point earned! (Total: $points/100)"
    else
        echo "Wrong! The correct answer was $correct_answer"
    fi
    
    round=$((round + 1))
done

# Victory message
echo ""
echo "CONGRATULATIONS, $player_name!"
echo "You've reached 100 points!"
echo "Here's your flag: frogCTF{right_left_repeat}"
