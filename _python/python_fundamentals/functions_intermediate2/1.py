x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

def change_value(x):
    x[1][0] = 15
    return(x)
print(change_value(x))

def change_last_name(students):
    students[0]['last_name']="Bryant"
    return students
print(change_last_name(students))

def change_first_name(sports_directory):
    sports_directory['soccer'][0]="Andres"
    return sports_directory
print(change_first_name(sports_directory))

def change_z(z):
    z[0]['y']=30
    return z
print(change_z(z))

