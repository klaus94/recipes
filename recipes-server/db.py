#!/ usr/binenv python
# -*- coding : utf -8 -*-

import sqlite3
from Recepe import Recepe

class DB(object):
	def __init__(self):
		#... connect to database
		self.openConnection()

		sqlCommand = """CREATE TABLE IF NOT EXISTS recepe (
			id INTEGER PRIMARY KEY,
			name VARCHAR(20),
			category INTEGER,
			description VARCHAR(1000));"""
		self.cursor.execute(sqlCommand)
		self.connection.commit()
		self.closeConnection()

	def openConnection(self):
		self.connection = sqlite3.connect("recipes.db")
		self.cursor = self.connection.cursor()

	# for debugging	
	def clearDataBase(self):
		sqlCommand = """DELETE FROM recepe;"""
		self.cursor.execute(sqlCommand)
		self.connection.commit()

	def addRecipe(self, recipe):
		self.openConnection()

		formatString = """INSERT INTO recepe (name, category, description) 
			VALUES ("{name}", {category}, "{description}");"""
		sqlCommand = formatString.format(name = recipe.name, \
			category = recipe.category, \
			description = recipe.description)
		self.cursor.execute(sqlCommand)
		self.connection.commit()

		self.closeConnection()

	def getRecipes(self):
		self.openConnection()
		self.cursor.execute("SELECT * FROM recepe")
		recepeList = self.cursor.fetchall()
		result = []
		for ele in recepeList:
			result.append(Recepe(ele[0], ele[1], ele[2], ele[3]))
		self.closeConnection()
		return result

	# def storePoint(self, name, points):
	# 	# look up, if entry is in database
	# 	formatString = """SELECT playerName, points FROM points WHERE playerName = "{name}";"""
	# 	sqlCommand = formatString.format(name = name)
	# 	self.cursor.execute(sqlCommand)
	# 	self.connection.commit()
	# 	result = self.cursor.fetchall()

	# 	print("points: {0} result.points: {1}".format(points, result.points))
	# 	# delete existing entry
	# 	if ( (len(result) > 0) && (points > result.points) ):

	# 		formatString = """DELETE FROM points WHERE playerName = "{name}";"""
	# 		sqlCommand = formatString.format(name = name)
	# 		self.cursor.execute(sqlCommand)
	# 		self.connection.commit()

	# 		# add new entry
	# 		formatString = """INSERT INTO points (playerName, points) 
	# 			VALUES ("{name}", {points});"""
	# 		sqlCommand = formatString.format(name = name, points = points)
	# 		self.cursor.execute(sqlCommand)
	# 		self.connection.commit()

	# def deleteEntry(self, name):
	# 	# look up, if entry is in database
	# 	formatString = """SELECT playerName FROM points WHERE playerName = "{name}";"""
	# 	sqlCommand = formatString.format(name = name)
	# 	self.cursor.execute(sqlCommand)
	# 	self.connection.commit()

	# 	# delete existing entry
	# 	if ( len(self.cursor.fetchall()) ):
	# 		formatString = """DELETE FROM points WHERE playerName = "{name}";"""
	# 		sqlCommand = formatString.format(name = name)
	# 		self.cursor.execute(sqlCommand)
	# 		self.connection.commit()

	# def showSortedList(self):
	# 	self.cursor.execute("SELECT * FROM points")
	# 	pointList = self.cursor.fetchall()
	# 	pointList = sorted(pointList, key=lambda entry: entry[1])		#sort by points
		
	# 	place = 1
	# 	print("Bestenliste:")
	# 	for entry in pointList[::-1]:									#reverse list --> hightst point at the top
	# 		print("{0}. {1}: {2} Punkte".format(place, entry[0], entry[1]) )
	# 		place += 1

	# def getSortedList(self):
	# 	self.cursor.execute("SELECT * FROM points")
	# 	pointList = self.cursor.fetchall()
	# 	pointList = sorted(pointList, key=lambda entry: entry[1])		#sort by points
	# 	result = []
	# 	for entry in pointList[::-1]:									#reverse list --> hightst point at the top
	# 		result.append(entry)
	# 	return result

	def closeConnection(self):
		self.connection.close()

