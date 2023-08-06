from random import randint
yes_list=['yes','y', 'ye']
game_list=['rock','paper','scissors']
streak_list=[]
def win_streak():
    print(f'your best streak is...{(max(streak_list))}')
player= False
def game_start():
    wins=0
    while player == False:
        computer = game_list[randint(0, 2)]
        choice= input('select one of the choices given')
        try:
            if choice not in game_list:
                raise  ValueError('not a valid input, try again')
            else:
                if choice == computer:
                    print(computer)
                    print('tie')
                    print('your streak is...'+ streak_list[-1])
                else:
                    if choice == 'rock':
                        if computer == 'paper':
                            print(computer)
                            print('you lose!')
                            streak_list.append(0)
                            go_again = input('do you want to go again?')
                            if go_again not in yes_list:
                                print('oh well it was a good run here is your best streak...')
                                print(win_streak)
                                break
                            elif go_again in yes_list:
                                computer = game_list[randint(0, 2)]
                                continue
                        elif computer == 'scissors':
                            print(computer)
                            print('you won!')
                            wins += 1
                            streak_list.append(wins)
                            go_again = input('do you want to go again?')
                            if go_again not in yes_list:
                                print('oh well it was a good run here is your best streak...')
                                print(wins)
                                break
                            elif go_again in yes_list:
                                computer = game_list[randint(0, 2)]
                                continue
                    elif choice == 'paper':
                        if computer == 'scissors':
                            print(computer)
                            print('you lose!')
                            streak_list.append(0)
                            go_again = input('do you want to go again?')
                            if go_again not in yes_list:
                                print('oh well it was a good run here is your best streak...')
                                print(wins)
                                break
                            elif go_again in yes_list:
                                computer = game_list[randint(0, 2)]
                                continue
                        elif computer == 'rock':
                            print(computer)
                            print('you won!')
                            wins += 1
                            streak_list.append(wins)
                            go_again = input('do you want to go again?')
                            if go_again not in yes_list:
                                print('oh well it was a good run here is your best streak...')
                                print(wins)
                                break
                            elif go_again in yes_list:
                                computer = game_list[randint(0, 2)]
                                continue
                    elif choice == 'scissors':
                        if computer == 'rock':
                            print(computer)
                            print('you lose!')
                            streak_list.append(0)
                            go_again = input('do you want to go again?')
                            if go_again not in yes_list:
                                print('oh well it was a good run here is your best streak...')
                                print(wins)
                                break
                            elif go_again in yes_list:
                                computer = game_list[randint(0, 2)]
                                continue
                        elif computer == 'paper':
                            print(computer)
                            print('you won!')
                            wins +=1
                            streak_list.append(wins)
                            go_again= input('do you want to go again?')
                            if go_again not in yes_list:
                                print('oh well it was a good run here is your best streak...')
                                print(wins)
                                break
                            elif go_again in yes_list:
                                computer = game_list[randint(0, 2)]
                                continue
        except:
            print('not acceptable')
game_start()