# Files:
- valueIterationAgent.py: This file implements value iteration agent.
- qlearningAgents.py: This file implements Q-learning as a reinforcement learning agent by generating a Q-value.
- analysis.py: This file finds the different values to manimpulate the behavior of the Pacman.

# Running Tests:
IMPORTANT: In order to run these tests, download the pacai repo, open the student folder, and replace the valueIteration.py, qlearningAgents.py, and the analysis.py files with mine.

**Iterations: Run the following:**

```python3 -m pacai.bin.gridworld --agent value --iterations 100 --episodes 10```

```python3 -m pacai.bin.gridworld --agent value --iterations 5```

<img width="618" alt="image" src="https://github.com/christy-jose01/Pacman-AI/assets/77473804/7a8aa471-6091-4aad-b566-4192f58f0e1a">

**QLearning: Run the following:**

```python3 -m pacai.bin.gridworld --agent q --episodes 5 --manual```

```python3 -m pacai.bin.gridworld --agent q --episodes 100```

```python3 -m pacai.bin.gridworld --agent q --episodes 50 --noise 0 --grid BridgeGrid --epsilon 1```

```python3 -m pacai.bin.pacman -p PacmanQAgent --num-training 2000 --num-games 2010 --layout smallGrid```

```python3 -m pacai.bin.pacman -p ApproximateQAgent --num-training 2000 --num-games 2010 --layout smallGrid```

```python3 -m pacai.bin.pacman -p ApproximateQAgent --agent-args extractor=pacai.core.featureExtractors.SimpleExtractor --num-training 50 --num-games 60 --layout mediumGrid```

**Analysis: Run the following:**

```python3 -m pacai.bin.gridworld --agent value --iterations 100 --grid BridgeGrid --discount 0.9 --noise 0.2 --living-reward 0.0```

This is the default command that you need to enter. However, for each of the following scenarios you will need to change the noise value, discount value, and living reward value. These values are given in analysis.py

To cross the bridge: refer to the values in 2.
To prefer the close exit (+1), risking the cliff (-10): refer to the values in 3a.
To prefer the close exit (+1), but avoiding the cliff (-10): refer to the values in 3b.
To prefer the distant exit (+10), risking the cliff (-10): refer to the values in 3c.
To prefer the distant exit (+10), avoiding the cliff (-10): refer to the values in 3d.
To avoid both exits (also avoiding the cliff): refer to the values in 3e
