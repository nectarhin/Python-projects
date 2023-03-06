Gryffindor = 0
Ravenclaw = 0
Hufflepuff = 0
Slytherin = 0

# 1 Question
print('Q1) Do you like Dawn or Dusk?')
print('1) Dawn')
print('2) Dusk')
q1 = int (input())
if q1 == 1:
    Gryffindor += 1
    Ravenclaw += 1
    
    print('Gryffindor and Ravenclaw both get a +1\n')
    print('Gryffindor = ' + str(Gryffindor))
    print('Slytherin = ' + str(Slytherin))
    print('Hufflepuff = ' + str(Hufflepuff))
    print('Ravenclaw = ' + str(Ravenclaw),'\n')
    
elif q1 == 2:
    Hufflepuff += 1
    Slytherin += 1
    
    print('Hufflepuff and Slytherin both get a +1.\n')
    print('Gryffindor = ' + str(Gryffindor))
    print('Slytherin = ' + str(Slytherin))
    print('Hufflepuff = ' + str(Hufflepuff))
    print('Ravenclaw = ' + str(Ravenclaw),'\n')
else:
    print('"Wrong input."')
    
#2 Question
print("Q2) (When I'm dead, I want people to remember me as:")
print('1) The good')
print('2) The Great')
print('3) The wise')
print('4) The bold')
q2 = int(input())
if q2 == 1:
    Hufflepuff += 2
    print('Hufflepuff +2\n')
    
    print('Gryffindor = ' + str(Gryffindor))
    print('Slytherin = ' + str(Slytherin))
    print('Hufflepuff = ' + str(Hufflepuff))
    print('Ravenclaw = ' + str(Ravenclaw),'\n')
    
elif q2 == 2:
    Slytherin += 2
    print('Slytherin +2')
    
    print('Gryffindor = ' + str(Gryffindor))
    print('Slytherin = ' + str(Slytherin))
    print('Hufflepuff = ' + str(Hufflepuff))
    print('Ravenclaw = ' + str(Ravenclaw),'\n')
    
elif q2 == 3:
    Ravenclaw += 1   
    print('Ravenclaw +2')
    
    print('Gryffindor = ' + str(Gryffindor))
    print('Slytherin = ' + str(Slytherin))
    print('Hufflepuff = ' + str(Hufflepuff))
    print('Ravenclaw = ' + str(Ravenclaw),'\n')
    
elif q2 == 4:
    Gryffindor += 2   
    print('Gryffindor +2')
    
    print('Gryffindor = ' + str(Gryffindor))
    print('Slytherin = ' + str(Slytherin))
    print('Hufflepuff = ' + str(Hufflepuff))
    print('Ravenclaw = ' + str(Ravenclaw),'\n')
    
else:
    print('"Wrong input"')
    
#3 Question
print("Q3) Which kind of instrument most pleases your ear?")
print('1) The violin')
print('2) The trumpet')
print('3) The piano')
print('4) The drum')
q3 = int(input())

if q3 == 1:
    Slytherin += 4
    print('Slytherin +4')
    print('Gryffindor = ' + str(Gryffindor))
    print('Slytherin = ' + str(Slytherin))
    print('Hufflepuff = ' + str(Hufflepuff))
    print('Ravenclaw = ' + str(Ravenclaw))
    
elif q3 == 2:
    Hufflepuff += 4
    print('Hufflepuff +4')
    print('Gryffindor = ' + str(Gryffindor))
    print('Slytherin = ' + str(Slytherin))
    print('Hufflepuff = ' + str(Hufflepuff))
    print('Ravenclaw = ' + str(Ravenclaw))
    
elif q3 == 3:
    Ravenclaw += 1 
    print('Ravenclaw +4')
    print('Gryffindor = ' + str(Gryffindor))
    print('Slytherin = ' + str(Slytherin))
    print('Hufflepuff = ' + str(Hufflepuff))
    print('Ravenclaw = ' + str(Ravenclaw))
    
elif q3 == 4:
    Gryffindor += 4
    print('Gryffindor +4')
    print('Gryffindor = ' + str(Gryffindor))
    print('Slytherin = ' + str(Slytherin))
    print('Hufflepuff = ' + str(Hufflepuff))
    print('Ravenclaw = ' + str(Ravenclaw))
    
else:
    print('"Wrong input"')
    print('Gryffindor = ' + str(Gryffindor))
    print('Slytherin = ' + str(Slytherin))
    print('Hufflepuff = ' + str(Hufflepuff))
    print('Ravenclaw = ' + str(Ravenclaw))
    
# winner
if Gryffindor >= Ravenclaw and Gryffindor >= Hufflepuff and Gryffindor >= Slytherin:
  print('\n Gryffindor!')
elif Ravenclaw >= Hufflepuff and Ravenclaw >= Slytherin:
  print('\nRavenclaw!')
elif Hufflepuff >= Slytherin:
  print('\nHufflepuff!')
else:
  print('\nSlytherin!')




