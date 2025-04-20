import torch
import torch.nn as nn

def pgd_attack(
    model,
    x,
    y,
    epsilon,
    alpha,
    num_iter=10,
    loss_fn=nn.BCELoss(),
    targeted=False,
    rand_init=True
):
   
    model.eval()
    x_adv = x.clone().detach()
    
    # Random initialization within epsilon-ball
    if rand_init:
        x_adv = x_adv + torch.empty_like(x_adv).uniform_(-epsilon, epsilon)
        x_adv = torch.clamp(x_adv, 0, 1).detach()
    
    for _ in range(num_iter):
        x_adv.requires_grad = True
        
        # Forward pass
        outputs = model(x_adv)
        
        # Calculate loss
        loss = loss_fn(outputs, y)
        if targeted:
            loss = -loss  # Minimize loss for targeted attack
        
        # Compute gradients
        model.zero_grad()
        loss.backward()
        grad = x_adv.grad.data
        
        # Update adversarial example
        x_adv = x_adv.detach() + alpha * grad.sign()
        
        # Project back to epsilon-ball and valid pixel range
        delta = torch.clamp(x_adv - x, min=-epsilon, max=epsilon)
        x_adv = torch.clamp(x + delta, 0, 1).detach()
    
    return x_adv
