from flask_app.config.mysqlconnection import connectToMySQL

DATABASE = 'dojos_and_ninjas_schema'

class Ninja:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojo_id = data['dojo_id']

    @classmethod
    def get_all_ninjas(cls,**data):
        query = "SELECT * FROM ninjas WHERE dojo_id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query,data)
        all_ninjas = []
        for ninja in results:
            all_ninjas.append(cls(ninja))
        return all_ninjas

    @classmethod
    def create(cls,data):
        query = "INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s);"
        ninja_id = connectToMySQL(DATABASE).query_db(query,data)
        return ninja_id