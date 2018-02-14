#!flask/bin/python
from flask import Flask, jsonify, abort, make_response, request
from flask_cors import CORS
from db import DB
from Recepe import Recepe

app = Flask(__name__)
CORS(app)

db = DB()

# add test recepe
# newRec = Recepe(1, 'Buy groceries', 1, 'Milk, Cheese, Pizza, Fruit, Tylenol')
# db.addRecipe(newRec)


@app.route('/recepes/list', methods=['GET'])
def get_tasks():
	return jsonify([r.serialize() for r in db.getRecipes()])

@app.route('/recepes/<int:recipe_id>', methods=['GET'])
def get_task(recipe_id):
	recipe = [recipe for recipe in db.getRecipes() if recipe.id == recipe_id]
	if len(recipe) == 0:
		abort(404)
	return jsonify(recipe[0].serialize())

# @app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['GET'])
# def get_task(task_id):
# 	task = [task for task in tasks if task['id'] == task_id]
# 	if len(task) == 0:
# 		abort(404)
# 	return jsonify({'task': task[0]})

@app.route('/recepes/new', methods=['POST'])
def create_task():
	json = request.get_json()
	print json
	id = 0
	if 'id' in json:
		id = json['id']
	try:
		recipe = Recepe(id, json['name'], json['category'], json['description'])
		db.addRecipe(recipe)
	except Exception as e:
		return make_response(jsonify({'error': 'recepe has wrong format or some properties are missing'}), 400)
	
	return jsonify('success'), 201

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
	app.run(debug=True)