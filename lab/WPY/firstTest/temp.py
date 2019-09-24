import time
import random
while True:
    player_victory=0
    enemy_victory=0
    for i in range(1,4):
        time.sleep(1.5)
        print('  \n——————现在是第 %s 局——————' % i)
        player_life = random.randint(100,150)
        player_attack = random.randint(30,50)
        enemy_life = random.randint(100,130)
        enemy_attack = random.randint(30,70)

        print('\n玩家血量 %s \n攻击 %s ' % (player_life,player_attack))

        print('\n敌人血量 %s \n攻击 %s ' % (enemy_life,enemy_attack))

        
        while player_life>0 and enemy_life>0:
            player_life = player_life - enemy_attack
            enemy_life = enemy_life - player_attack
            print('敌人发动攻击，玩家剩余血量 %s ' % player_life)
            print('玩家发动攻击，敌人剩余血量 %s ' % enemy_life)


        if  player_life > 0 and enemy_life <= 0:
            player_victory+=1
            print('玩家赢')
        elif player_life<=0 and enemy_life>0:
            enemy_victory+=1
            print('玩家输')
        else:
         print('平局')
            
    if player_victory>enemy_victory:
        print('玩家赢得胜利')
    elif player_victory<enemy_victory:
        print('敌人赢得胜利')
    else:
        print('双方平局')
        
    a1 = input('要继续游戏吗，请输入n退出，输入其他继续：')
    if a1 == 'n':
        break

print('%d X %.2f = %s' % (1.5,2.015,'字符串啊'))
print(list(range(1,3)))
print(list(range(2,3)))
for i in range(1,3):
    print(i,end=' ')