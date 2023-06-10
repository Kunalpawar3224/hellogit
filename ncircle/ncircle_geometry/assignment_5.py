# Formulas to be used:
# k = ((y2-y1) * (x3-x1) - (x2-x1) * (y3-y1)) / ((y2-y1)^2 + (x2-x1)^2)
# x4 = x3 - k * (y2-y1)
# y4 = y3 + k * (x2-x1)



def projection_of_point():
	'''Project the point G on given line
	'''

	# reference for equation of a line:https://content.byui.edu/file/b8b83119-9acc-4a7b-bc84-efacf9043998/1/Math-2-11-2.html#WS2
	# Take the coordinates of a point from the user
	x1 = int(input("Please enter x1 coordinate: "))   
	y1 = int(input("Please enter y1 coordinate: "))

	x2 = int(input("Please enter x2 coordinate: "))
	y2 = int(input("Please enter y2 coordinate: "))

	start_point = (x1,y1)
	end_point = (x2,y2)

	# let x3 and y3 be the point G
	x3 = int(input("Please enter first coordinate of point G x3: "))	
	y3 = int(input("Please enter second coordinate of point G y3: "))
	g = (x3, y3)

    # formula's
    # k = k = ((y2-y1) * (x3-x1) - (x2-x1) * (y3-y1)) / ((y2-y1)^2 + (x2-x1)^2)

    # first we find the numerator as k1
	k1 = ((y2-y1) * (x3-x1) - (x2-x1) * (y3-y1))

    # after that we find the denominator as k2
	k2 = ((y2-y1)**2) + ((x2-x1)**2)

	k = k1/k2

	# let x4 and y4 be the point on a line
	x4 = x3 - k * (y2-y1)
	y4 = y3 + k * (x2-x1)

	print(f"Point projecting on a given line is: {(x4, y4)}")

projection_of_point()