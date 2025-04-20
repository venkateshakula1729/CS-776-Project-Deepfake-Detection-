# Note: Since we realised that actual one-pixel attack uses differential evolution and implementing it is
#        computationally expensive and complicated, we sticked to this basic implementaion in some parts of our models
def one_pixel_attack(images, pixel_count=1):
    perturbed = images.clone()
    batch_size, _, h, w = images.shape
    for i in range(batch_size):
        for _ in range(pixel_count):
            x, y = np.random.randint(0, h), np.random.randint(0, w)
            perturbed[i, :, x, y] = torch.rand(3)
    return perturbed
