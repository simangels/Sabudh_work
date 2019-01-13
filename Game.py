class Graphics():
	size=0
	m_list=[]
	def __init__(self):
		print("What SIZE of broad you want to choose :- \n")
		self.size=int(input("Example:- (For 3x3 , Enter 3)\n"))
		for i in range(self.size):
			print(" ---"*(self.size))
			print("|   "*(self.size+1))
			if(i == self.size-1):
				print(" ---"*(self.size))
	
	def setboard(self): 
		for i in range(0,self.size*self.size):
			boundlist =[ i*self.size-1 for i in range(1,self.size+1)]
			if i not in boundlist:
				self.m_list.insert(i,"|   ")
			else:
				self.m_list.insert(i,"|   |")
		for i in range(0,self.size):
			print("")
			print(" ---"*(self.size))
			for j in range(0,self.size):
				print(self.m_list[i*self.size+j],end="")
			if(i == self.size-1):
				print("")
				print(" ---"*(self.size))

	def showboard(self): 
		for i in range(0,self.size):
			print("")
			print(" ---"*(self.size))
			for j in range(0,self.size):
				print(self.m_list[i*self.size+j],end="")
			if(i == self.size-1):
				print("")
				print(" ---"*(self.size))


class Back_End():	
	def user_input(self,graphics,sign):	
		s_coord =input("Enter the coordinate , where you want enter:-\n")
		coord = s_coord.split(",")
		x_coord =int(coord[0])-1
		y_coord =int(coord[1])-1
		s_fetch = graphics.m_list[x_coord*graphics.size+y_coord]
		test =[*s_fetch]
		if(not test[2]=="X"or test[2]=="O"):
			test[2]=sign
			graphics.m_list[x_coord*graphics.size+y_coord]="".join(test)
		else:
			self.user_input(graphics,sign)

	def check(self,graphics):
		#leftdigonal
		checklist=[ i*(graphics.size+1) for i in range(0,graphics.size)]
		self.sub_check(graphics,checklist)
		
		#rightdigonal
		checklist = [ (graphics.size-1)*(i+1) for i in range (0, graphics.size)]
		self.sub_check(graphics,checklist)
		
		#up-horizentally
		checklist =[ i for i in range(0,graphics.size)] 
		self.sub_check(graphics,checklist)

		#left-veritcally
		checklist = [ i*graphics.size for i in range(0 ,graphics.size) ]
		self.sub_check(graphics,checklist)
		
		#down-horizentally
		checklist = [ (graphics.size*(graphics.size-1))+i for i in range(0 ,graphics.size) ]
		self.sub_check(graphics,checklist)

		#right-vertically
		checklist=[ (graphics.size*(i+1))-1 for i in range(0 , graphics.size)]
		self.sub_check(graphics,checklist)
		
		#bettwen-vertically
		if(graphics.size>2):
			for x in range(1 ,graphics.size-1):
				checklist = [(graphics.size*i)+x for i in range(0,graphics.size)]
				self.sub_check(graphics,checklist)
		#bettween horizentally
		if(graphics.size>2):
			for x in range(1 ,graphics.size-1):
				checklist = [((graphics.size*x)+i) for i in range(0,graphics.size)]
				print(checklist)
				self.sub_check(graphics,checklist)
		
		
	def sub_check(self,graphics,checklist):
		x_gamepoint=0
		o_gamepoint=0
		for i in checklist:
			string=graphics.m_list[i]
			if   string[2] =="X":
				x_gamepoint= x_gamepoint+1
			elif string[2] =="O":
				o_gamepoint= o_gamepoint+1
			else:
				break
		if(x_gamepoint==graphics.size):
			print("X has won the game")
			graphics.showboard()
			exit()
		if(o_gamepoint==graphics.size):
			print("O has won the game")
			graphics.showboard()
			exit()
		




class Game():
	graphics = Graphics()
	graphics.setboard()
	backend = Back_End()
	for i in range(0,graphics.size*graphics.size):
		
		if(i%2==0):
			print("PLAYER X:-")
			backend.user_input(graphics,"X")
			backend.check(graphics)
			graphics.showboard()			

		else:
			print("PLAYER O:-")
			backend.user_input(graphics,"O")
			backend.check(graphics)
			graphics.showboard()
