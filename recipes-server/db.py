#!/ usr/binenv python
# -*- coding : utf -8 -*-

import sqlite3
from Recepe import Recepe

class DB(object):
	def __init__(self):
		self.openConnection()

		# create recepe-database
		sqlCommand = """CREATE TABLE IF NOT EXISTS recepe (
			id INTEGER PRIMARY KEY,
			name VARCHAR(20),
			category INTEGER,
			description VARCHAR(1000),
			incredients TEXT);"""
		self.cursor.execute(sqlCommand)
		self.connection.commit()

		# create image-database
		sqlCommand = """CREATE TABLE IF NOT EXISTS images (
			id INTEGER PRIMARY KEY,
			thumbnail,
			recepe_id INTEGER,
			image BLOB);"""
		self.cursor.execute(sqlCommand)
		self.connection.commit()

		self.closeConnection()

	def openConnection(self):
		self.connection = sqlite3.connect("recepes.db")
		self.cursor = self.connection.cursor()

	# for debugging	
	def clearDataBase(self):
		sqlCommand = """DELETE FROM recepe;"""
		self.cursor.execute(sqlCommand)
		self.connection.commit()

	def addRecepe(self, recepe):
		self.openConnection()

		# delete all "," from incredients and make a string out of all incredients
		incredientsList = list(map(lambda incr: incr.replace(",", ""), recepe.incredients))
		incredientsString = ",".join(incredientsList)

		sqlCommand = """INSERT INTO recepe (name, category, description, incredients) 
			VALUES (?, ?, ?, ?);"""
		self.cursor.execute(sqlCommand, ( \
			recepe.name, \
			recepe.category, \
			recepe.description, \
			incredientsString )
		)
		self.connection.commit()
		rowID = self.cursor.lastrowid
		self.closeConnection()

		return rowID

	def addImage(self, recepe_id, image):
		self.openConnection()
		sqlCommand = """INSERT INTO images (recepe_id, image) VALUES (?, ?);"""
		self.cursor.execute(sqlCommand, (recepe_id, image))
		self.connection.commit()

		self.closeConnection()

	def get_image(self, image_id):
		self.openConnection()
		self.cursor.execute("SELECT image FROM images i WHERE i.id = ?", (image_id, ))
		image = self.cursor.fetchone()

		if (len(image) != 1):
			return None
		self.closeConnection()

		return image[0]

	def get_images_for_recepe(self, recepe_id):
		self.openConnection()
		self.cursor.execute(
			"""SELECT i.id FROM images i
				INNER JOIN recepe r 
				WHERE r.id = ? AND r.id = i.recepe_id""", (recepe_id, ))
		imageIDs = self.cursor.fetchall()
		self.closeConnection()

		return [i[0] for i in imageIDs]


	def getRecepes(self):
		self.openConnection()
		self.cursor.execute("SELECT * FROM recepe")
		recepeList = self.cursor.fetchall()
		result = []
		for ele in recepeList:
			incredString = ele[4]
			incredList = incredString.split(",")
			result.append(Recepe(ele[0], ele[1], ele[2], ele[3], incredList))
		self.closeConnection()
		return result

	def getRecepe(self, recepe_id):
		self.openConnection()
		print type(recepe_id)
		self.cursor.execute("SELECT * FROM recepe r WHERE r.id = ?", (recepe_id, ))
		results = self.cursor.fetchall()
		
		if (len(results) != 1):
			return None

		r = results[0]

		incredString = r[4]
		incredList = incredString.split(",")

		result = Recepe(r[0], r[1], r[2], r[3], incredList)
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

