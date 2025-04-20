import torch
import torch.nn as nn

def fgsm_attack(model, x, y, epsilon, loss_fn=torch.nn.BCELoss()):
   
    # Forward pass
    outputs = model(x)
    loss = loss_fn(outputs, y)
    
    # Zero gradients, backward pass
    model.zero_grad()
    loss.backward()
    
    # Get sign of gradients
    gradient_sign = x.grad.data.sign()
    
    # Create and return adversarial example
    x_adv = x + epsilon * gradient_sign
    return torch.clamp(x_adv, 0, 1)  # Clip to valid pixel range
