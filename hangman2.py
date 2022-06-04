import random

def hangman():
    word_list = ["сколопендроморф", "сковорода", "виселица",
                 "скоморох"]
    random_number = random.randint(0, 4)
    word = word_list[random_number]
    wrong = 0
    stages = ["",
              "________        ",
              "|               ",
              "|        |      ",
              "|        O      ",         
              "|       /|\     ",                           
              "|       / \     ",
              "|               "
              ]                                               
    remaining_letters = list(word)   
    letter_board = ["__"] * len(word)
    win = False                                             
    print("Добро пожаловать на казнь!")
    while wrong < len(stages) - 1:                  
        print("\n")                         
        quess  = input("Введите букву: ")    
        if quess in remaining_letters:                    
            char_index = remaining_letters.index(quess)
            letter_board[char_index] = quess          
            remaining_letters[char_index] = '$'
        else:                           
            wrong += 1                      
        print((" ".join(letter_board)))                
        e = wrong + 1                           
        print("\n".join(stages[0: e]))      
        if "__" not in letter_board:               
            print("Вы выиграли! Было загадано слово: "),
            print(" ".join(letter_board))                  
            win = True
            break                                   
    if not win:
            print("\n".join(stages[0: wrong]))
            print("Вы програли! Было загадано слово: {}.".format(word))

hangman()
