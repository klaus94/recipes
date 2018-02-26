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
			description TEXT,
			incredients TEXT);"""
		self.cursor.execute(sqlCommand)
		self.connection.commit()

		# create image-database
		sqlCommand = """CREATE TABLE IF NOT EXISTS images (
			id INTEGER PRIMARY KEY,
			recepe_id INTEGER,
			image_file_name TEXT,
			thumbnail_file_path TEXT);"""
		self.cursor.execute(sqlCommand)
		self.connection.commit()

		self.closeConnection()

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
			incredientsString)
		)
		self.connection.commit()
		rowID = self.cursor.lastrowid
		self.closeConnection()

		return rowID

	def addImage(self, recepe_id, imgName):
		self.openConnection()

		# insert image into image-table
		sqlCommand = """INSERT INTO images (recepe_id, image_file_name) VALUES (?, ?);"""
		self.cursor.execute(sqlCommand, (recepe_id, imgName))
		self.connection.commit()

		self.closeConnection()

	def get_image_file_name(self, image_id):
		self.openConnection()
		self.cursor.execute("SELECT image_file_name FROM images i WHERE i.id = ?", (image_id, ))
		imagePaths = self.cursor.fetchone()

		if (len(imagePaths) != 1):
			return None
		self.closeConnection()

		return imagePaths[0]


	# todo: delete this, when other methods are ready
	def get_images_for_recepe(self, recepe_id):
		self.openConnection()
		self.cursor.execute(
			"""SELECT i.id FROM images i
				INNER JOIN recepe r ON r.id = i.recepe_id
				WHERE r.id = ?""", (recepe_id, ))
		imageIDs = self.cursor.fetchall()
		self.closeConnection()

		return [i[0] for i in imageIDs]


	def getRecepes(self):
		result = []

		self.openConnection()
		self.cursor.execute("SELECT * FROM recepe r")
		recepeList = self.cursor.fetchall()
		for ele in recepeList:
			incredList = []
			imageList = self.get_images_for_recepe(ele[0])
			if len(ele[4]) > 0:
				incredList = ele[4].split(",")
			result.append(Recepe(ele[0], ele[1], ele[2], ele[3], incredList, imageList))
		self.closeConnection()
		return result

	def getRecepe(self, recepe_id):
		self.openConnection()
		self.cursor.execute("SELECT * FROM recepe r WHERE r.id = ?", (recepe_id, ))
		results = self.cursor.fetchall()
		if (len(results) != 1):
			return None
		r = results[0]
		incredList = []
		imageList = self.get_images_for_recepe(r[0])
		if len(r[4]) > 0:
			incredList = r[4].split(",")
		result = Recepe(r[0], r[1], r[2], r[3], incredList, imageList)
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

	def openConnection(self):
		self.connection = sqlite3.connect("recepes.db")
		self.cursor = self.connection.cursor()

	def closeConnection(self):
		self.connection.close()

