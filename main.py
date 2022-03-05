import random, turtle, time

#setting up the turtle screen
s = turtle.Screen()
s.setup(1000, 600)
s.bgcolor("black")
s.tracer(0)
s.title("list sorter visualizer")

#turtle renderer
bardrawer = turtle.Turtle()
bardrawer.hideturtle()
bardrawer.pensize(6)
bardrawer.color("white")

#generating the shuffled list
list = [i for i in range(100)]
random.shuffle(list)

#spitting bars
def drawbars(iterations, renderlist = list):
	bardrawer.clear()
	bardrawer.penup()
	for i in range(len(renderlist)):
		bardrawer.penup()
		turtx = i * 8 - 490
		bardrawer.goto(turtx, -300)
		bardrawer.pendown()
		bardrawer.goto(turtx, (renderlist[i] * len(list)/20) - 300)
	bardrawer.penup()
	bardrawer.goto(-450, 200)
	bardrawer.write("Iteration %s" % iterations, font = ("Courier", 16, "bold"))
	s.update()

#done and dusted
def done(finaltime):
	bardrawer.goto(-450, 250)
	bardrawer.write("Final time: %s seconds." % finaltime, font = ("Courier", 16, "bold"))

#testing out sort for mergesort
def sortsorted(list1, list2):
	newlist = []
	i = 0
	j = 0
	while(len(newlist) < len(list1) + len(list2)):
		if(list1[i] < list2[j]):
			newlist.append(list1[i])
			if(i == len(list1) - 1):
				break
			else:
				i += 1
		else:
			newlist.append(list2[j])
			if(j == len(list2) - 1):
				break
			else:
				j += 1
	return(newlist)

#Bubble sort
def bubblesort():
	pretime = time.perf_counter()
	iterations = 0
	#going through every item
	for i in range(len(list)):
		#don't have to go through things twice
		for j in range(1, len(list) - i):
			iterations += 1
			if(list[j] < list[j - 1]):
				list[j], list[j - 1] = list[j - 1], list[j]
				drawbars(iterations)
	posttime = time.perf_counter()
	done(round(posttime - pretime, 2))

def bogosort():
	global list
	iterations=  0
	inorder = False
	while not inorder:
		iterations += 1
		inorder2 = True
		random.shuffle(list)
		drawbars(iterations)
		for i in range(len(list) - 1):
			if(list[i] > list[i+1]):
				inorder2 = False
				break
		if(inorder2):
			inorder = True

#insertion sort
def insertionsort():
	pretime = time.perf_counter()
	iterations = 0
	for i in range(1, len(list)):
		iterations += 1
		key = list[i]
		j = i-1
		while j >= 0 and key < list[j] :
				list[j + 1] = list[j]
				j -= 1
		list[j + 1] = key
		drawbars(iterations)
	posttime = time.perf_counter()
	done(round(posttime - pretime, 2))


insertionsort()
print(list)


while True:
	s.update()
