all_stydents = {'Denys Hoptarev', 'Godunov Nikita', "Dzyadzuh Yuriy", 'Trofimchuk Vladymir', 'Vorobieva Galina', 'Vladymir Savchenko',
                'Daniil Marynich', 'Korshunov Dmitriy', 'Conor McGregor'}
Python = {'Denys Hoptarev', 'Dzyadzuh Yuriy', "Vladymir Savchenko", 'Daniil Marynich'}
FrontEnd = {'Godunov Nikita', "Trofimchuk Vladymir", 'Denys Hoptarev', }
FullStack = {'Korshunov Dmitriy', 'Daniil Marynich', "Vorobieva Galina", 'Dzyadzuh Yuriy'}
Java = {'Conor McGregor', 'Daniil Marynich', "Trofimchuk Vladymir"}

print('Stydents who study in two or more group: ' + str(
    (Python & FrontEnd) | (Python & FullStack) | (Python & Java) | (FrontEnd & FullStack) | (FrontEnd & Java) | (
            FullStack & Java)))
print('Students not studying FrontEnd: ' + str(all_stydents - FrontEnd))
print('Students who study Python and Java: ' + str(Python | Java))