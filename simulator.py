import numpy as np
from copy import deepcopy

class sim_object:
	# width = object width
	# height = Object Height 
	# occ_list = A list of tuples of the form: [(width,height),(x,y)] where each x,y coordinate
	# 			 specifies a "filled" cell of the object. The first tuple defines the object size.
	# occ_array = An array encoding the object. The first dimension is Y and the second is X.
	# *** NOTE: the array is transposed so that its easy to visually 'draw' out shapes
	def __init__(self,x,y,occ_list=None,occ_arr=None):
		if occ_arr != None:
			occ_arr = np.transpose(occ_arr)
			self.width = len(occ_arr)
			self.height = len(occ_arr[0])
			self.x = x
			self.y = y
			self.obj = deepcopy(occ_arr)
		elif occ_list != None:
			sys.exit("occ_list not currently implemented");
		else:
			sys.exit("Must pass either occ_list or occ_arr");
		self.preprocess()

	#Preprocessing to accelerate collision checking
	def preprocess(self):
		#create collision lookup table
		self.collide = [0]*4
		self.collide[0] = [float("inf")]*self.height
		self.collide[2] = [-1]*self.height
		self.collide[1] = [float("inf")]*self.width
		self.collide[3] = [-1]*self.width

		#populate collision LUT
		for i in range(0,self.width):
			for j in range(0,self.height):
				if self.obj[i][j] == 1:
					self.collide[0][j] = min(self.collide[0][j],i) #left collision
					self.collide[2][j] = max(self.collide[2][j],i) #right collision
					self.collide[1][i] = min(self.collide[1][i],j) #top collision
					self.collide[3][i] = max(self.collide[3][i],j) #bottom collision

		for i in range(0,4):
			for j in range(0,len(self.collide[i])):
				if self.collide[i][j] == float("inf"):
					self.collide[i][j] = -1
class simulator:

	# Width = world width
	# Height = World Height
	# Objects = a list of tuples of the form: [ (x,y,obj_arr)] 
	#			where: 
	#				x,y = top left corner of object
	#				obj_arr = an array encoding the object
	## NOTE: Currently only supports one object
	def __init__(self,width,height,objects):
		assert len(objects) == 1, "simulator currently supports only 1 object. %d objects provided." % len(objects)
		self.width = width
		self.height = height
		for obj in objects:
			#Ensure valid object
			assert obj.x+obj.width <= width and obj.x >= 0, "object out of bounds in x"
			assert obj.y+obj.height <= height and obj.y >= 0, "object out of bounds in y"
			#store object
			self.obj = obj

	#Direction: 0: left, 1: top, 2: right, 3: bottom
	def collision_check(loc,dir, obj_loc=None):
		pass
		

	#TODO: Implement animation
	def grasp_action(gripper_loc,gripper_dir, obj_loc=None, animate=False):
		pass
		#returns: (gripper x,gripper y,s1,s2,s3,cost_incurred)



if __name__ == "__main__":
	#Object in array form
	obj1 =	 		[[0,0,1,0,0],
					 [1,1,1,1,1],
					 [1,1,1,1,1]]

	obj2 =	 		[[0,0,0,0,0],
					 [0,1,1,1,0],
					 [0,0,0,1,0],
					 [0,0,0,0,0]]
	print "----"
	check_col_proc = sim_object(0,0,occ_arr=obj2)
	print check_col_proc.collide
	print "----"

	obj_simple = [[1]]



	#Create the object object <_< 
	test_obj = sim_object(1,1,occ_arr=obj_simple)

	#Create sim instance
	sim = simulator(5,5,[test_obj])
	
	print "Collision tables:"
	print test_obj.collide

	obj_arr = 		[[1,2,3,4,5],
					 [6,7,8,9,10],
					 [11,12,13,14,15]]