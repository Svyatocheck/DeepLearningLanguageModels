from aiogram.dispatcher.filters.state import State, StatesGroup

class User:

    def __init__(self, user_id, isHR) -> None:
        self.user_id = user_id
        self.name = ''
        self.contacts = ''
        self.skills = []
        self.isHR = isHR

    def set_user_id(self, user_id):
        self.user_id = user_id
    
    def get_user_id(self):
        return self.user_id
    
    def set_hr_status(self, isHR):
        self.isHR = isHR
    
    def get_hr_status(self):
        return self.isHR
    
    def get_user_data(self, user_id):
        """
        Retrieves the user's data from storage. Placeholder function.
        """
        return None  # Placeholder

    def format_user_card(self, user_data):
        """
        Formats the user's data into a readable card format. Placeholder function.
        """
        return "User Information Card"  # Placeholder



class Form(StatesGroup):
    """
    Defines states for the user data update process.
    """
    waiting_for_user_data = State()

    waiting_for_role = State()  # User has started the conversation but hasn't chosen a role
    waiting_for_resume = State()  # User is expected to send a resume
    waiting_for_job_description = State()  # User is expected to send a job description