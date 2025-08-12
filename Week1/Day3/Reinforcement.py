import gym
import torch
import torch.nn as nn
import torch.optim as optim

# Create environment
env = gym.make('CartPole-v1')

print("Observation space:", env.observation_space)
print("Action space:", env.action_space)

# Define model
model = nn.Sequential(
    nn.Linear(env.observation_space.shape[0], 64),
    nn.ReLU(),
    nn.Linear(64, 64),
    nn.ReLU(),
    nn.Linear(64, env.action_space.n)
)

optimizer = optim.Adam(model.parameters(), lr=0.001)
criterion = nn.CrossEntropyLoss()

# Training loop
n = 100
for episode in range(n):
    state, _ = env.reset()  # Gym new API
    done = False
    total_reward = 0
    
    while not done:
        state_tensor = torch.tensor(state, dtype=torch.float32)
        
        # Get action probabilities
        logits = model(state_tensor)
        action_probs = torch.softmax(logits, dim=0)
        
        # Sample action
        action = torch.multinomial(action_probs, num_samples=1).item()
        
        # Step environment
        next_state, reward, terminated, truncated, _ = env.step(action)
        done = terminated or truncated
        
        # Compute loss (target is the chosen action)
        optimizer.zero_grad()
        loss = criterion(logits.unsqueeze(0), torch.tensor([action], dtype=torch.long))
        loss.backward()
        optimizer.step()
        
        state = next_state
        total_reward += reward

    print(f"Episode {episode+1}, Total Reward: {total_reward}")

env.close()
