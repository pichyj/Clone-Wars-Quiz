#quiz on star wars the clone wars
print('Welcome to this fun quiz! There will be 20 questions in total')
ask_play = input('Do you want to play this quiz? ')

if ask_play.lower() != 'yes':
    quit()

ask_starwars = input('Do you know anything about Star Wars: The Clone Wars? Answer with yes, no, a little. ')

if ask_starwars == 'yes':
    print('You may do very well!')
    print("Yay! Let's continue!")
if ask_starwars == 'no':
    print('You will struggle on this quiz.')
    print("But that's okay, let's continue!")
if ask_starwars == 'a little':
    print('You might need some luck.')
    print("There is no harm in trying, let's continue!")

count = 0

answer = input('1) Who is Anakin Skywalker in the Clone Wars? ')
if answer.lower() == 'jedi' or answer.lower() == 'a jedi':
    print('Correct!')
    count += 1
else:
    print('Incorrect!')

answer = input('2) After the youngling stage, what are jedis in training called? ')
if answer.lower() == 'padawan':
    print('Correct!')
    count += 1
else:
    print('Incorrect!')

answer = input('3) Who died at the Citadel and was rescued in season 7 of the Clone Wars? ')
if answer.lower() == 'echo':
    print('Correct!')
    count += 1
else:
    print('Incorrect!')

answer = input("4) Which clone is called 'Captain' before their name? ")
if answer.lower() == 'rex' or answer.lower() == 'captain rex':
    print('Correct!')
    count += 1
else:
    print('Incorrect!')

answer = input('5) Which clone was known as a deserter? ')
if answer.lower() == 'cut' or answer.lower() == 'cut lawquane' or answer.lower() == 'lawquane':
    print('Correct!')
    count += 1
else:
    print('Incorrect!')

answer = input('6) Which clone killed Jedi General Pong Krell? ')
if answer.lower() == 'dogma':
    print('Correct')
    count += 1
else:
    print('Incorrect!')

answer = input("7) What is Fives's clone number? Answer does not need CT. ")
if answer.lower() == '5555':
    print('Correct!')
    count += 1
else:
    print('Incorrect!')

answer = input("8) Who was Anakin Skywalker's padawan? ")
if answer.lower() == 'ahsoka tano' or answer.lower() == 'ahsoka':
    print('Correct!')
    count += 1
else:
    print('Incorrect!')

answer = input("9) Who killed Jango Fett? ")
if answer.lower() == 'jedi master mace windu' or answer.lower() == 'mace windu' or answer.lower() == 'jedi mace windu':
    print('Correct!')
    count += 1
else:
    print('Incorrect')

answer = input('10) What number order forces all clones to kill the jedi? ')
if answer.lower() == '66':
    print('Correct!')
    count += 1
else:
    print('Incorrect!')

answer = input('11) Who says that experience outranks everything? ')
if answer.lower() == 'rex' or answer.lower() == 'captain rex':
    print('Correct!')
    count += 1
else:
    print('Incorrect!')

answer = input('12) Who killed Jedi Master Tiplar? ')
if answer.lower() == 'tup' or answer.lower() == 'cutup':
    print('Correct!')
    count += 1
else:
    print('Incorrect!')

answer = input('13) In season 7, a group of defective clones are introduced, what are the called? ')
if answer.lower() == 'the bad batch' or answer.lower() == 'bad batch' or answer.lower() == 'clone force 99':
    print('Correct!')
    count += 1
else:
    print('Incorrect!')

answer = input("14) What is the droid's name who helped assist Fives in discovering the inhibitor chips? ")
if answer.lower() == 'azi' or answer.lower() == 'azi-3' or answer.lower() == 'azi 3' or answer.lower() == 'azi-345211896246498721347':
    print('Correct!')
    count += 1
else:
    print('Incorrect!')

answer = input('15) Name one member of the Domino squad.')
if answer.lower() == 'sev' or answer.lower() == 'boss' or answer.lower() == 'fixer' or answer.lower() == 'scorch':
    print('Correct!')
    count += 1
else:
    print('Incorrect!')

answer = input('16) Name one member of the Delta squad. ')
if answer.lower() == 'echo' or answer.lower() == 'fives' or answer.lower() == 'tup' or answer.lower() == 'cutup' or answer.lower() == 'hevy' or answer.lower() == 'droidbait':
    print('Correct!')
    count += 1
else:
    print('Incorrect!')

answer = input('17) Who framed Ahsoka Tano for murder? ')
if answer.lower() == 'barriss' or answer.lower() == 'barriss offee' or answer.lower() == 'offee':
    print('Correct!')
    count += 1
else:
    print('Incorrect!')

answer = input('18) What ARC trooper joined The Bad Batch? ')
if answer.lower() == 'echo':
    print('Correct!')
    count += 1
else:
    print('Incorrect!')

answer = input("19) Who was Count Dooku's padawan? ")
if answer.lower() == 'jedi master qui-gon' or answer.lower() == 'qui-gon' or answer.lower() == 'jedi master qui gon' or answer.lower() == 'qui gon':
    print('Correct!')
    count += 1
else:
    print('Incorrect!')

answer = input('20) Who appears in the finale of the Clone Wars? ')
if answer.lower() == 'darth vader' or answer.lower() == 'vader':
    print('Correct!')
    count += 1
else:
    print('Incorrect!')

print('')
print(count)
print('')
print('You scored', count, 'out of 20!')
if count >= 15:
    print('You are a true Star Wars nerd. You really know your stuff, keep it up. May the force be with you.')
elif 14 >= count >= 6:
    print('Eh, you need to watch Star Wars: The Clone Wars, then try again.')
else:
    print('Why did you even bother taking this quiz?')
print('')
print('Thanks for playing!')


