################### Scope ####################

# player_health = 10
#
#
# def damage(player_health):
#
#
#   player_health -= 2
#   return player_health
#   print('damage taken')
#
#
# player_health = damage(player_health)
# print(player_health)

# def new_function():
#   enemies = ['zombie','skeliton','frog']
#   game_lavel = 3
#   if game_lavel > 2:
#     new_enemy = enemies[0]
#
# print(new_enemy)

''''
local scope is when function varible is created and this used in side a function thing of function as its own littlle world nothing that is set as varibles can be used
outside of it unlesss its passed into function like def function(varible,varible1). 

gloval scope are in the script varibles that are set outside of function that can be used by if while or statements but not functions

functions create almst like a new page where things they use 
'''


enemies = 1


def increase_enemies():


  print(enemies)
  return enemies + 1
print(enemies)


enemies = increase_enemies()

print(enemies)