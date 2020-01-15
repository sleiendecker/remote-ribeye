from flask_restful import Resource


class Hello(Resource):
    def get(self):
      print("self:", self)
      return {"message": "Hello, World!"}