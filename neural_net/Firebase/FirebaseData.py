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
    def update(self):
        self.data = self.db.get().val()
    def aggregate(self):
        #picks apart the database values
        #first loop takes apart the dictionary making sure none are zero
        #second takes apart the last bit
        return [[j for j in self.data[i].values()] for i in self.data if i]
