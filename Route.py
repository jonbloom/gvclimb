class Route(object):
	id = 0
	route_type = ""
	rating = ""
	rope = 0
	name = ""
	date_set = ""
	setter = ""
	base_color = "none"
	color_1 = "none"
	color_2 = "none"
	special_base = "none"
	def __init__(self,route_type,rating,rope,name,date_set,setter,base_color,color_1,color_2,special_base):
		self.route_type = route_type
		self.rating = rating
		self.rope = rope
		self.name = name
		self.date_set = date_set
		self.setter = setter
		self.base_color = base_color
		self.color_1 = color_1
		self.color_2 = color_2
		self.special_base = special_base