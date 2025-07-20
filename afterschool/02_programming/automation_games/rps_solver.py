import subprocess
import re
import time

def solve_rps_game():
    # Start the game process
    game = subprocess.Popen(
        ['./rps.sh'],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        bufsize=1
    )
    
    # Counter moves lookup table
    counter_moves = {
        'rock': 'paper',
        'paper': 'scissors',
        'scissors': 'rock'
    }
    
    # Send player name
    game.stdin.write("PythonSolver\n")
    game.stdin.flush()
    
    # Wait for game to start
    time.sleep(0.5)
    
    # Main game loop
    while True:
        # Read game output line by line
        line = game.stdout.readline()
        if not line:
            break
        
        print(line.strip())  # Print game output
        
        # Check for win condition
        if 'frogCTF{' in line:
            print("\nFlag captured successfully!")
            break
        
        # Look for computer's move
        if 'Computer shows:' in line:
            # Extract computer's choice
            comp_choice = line.split(':')[-1].strip().lower()
            
            # Determine correct counter move
            player_move = counter_moves.get(comp_choice, 'rock')  # Default to rock if unexpected input
            
            # Send our move
            game.stdin.write(f"{player_move}\n")
            game.stdin.flush()
            print(f"Playing: {player_move}")
            
            # Small delay to prevent overwhelming the game
            time.sleep(0.1)

if __name__ == "__main__":
    solve_rps_game()
