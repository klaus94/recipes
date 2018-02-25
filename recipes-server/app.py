#!flask/bin/python
from flask import Flask, jsonify, abort, make_response, request, send_file
from flask_cors import CORS
from db import DB
from Recepe import Recepe
from random import randrange

app = Flask(__name__)
CORS(app)

db = DB()

# add test recepe
# newRec = Recepe(1, 'Buy groceries', 1, 'Milk, Cheese, Pizza, Fruit, Tylenol')
# db.addrecepe(newRec)


@app.route('/recepes/list', methods=['GET'])
def get_recepes():
	return jsonify([r.serialize() for r in db.getRecepes()])

@app.route('/recepes/<int:recepe_id>', methods=['GET'])
def get_recepe(recepe_id):
	recepe = db.getRecepe(recepe_id)
	if recepe == None:
		abort(404)
	return jsonify(recepe.serialize())


@app.route('/recepes/new', methods=['POST'])
def create_recepe():
	json = request.get_json()
	id = 0
	description = ""
	if 'id' in json:
		id = json['id']
	if 'description' in json:
		description = json['description']
	try:
		recepe = Recepe(id, json['name'], json['category'], description, json['incredients'])
		id = db.addRecepe(recepe)
	except Exception as e:
		print e
		return make_response(jsonify({'error': 'recepe has wrong format or some properties are missing'}), 400)
	
	return jsonify(id), 201

@app.route('/recepes/<int:recepe_id>/images', methods=['GET'])
def get_images_for_recepe(recepe_id):
	return jsonify(db.get_images_for_recepe(recepe_id)), 200

@app.route('/images/new/<int:recepe_id>', methods=['POST'])
def add_image(recepe_id):
	print dir(request.files['image'])
	imgName = "img_" + str(randrange(0, 100000000)) + ".jpg"
	filePath = "images/" + imgName
	request.files['image'].save(filePath)

	db.addImage(recepe_id, imgName)
	return jsonify('success'), 201

# @app.route('/images/<int:image_id>', methods=['GET'])
# def get_image(image_id):
# 	return db.get_image(image_id)

@app.route('/images/<int:image_id>', methods=['GET'])
def get_image(image_id):
	fileName = db.get_image_file_name(image_id)
	path = "images/" + fileName

	return send_file(path, mimetype='image/jpeg')




@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
	task = [task for task in tasks if task['id'] == task_id]
	if len(task) == 0:
		abort(404)
	if not request.json:
		abort(400)
	if 'title' in request.json and type(request.json['title']) != unicode:
		abort(400)
	if 'description' in request.json and type(request.json['description']) is not unicode:
		abort(400)
	if 'done' in request.json and type(request.json['done']) is not bool:
		abort(400)
	task[0]['title'] = request.json.get('title', task[0]['title'])
	task[0]['description'] = request.json.get('description', task[0]['description'])
	task[0]['done'] = request.json.get('done', task[0]['done'])
	return jsonify({'task': task[0]})

@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
	task = [task for task in tasks if task['id'] == task_id]
	if len(task) == 0:
		abort(404)
	tasks.remove(task[0])
	return jsonify({'result': True})

@app.errorhandler(404)
def not_found(error):
	return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True)