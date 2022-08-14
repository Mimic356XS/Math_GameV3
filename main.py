from msilib.schema import Font


def main():

    from colorama import Fore, Back, Style
    import random
    import fontstyle # fontsytle syntax: text = fontstyle.apply('GEEKSFORGEEKS', 'bold/Italic/red/GREEN_BG')

    #title
    print(f"{Fore.GREEN}{Back.BLACK}{Style.NORMAL}███████████████████████████████████████████████████████████████████████████████████")
    print(f"{Fore.GREEN}{Back.BLACK}{Style.NORMAL}█▄─▀█▀─▄█▄─██─▄█▄─▄███─▄─▄─█▄─▄█▄─▄▄─█▄─▄███▄─▄█─▄▄▄─██▀▄─██─▄─▄─█▄─▄█─▄▄─█▄─▀█▄─▄█")
    print(f"{Fore.GREEN}{Back.BLACK}{Style.NORMAL}██─█▄█─███─██─███─██▀███─████─███─▄▄▄██─██▀██─██─███▀██─▀─████─████─██─██─██─█▄▀─██")
    print(f"{Fore.GREEN}{Back.BLACK}{Style.NORMAL}█▄▄▄█▄▄▄██▄▄▄▄██▄▄▄▄▄██▄▄▄██▄▄▄█▄▄▄███▄▄▄▄▄█▄▄▄█▄▄▄▄▄█▄▄█▄▄██▄▄▄██▄▄▄█▄▄▄▄█▄▄▄██▄▄█")

    PlayQuit = input(f"{Fore.MAGENTA}type play, or type quit : ")
    if PlayQuit.lower() != "play":
        exit()
    if PlayQuit.lower() == "play":
        pass
    if PlayQuit.lower() == "quit":
        exit()
    if PlayQuit.lower() == "Quit":
        exit()

    Player_name = input(f"{Fore.CYAN}What is your name? : ")

    score = 0
    level = 1
    lives = 3
    # ranks in a tuple
    rank = (f"{Fore.BLACK}{Style.DIM}Coal I", f'{Fore.BLACK}Coal II', f'{Fore.BLACK}Coal III', # 0, 1, 2
    f'{Fore.YELLOW}{Style.DIM}Copper I', f'{Fore.YELLOW}{Style.DIM}Copper II', f'{Fore.YELLOW}{Style.DIM}Copper III',  # 3, 4, 5
    f'{Fore.WHITE}{Style.BRIGHT}Iron I', f'{Fore.WHITE}{Style.BRIGHT}Iron II', f'{Fore.WHITE}{Style.BRIGHT}Iron III', # 6, 7, 8
    f'{Fore.YELLOW}{Style.BRIGHT}Gold I', f'{Fore.YELLOW}{Style.BRIGHT}Gold II', f'{Fore.YELLOW}{Style.BRIGHT}Gold III', # 9, 10, 11
    f'{Fore.CYAN}{Style.BRIGHT}Diamond I', f'{Fore.CYAN}{Style.BRIGHT}Diamond II', f'{Fore.CYAN}{Style.BRIGHT}Diamond III', # 12, 13, 14
    f'{Fore.LIGHTGREEN_EX}{Style.BRIGHT}Emerald I', f'{Fore.LIGHTGREEN_EX}{Style.BRIGHT}Emerald II', f'{Fore.LIGHTGREEN_EX}{Style.BRIGHT}Emerald III', # 15, 16,17
    f'{Fore.RED}{Style.DIM}Netherite I', f'{Fore.RED}{Style.DIM}Netherite II', f'{Fore.RED}{Style.DIM}Netherite III'); # 18, 19, 20

    while True:
        x = random.randint(1, 1) 
        y = random.randint(1, 1)

        questiontxt = fontstyle.apply("What is " + str(x) + " Times " + str(y) + " ?", 'bold/Underline/blue/BLACK_BG')
       
        print(questiontxt) # question asker
            

        answer = int(input(f"Answer: "))
        # Checking Answer and Scoring

        correct = fontstyle.apply('Correct !', 'bold/Italic/green/BLACK_BG')
        correct2 = fontstyle.apply('--------------------------------', 'bold/Italic/blue/BLACK_BG')
        scoretxt = fontstyle.apply('Score : ', 'bold/Underline/yellow/BLACK_BG')
        livestxt = fontstyle.apply('Lives : ', 'bold/Underline/red/BLACK_BG')
        leveltxt = fontstyle.apply('Level : ', 'bold/Underline/purple/BLACK_BG')
        incorrect = fontstyle.apply('Correct !', 'bold/Strike/red/BLACK_BG')
        incorrect2 = fontstyle.apply(', The answer was ' + str(x*y) + " ", 'bold/Italic/red/BLACK_BG')

        # Ranks
        rank0 = fontstyle.apply("[  You are now rank : " + rank[0] + " ]", 'bold/Underline/darkcyan/BLACK_BG') # 0
        rank1 = fontstyle.apply("[  You are now rank : " + rank[1] + " ]", 'bold/Underline/darkcyan/BLACK_BG') # 1
        rank2 = fontstyle.apply("[  You are now rank : " + rank[2] + " ]", 'bold/Underline/darkcyan/BLACK_BG') # 2
        rank3 = fontstyle.apply("[  You are now rank : " + rank[3] + " ]", 'bold/Underline/darkcyan/BLACK_BG') # 3
        rank4 = fontstyle.apply("[  You are now rank : " + rank[4] + " ]", 'bold/Underline/darkcyan/BLACK_BG') # 4
        rank5 = fontstyle.apply("[  You are now rank : " + rank[5] + " ]", 'bold/Underline/darkcyan/BLACK_BG') # 5
        rank6 = fontstyle.apply("[  You are now rank : " + rank[6] + " ]", 'bold/Underline/darkcyan/BLACK_BG') # 6
        rank7 = fontstyle.apply("[  You are now rank : " + rank[7] + " ]", 'bold/Underline/darkcyan/BLACK_BG') # 7
        rank8 = fontstyle.apply("[  You are now rank : " + rank[8] + " ]", 'bold/Underline/darkcyan/BLACK_BG') # 8
        rank9 = fontstyle.apply("[  You are now rank : " + rank[9] + " ]", 'bold/Underline/darkcyan/BLACK_BG') # 9
        rank10 = fontstyle.apply("[  You are now rank : " + rank[10] + " ]", 'bold/Underline/darkcyan/BLACK_BG') # 10
        rank11 = fontstyle.apply("[  You are now rank : " + rank[11] + " ]", 'bold/Underline/darkcyan/BLACK_BG') # 11
        rank12 = fontstyle.apply("[  You are now rank : " + rank[12] + " ]", 'bold/Underline/darkcyan/BLACK_BG') # 12
        rank13 = fontstyle.apply("[  You are now rank : " + rank[13] + " ]", 'bold/Underline/darkcyan/BLACK_BG') # 13
        rank14 = fontstyle.apply("[  You are now rank : " + rank[14] + " ]", 'bold/Underline/darkcyan/BLACK_BG') # 14
        rank15 = fontstyle.apply("[  You are now rank : " + rank[15] + " ]", 'bold/Underline/darkcyan/BLACK_BG') # 15
        rank16 = fontstyle.apply("[  You are now rank : " + rank[16] + " ]", 'bold/Underline/darkcyan/BLACK_BG') # 16
        rank17 = fontstyle.apply("[  You are now rank : " + rank[17] + " ]", 'bold/Underline/darkcyan/BLACK_BG') # 17
        rank18 = fontstyle.apply("[  You are now rank : " + rank[18] + " ]", 'bold/Underline/darkcyan/BLACK_BG') # 18
        rank19 = fontstyle.apply("[  You are now rank : " + rank[19] + " ]", 'bold/Underline/darkcyan/BLACK_BG') # 19
        rank20 = fontstyle.apply("[  You are now rank : " + rank[20] + " ]", 'bold/Underline/darkcyan/BLAXK_BG') # 20
        


        if answer == (
                x * y):

            print(correct)
            print(correct2)

            score += 10

            print(scoretxt, score,
                  leveltxt, level,
                  livestxt, lives)

        else:  # <-- if the player gets the question incorrect
            score -= 2 # score
            lives -= 1 # lives
            print(incorrect + incorrect2,
                  
                  scoretxt, score,
                  leveltxt, level,
                  livestxt, lives)

        if score == 10 and level == 1:
            level += 1
            print(rank0)

        if score == 20 and level == 2:
            level += 1
            print(rank1)

        if score == 30 and level == 3:
            level += 1
            print(rank2)

        if score == 40 and level == 4:
            level += 1
            print(rank3)

        if score == 50 and level == 5:
            level += 1
            print(rank4)

        if score == 60 and level == 6:
            level += 1
            print(rank5)

        if score == 70 and level == 7:
            level += 1
            print(rank6)
        
        if score == 80 and level == 8:
            level += 1
            print(rank7)

        if score == 90 and level == 9:
            level += 1
            print(rank8)

        if score == 100 and level == 10:
            level += 1
            print(rank9)

        if score == 110 and level == 11:
            level += 1
            print(rank10)

        if score == 120 and level == 12:
            level += 1
            print(rank11)

        if score == 130 and level == 13:
            level += 1
            print(rank12)

        if score == 140 and level == 14:
            level += 1
            print(rank13)

        if score == 150 and level == 15:
            level += 1
            print(rank14)

        if score == 160 and level == 16:
            level += 1
            print(rank15)

        if score == 170 and level == 17:
            level += 1
            print(rank16)
        
        if score == 180 and level == 18:
            level += 1
            print(rank17)

        if score == 190 and level == 19:
            level += 1
            print(rank18)

        if score == 200 and level == 20:
            level += 1
            print(rank19)

        if score == 210 and level == 21:
            level += 1
            print(rank20)

main()
