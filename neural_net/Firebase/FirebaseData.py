import pyrebase
import pandas

class FirebaseData:
    def __init__(self):
        self.config = {
            "apiKey": "AIzaSyByP5STU5jf_kmCRh4YpqYYwj72o3FdIIE",
            "authDomain": "mlacceldata.firebaseapp.com",
            "databaseURL": "https://mlacceldata.firebaseio.com",
            "projectId": "mlacceldata",
            "storageBucket": "mlacceldata.appspot.com",
            "messagingSenderId": "238781593745"
        }
        self.firebase = pyrebase.initialize_app(self.config)
        self.db = self.firebase.database()
        self.update()
        #self.stream = self.db.stream(lambda message: self.db.get().val())
    def __repr__(self):
        return "FirebaseDataObject"
    def __str__(self):
        self.update()
        return(str(self.data))
    def update(self):
        self.data = self.db.get().val()
    def aggregate(self):
        temp = [i for i in self.data]
        print(123412341234)
        print(self.data)
        print(temp)
        self.matrix = pandas.DataFrame(temp).as_matrix()
        return self.matrix
