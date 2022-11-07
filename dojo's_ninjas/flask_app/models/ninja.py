from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:
    db = 'dojos_and_ninjas_schema'
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojo_id = data['dojo_id']

    @classmethod
    def save(cls,data):
        query = "INSERT INTO ninjas (first_name,last_name,age,created_at,updated_at,dojo_id) VALUES (%(first_name)s,%(last_name)s,%(age)s,NOW(),NOW(),%(dojo_id)s)"
        return connectToMySQL(cls.db).query_db(query,data)
        
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas;"
        ninjas_from_db =  connectToMySQL(cls.db).query_db(query)
        ninjas =[]
        for n in ninjas_from_db:
            ninjas.append(cls(n))
        return ninjas