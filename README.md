# 2nd-game
Install Pygame: Make sure you have Pygame installed. You can install it via pip:

Install pygame using pip
pip install pygame



New Update : # Load player (airplane) image
airplane_img = pygame.image.load("airplane.png") # change this base on your png picture
airplane_img = pygame.transform.scale(airplane_img, (50, 50))  # Resize as needed


# Load bullet image
bullet_img = pygame.image.load("bullet.png") #change this base on your png picture
bullet_img = pygame.transform.scale(bullet_img, (10, 20))  # Resize as needed
