import faiss as faiss
from database.faiss import faiss_search_e5
import pandas as pd

# DIMENSION = 312
DIMENSION = 768

class User:
    pass

# database.py
class Database:

    def __init__(self):
        # try:
        #     self.index = faiss.read_index(r'database/database_e5.index')
        # except Exception:
        self.index = faiss.IndexFlatL2(DIMENSION)
        embed = pd.read_csv(r'database/embed_e5.csv', index_col=0)
        vectors = embed.values.astype('float32')
        self.index.add(vectors)  


    def get_job_postings(self) -> pd.DataFrame:
        df = pd.read_csv(r'database/hh_database_clear.csv', index_col=0)
        return faiss_search_e5(r"temp/example.txt", self.index, df)

    def improve_vacancy(self, message) -> str:
        return f"You answered {message}"
    
    def get_hr_users(self):
        return self.hr_users

    def get_job_seekers(self):
        return self.hr_users
    
    def add_hr_users(self, user : User):
        self.hr_users.append(user)
    
    def add_job_seekers(self, user : User):
        self.job_seekers.append(user)
    
    def get_user_data(self, user_id):
        return self.user
    
    def set_current_user(self, user):
        """
        Temporary function to set current user
        """
        self.user = user
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.save_to_database()

    def save_to_database(self):
        faiss.write_index(self.index, r"database\database_e5.index")
    
        