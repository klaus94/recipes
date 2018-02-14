#!/ usr/binenv python
# -*- coding : utf -8 -*-

class Recepe(object):
	def __init__(self, id, name, category, description):
		self.id = id
		self.name = name
		self.category = category
		self.description = description

	def serialize(self):
		return {
			'id': self.id, 
			'name': self.name,
			'category': self.category,
			'description': self.description
		}