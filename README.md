# Hungry Blob Game

Hungry Blob is a relaxing 2D indie game where players control a blob that can move left, right, and jump, collecting orbs that affect the blob's speed. The game is designed to be endless and casual, with no winning condition, making it a perfect game to unwind and play for fun. It started as a high school project in C# and was later rewritten and developed further in Python using the Pygame library.

## Features

- **Blob Movement**: Smooth control for moving left, right, and jumping.
- **Three Speed Orbs**:
  - 0.5x Speed Orb: Slows the blob down.
  - 1x Speed Orb: Keeps the blob at a normal speed.
  - 2x Speed Orb: Speeds the blob up.
- **Endless Gameplay**: The game has no final objective or winning condition, providing a relaxing, endless play experience.
- **Animated Character**: The blob character is animated with simple sprite-based movement.

## Getting Started

These instructions will help you set up and run the game on your local machine.

### Prerequisites

Ensure you have the following installed on your system:

- Python 3.x
- Pygame library

### Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/ecinteza/game-hungry-blob.git
   cd game-hungry-blob
   ```

2. **Install the Pygame library**:

   ```bash
   pip install pygame
   ```

### Running the Game

To start the game, run the following command:

```bash
python hungry_blob.py
```

- The blob can be controlled using the arrow keys for left and right movement, and the spacebar to jump.
- Collect different orbs to change the blob's speed.

### How It Works

- **Movement and Controls**: The player can control the blob's movement with the arrow keys and jump with the spacebar.
- **Orbs**: The game features three types of orbs:
  - **0.5x Speed Orb**: Slows down the blob’s movement.
  - **1x Speed Orb**: Restores the blob’s speed to normal.
  - **2x Speed Orb**: Increases the blob’s movement speed.

### Future Improvements

- **New Orbs**: Introducing new types of orbs with additional effects (e.g., size-changing orbs, time-based effects).
- **Level Design**: Add different environments or levels with varying challenges.
- **Multiplayer Mode**: Allow multiple players to compete or cooperate in the same game.

### Troubleshooting

- **Performance issues**: Ensure you have installed the latest version of Python and Pygame.
- **Graphics not loading properly**: Check that all image files are present in the correct directory.

### Contributing

Feel free to fork the repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
