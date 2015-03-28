import uuid
class Guid(object):
    @staticmethod
    def New():
        id = uuid.uuid1()
        return uuid.uuid3(id,str(id))