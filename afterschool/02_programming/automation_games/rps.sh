#!/bin/bash

# Rock-Paper-Scissors Challenge Game

# Ask for player's name
echo "Welcome to the RPS Challenge Game!"
read -p "Enter your name: " player_name
echo "Hello, $player_name! Let's begin!"
echo "I'll show an RPS choice, and you must counter it to earn points."
echo "First to 100 points wins the flag!"
echo ""

points=0
round=1

while [ $points -lt 100 ]; do
    # Generate computer's choice (1=rock, 2=paper, 3=scissors)
    choice=$((RANDOM % 3 + 1))
    
    case $choice in
        1) comp_choice="rock" ;;
        2) comp_choice="paper" ;;
        3) comp_choice="scissors" ;;
    esac
    
    echo ""
    echo "--- Round $round ---"
    echo "Computer shows: $comp_choice"
    read -p "Your counter move (rock/paper/scissors): " player_move
    
    # Convert to lowercase
    player_move=${player_move,,}
    
    # Determine if player countered correctly
    case "$comp_choice-$player_move" in
        "rock-paper"|"paper-scissors"|"scissors-rock")
            points=$((points + 1))
            echo "Correct! Point earned! (Total: $points/100)"
            ;;
        "rock-rock"|"paper-paper"|"scissors-scissors")
            echo "Draw! No points."
            ;;
        *)
            echo "Wrong counter! No points."
            ;;
    esac
    round=$((round + 1))
done

# Victory message
echo ""
echo "CONGRATULATIONS, $player_name!"
echo "You've reached 100 points!"
echo "Here's your flag: frogCTF{RPS_FTW}"
