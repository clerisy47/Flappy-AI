# Flappy AI

Flappy AI is a reinforcement learning application for the game Flappy Bird, implemented using the NEAT (NeuroEvolution of Augmenting Topologies) algorithm. The goal of the application is to train a neural network to play Flappy Bird by evolving a population of bird agents over multiple generations.

## Getting Started

Ensure you have Python installed on your system.

1. Clone the repository:

   ```bash
   git clone https://github.com/your_username/flappy-ai.git
   cd flappy-ai
   ```

2. Install dependencies:

   ```bash
   pip install pygame neat-python
   ```

3. Run the application:

   ```bash
   python flappy_ai.py
   ```

## Gameplay

- The game window displays the Flappy Bird environment, including pipes and a moving base.
- Birds are controlled by neural networks that evolve over generations using the NEAT algorithm.
- The goal is to navigate the birds through the pipes by jumping at the right time.
- The score indicates the number of pipes successfully passed by the birds.
- The game ends when all birds either collide with pipes or reach a score of 100.

## Configuration

The neural network and NEAT algorithm parameters are configured in the `config.txt` file. You can customize these parameters to experiment with different settings and improve the learning performance.

## Controls

- The birds are controlled by the neural network and automatically jump based on the learned behavior.

## Development

If you want to contribute or modify the game, you can explore the following files:

- `bird.py`: Contains the Bird class, representing the Flappy Bird agents.
- `base.py`: Implements the moving base of the game.
- `pipe.py`: Defines the Pipe class, representing the pipes that birds must navigate through.
- `flappy_ai.py`: The main script that orchestrates the game, NEAT algorithm, and visualization.

## Credits

- This implementation is based on the NEAT algorithm, pygame library, and the classic Flappy Bird game.
- NEAT (NeuroEvolution of Augmenting Topologies) is a method for evolving artificial neural networks.
- Flappy Bird is a popular mobile game developed by Dong Nguyen.

Enjoy training your AI to master Flappy Bird!
