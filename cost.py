H = float(input('Enter height of floor: '))
W = float(input('Enter width of floor: '))
A = H * W
h = float(input('Enter height of tile: '))
w = float(input('Enter width of tile: '))
a= h * w
rs = float(input('Enter cost of 1 tile: '))
no_of_tiles = A/a
total_cost = no_of_tiles * rs
print('No of tiles = ',no_of_tiles)
print('Total Cost = ',total_cost)