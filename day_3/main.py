def intersect(range_1,range_2):
	x1,x2 = range_1[0], range_1[1]
	if x2<x1:
		x1,x2 = x2,x1
	x3,x4 = range_2[0], range_2[1]
	if x4<x3:
		x3,x4 = x4,x3
	return x1<=x3<=x2 or x1<=x4<=x2 or x3<=x1<=x4 or x3<=x2<=x4

def find_intersection(w1,w2):
	output = []
	for i,_ in enumerate(w1):
		if i>0:
			line_1 = (w1[i-1],w1[i])
			for j,_ in enumerate(w2):
				if j>0:
					line_2 = (w2[j-1],w2[j])
					# print(f'line_1: {line_1}, line_2: {line_2}')
					x_int = intersect((line_1[0][0],line_1[1][0]), (line_2[0][0],line_2[1][0]))
					y_int = intersect((line_1[0][1],line_1[1][1]), (line_2[0][1],line_2[1][1]))
					# print(f'x_int: {x_int}, y_int: {y_int}')
					if x_int and y_int:
						out_point = [line_1[0][0],line_2[0][1]]
						if line_2[0][0]==line_2[1][0]:
							out_point = [line_2[0][0],line_1[0][1]]
						output.append(out_point)
	return output

def manhattan_dist(points):
	return [abs(point[1]) + abs(point[0]) for point in points]


inp_1 = [i for i in input().split(',')]
inp_2 = [i for i in input().split(',')]
wire_1 = [[0,0]] #start at central port
wire_2 = [[0,0]] #start at central port



for i,move in enumerate(inp_1):
	next_point = list(wire_1[i])
	if move[0]=='R':
		next_point[0]+=int(move[1:])
	elif move[0]=='L':
		next_point[0]-=int(move[1:])
	elif move[0]=='U':
		next_point[1]+=int(move[1:])
	elif move[0]=='D':
		next_point[1]-=int(move[1:])
	wire_1.append(next_point)

for i,move in enumerate(inp_2):
	next_point = list(wire_2[i])
	if move[0]=='R':
		next_point[0]+=int(move[1:])
	elif move[0]=='L':
		next_point[0]-=int(move[1:])
	elif move[0]=='U':
		next_point[1]+=int(move[1:])
	elif move[0]=='D':
		next_point[1]-=int(move[1:])
	wire_2.append(next_point)

# print('wire_1:', wire_1)
# print('wire_2:', wire_2)
#print(intersect([0,0],[-5,5]))
intersections = find_intersection(wire_1,wire_2)
print('intersections:', intersections)
distances = manhattan_dist(intersections)
print('distances:',distances)
distances.sort()
print('Nearest intersections:',distances[1])

steps = []

for int_point in intersections:
	# print('int point:',int_point)
	num_steps_1 = 0
	num_steps_2 = 0
	for i,_ in enumerate(wire_1):
		if i>0:
			line = (wire_1[i-1],wire_1[i])
			# print('line:',line)
			x_int = intersect((line[0][0],line[1][0]),(int_point[0],int_point[0]))
			y_int = intersect((line[0][1],line[1][1]),(int_point[1],int_point[1]))
			if x_int and y_int:
				num_steps_1 += abs(wire_1[i-1][0] - int_point[0]) + abs(wire_1[i-1][1] - int_point[1])
				break
			num_steps_1 += abs(wire_1[i-1][0] - wire_1[i][0]) + abs(wire_1[i-1][1] - wire_1[i][1])
	for j,_ in enumerate(wire_2):
		if j>0:
			line = (wire_2[j-1],wire_2[j])
			# print('line:',line)
			x_int = intersect((line[0][0],line[1][0]),(int_point[0],int_point[0]))
			y_int = intersect((line[0][1],line[1][1]),(int_point[1],int_point[1]))
			if x_int and y_int:
				num_steps_2 += abs(wire_2[j-1][0] - int_point[0]) + abs(wire_2[j-1][1] - int_point[1])
				break
			num_steps_2 += abs(wire_2[j-1][0] - wire_2[j][0]) + abs(wire_2[j-1][1] - wire_2[j][1])
	steps.append(num_steps_1+num_steps_2)
print('steps:',steps)
steps.sort()
print('Fewest steps:',steps[1])

