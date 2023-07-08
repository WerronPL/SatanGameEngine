# import the engine
import SatanGameEngine as satan

# initialize the game
game = satan.Game()
game.show_fps = True

# create background
background = satan.Background(game.window, image = game.load_image("assets/background.png", 1.0))
game.add_object(background)

# create enemy
enemy = satan.Rect(game.window, image = game.load_image("assets/enemy.png", 0.5))
enemy.x = 100
enemy.y = 200
enemy.width = 20
enemy.height = 20
enemy.color = satan.COLOR.RED
game.add_object(enemy)

# create player
player = satan.Player(game.window, image = game.load_image("assets/player.png", 0.5))
player.x = 0
player.y = 0
player.width = 20
player.height = 20
player.color = satan.COLOR.GREEN
player.speed = 2
player.can_sprint = True
game.add_object(player)

# update enemy's position
game.move(enemy, player.get_new_pos, player.speed - 1)

# run the game
game.run()


