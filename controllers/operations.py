class MongoDBController:
    def get_notes(self):#it is important to send "self" as parameter event when the function does not recieve real args. This is
    # a Flask requisite
        return "Notes are: []"