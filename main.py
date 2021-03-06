#Line 3 to line 7 are all the setups to make B0b the bot
#You first have do install the python discord module into your computer. 
import discord
import config
import random

from discord.ext import commands

#Line 12 is the special character used to call a command. 
# For example, typing !game1 followed by a specific message will make B0b play a game with you. 
# The special character can be anything you want. 
client = commands.Bot(command_prefix = "!")

#Line 15 to line 18 tells you when the bot is online through running the code through your terminal on Macbook or Command Prompt on Window
@client.event
async def on_ready():
    #You can adjust the message below to be anything you want. I just wanted this to be a goofy project :D
    print("B0b is online, welcome MrWaffles")

#Line 23 to line 42 is the code that allows B0b to respond to you when you say one of the three things in line 23. 
#B0b will randomly respond with one of his options in line 25
#Again, the messages in line 25 and 26 can be anything you want
@client.event 
async def on_message(text):
    greetings = ["hello", "hi", "howdy"]
    responses = ["what", "hello", "wanna fight"]
    B0b_choice = random.choice(responses)
    if text.author == client.user:
        return

    if any(word in text.content.lower() for word in greetings):
        await text.channel.send(B0b_choice + " " + str(text.author))

    #Line 35 to line 36 is a little something extra I added where if you type the words between the quotes word for word in line 35, B0b will respond with "I'm sorry" followed by the person who said it    
    if text.content.startswith("Why must you troll me B0b"):
        await text.channel.send("I'm sorry " + str(text.author))
    
    #Line 39 to line 40 allows B0b to send everyone in the discord server a message when I type the words between the quotes in line 39
    if text.content.startswith("B0b Attendance"):
        await text.channel.send("@everyone" + " Roll call!")
    
    await client.process_commands(text)

#Line 45 to line 85 is the first game I created. Rock Paper Scissor
@client.command()
async def game1(general, message):
    #Line 48 takes in the user's message than lowercases it to match on of the options in line 49
    user = message.lower()
    rock_paper_scissor_game_options = ["rock", "paper", "scissor"]
    #Line 51 allows B0b to randomly pick one of the options in line 49 to use for the game
    B0b_choice_for_rock_paper_scissor = random.choice(rock_paper_scissor_game_options)
    #Line 55 to line 85 is composed of if, else, and else if statements
    #Line 55 to line 57 makes B0b inform the user the message in line 56 if they did not pick one of the three options in line 49
    #If the user did pick one of the three optiions, they can move on to line 58 to line 85
    if user not in rock_paper_scissor_game_options:
        await general.send("Pick rock, paper, or scissor boss")
        return
    else:
        #Line 60 to line 62 is the code used when B0b and the user chose the same option
        await general.send(B0b_choice_for_rock_paper_scissor)
        if B0b_choice_for_rock_paper_scissor == user:
            await general.send("Tie")

        #Line 66 to line 68 is when the user chose paper and B0b chose scissor
        #B0b will print line 67 when this occurs    
        elif user == "paper":
            if B0b_choice_for_rock_paper_scissor == "scissor":
                await general.send("Yaaaay I win")
            #Line 70 to line 71 is the outcome when user chooeses paper(line 66) and B0b chooses rock
            if B0b_choice_for_rock_paper_scissor == "rock":
                await general.send("You cheated...somehow")
        
        #Line 74 to line 78 is repeat of the code above but when the user chooses scissor
        elif user == "scissor":
            if B0b_choice_for_rock_paper_scissor == "rock":
                await general.send("I know you can do better")
            if B0b_choice_for_rock_paper_scissor == "paper":
                await general.send("cheater")
        
        #Line 80 to line 85 is repeat of the code above as well but when the user chooses rock
        elif user == "rock":
            if B0b_choice_for_rock_paper_scissor == "paper":
                await general.send("Never give up")
            if B0b_choice_for_rock_paper_scissor == "scissor":
                await general.send("I'm gonna tell MrWaffles to make me win all the time >:(")

#Line 88 to line 122 is basically the code for the rock, paper, scissors game; however, the words are replaced with emojis
@client.command()
async def game1emoji(general, message):
    user = message
    #You can acquire the emojis I used from https://emojipedia.org/
        #Copy and paste the emoji from their website into the code
    rock_paper_scissor_game_options_emoji_version = ["??????", "????", "????"]
    B0b_choice_for_rock_paper_scissor_game_emoji_version = random.choice(rock_paper_scissor_game_options_emoji_version)
    if user not in rock_paper_scissor_game_options_emoji_version:
        await general.send("Pick ??????, ????, or ????")
        return
    else:
        await general.send(B0b_choice_for_rock_paper_scissor_game_emoji_version)
        if B0b_choice_for_rock_paper_scissor_game_emoji_version == user:
            await general.send("Tie")

        elif user == "????":
            if B0b_choice_for_rock_paper_scissor_game_emoji_version == "??????":
                await general.send("Yaaaay I win")
            #Line 107 to line 108 is the outcome when user chooeses paper(line 103) and B0b chooses rock
            if B0b_choice_for_rock_paper_scissor_game_emoji_version == "????":
                await general.send("You cheated...somehow")
        
        #Line 111 to line 115 is repeat of the code above but when the user chooses scissor
        elif user == "??????":
            if B0b_choice_for_rock_paper_scissor_game_emoji_version == "????":
                await general.send("I know you can do better")
            if B0b_choice_for_rock_paper_scissor_game_emoji_version == "????":
                await general.send("cheater")
        
        #Line 118 to line 122 is repeat of the code above as well but when the user chooses rock
        elif user == "????":
            if B0b_choice_for_rock_paper_scissor_game_emoji_version == "????":
                await general.send("Never give up")
            if B0b_choice_for_rock_paper_scissor_game_emoji_version == "??????":
                await general.send("I'm gonna tell MrWaffles to make me win all the time >:(")
   
#Line 128 to line 166 is the second game I created. Heads or tails
#The concept is the same as the rock, paper, and scissor game, but it also includes the choice the computer makes as the user is competing against B0b on who guesses correctly.
#The computer decides whether it lands on heads or tails. 
#The "and" statement is used so it has to pass through both conditions for the code within to work
@client.command()
async def game2(general, message):
    user = message.lower()
    heads_tails_game_options = ["heads", "tails"]
    B0b_choice_for_heads_tails = random.choice(heads_tails_game_options)
    computer_choice_for_heads_tails = random.choice(heads_tails_game_options)
    if user not in heads_tails_game_options:
        await general.send("Pick heads or tails boss")
        return
    else:
        await general.send(B0b_choice_for_heads_tails)
        if B0b_choice_for_heads_tails == user and computer_choice_for_heads_tails:
            await general.send("B0b's Choice: " + B0b_choice_for_heads_tails)
            await general.send("It landed on: " + computer_choice_for_heads_tails)
            await general.send("Darn no one won")    

        elif user == "heads" and computer_choice_for_heads_tails == "heads":
            if B0b_choice_for_heads_tails == "tails":
                await general.send("B0b's Choice: " + B0b_choice_for_heads_tails)
                await general.send("It landed on: " + computer_choice_for_heads_tails)
                await general.send("You're too good :/")

        elif B0b_choice_for_heads_tails == "heads" and computer_choice_for_heads_tails == "heads":
            if user == "tails":
                await general.send("B0b's Choice: " + B0b_choice_for_heads_tails)
                await general.send("It landed on: " + computer_choice_for_heads_tails)
                await general.send("Better luck next time")
        
        elif user == "tails" and computer_choice_for_heads_tails == "tails":
            if B0b_choice_for_heads_tails == "heads":
                await general.send("B0b's Choice: " + B0b_choice_for_heads_tails)
                await general.send("It landed on: " + computer_choice_for_heads_tails)
                await general.send("Andy should code me to only win...")
        
        elif B0b_choice_for_heads_tails == "tails" and computer_choice_for_heads_tails == "tails":
            if user == "heads":
                await general.send("B0b's Choice: " + B0b_choice_for_heads_tails)
                await general.send("It landed on: " + computer_choice_for_heads_tails)
                await general.send("Andy should pay me for winning this many times???? ")
  
#Line 170 to line 173 is the code that informs the user of B0b's purpose and his functions. 
#Simply say !please_help
@client.command()
async def please_help(message):
    await message.send("I am a Bot that Andy made for a fun side project.")
    await message.send("(1)!game1 is rock paper scissor. Simply say !game1 followed by either rock, paper, or scissor to play against me. \n(1.5)!game1emoji is the emoji version of rock, paper, and scissors game. Simply say !game1emoji followed by either the rock, paper, or scissors emoji to play against me. \n(2)!game2 is heads or tails. Simply say !game2 followed by either heads or tails to try your luck :D.")

#Line 176 runs the token you created. I have this stored in another file so no one can change Bob's function.
client.run(config.Secret)