from flask_app.config.mysqlconnection import connectToMySQL

DATABASE = 'dojos_and_ninjas_schema'

class Dojo:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all_dojos(cls):
        query = "SELECT * FROM dojos;"
        dojos_from_db = connectToMySQL(DATABASE).query_db(query)
        all_dojos = []
        for dojo in dojos_from_db:
            all_dojos.append(cls(dojo))
        return all_dojos

    @classmethod
    def get_one(cls, **data):
        query = "SELECT * FROM dojos WHERE dojos.id = %(id)s;"
        one_dojo = connectToMySQL(DATABASE).query_db(query,data)
        dojo = cls(one_dojo[0])
        return dojo

    @classmethod
    def add_dojo(cls,data):
        query = "INSERT INTO dojos (name) VALUES (%(name)s);"
        dojo_id = connectToMySQL(DATABASE).query_db(query,data)
        return dojo_id