from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from database.database import Database
from models.models import User, Form
from utils.messages import *
import re
from parser.parser import parser


def is_url(text):
    url_pattern = re.compile(r'https?://\S+|www\.\S+')
    return url_pattern.search(text) is not None

def register_common_handlers(dp: Dispatcher, bot: Bot, database: Database):

    @dp.message_handler(commands=['start'])
    async def send_welcome(message: types.Message):
        """
        Sends a welcome message with role selection buttons (HR or Job Seeker).
        """
        role_keyboard = InlineKeyboardMarkup(row_width=2)
        role_keyboard.add(
            InlineKeyboardButton(text="👔 I'm an HR Professional", callback_data="role_hr"),
            InlineKeyboardButton(text="🔍 I'm a Job Seeker", callback_data="role_job_seeker"))
        await message.reply(welcome_message, reply_markup=role_keyboard)


    @dp.callback_query_handler(lambda c: c.data and c.data.startswith('role_'))
    async def handle_role_query(callback_query: types.CallbackQuery, state: FSMContext):
        """
        Handles the user's role selection from the inline buttons and updates user role.
        """
        role = callback_query.data.split('_')[1]
        user_id = callback_query.from_user.id

        if role == 'hr':
            response_text = hr_welcome_message
            await Form.waiting_for_job_description.set()
        else:
            response_text = job_seeker_sorry_message
            # await Form.waiting_for_resume.set()

        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id, response_text)

    # Useless functions for now        
    # @dp.callback_query_handler(lambda c: c.data and c.data.startswith('correct_information_'))
    # async def handle_correction_request(callback_query: types.CallbackQuery):
    #     """
    #     Initiates the process for the user to correct their information.
    #     """
    #     confirmation = callback_query.data.split('_')[2]
    #     if confirmation == 'no':
    #         await Form.waiting_for_user_data.set()
    #         await bot.send_message(callback_query.from_user.id, correction_prompt_message)
    #     else:
    #         await bot.send_message(callback_query.from_user.id, process_completed_message)
    #         await show_user_menu(callback_query.from_user.id)

    #     await bot.answer_callback_query(callback_query.id)


    # @dp.message_handler(state=Form.waiting_for_user_data)
    # async def process_new_user_data(message: types.Message, state: FSMContext):
    #     """
    #     Processes the new user data provided after a correction request.
    #     """
    #     # User's corrected information
    #     # Replace with database queries needed
    #     updated_data = message.text

    #     await message.reply(f"Your information has been updated to:\n{updated_data}")
    #     await bot.send_message(message.from_user.id, process_completed_message)
    #     show_appropriate_menu(user_id=message.from_user.id,
    #                           chat_id=message.chat.id)
    #     await state.finish()


    # @dp.message_handler(commands=['mycard'])
    # async def show_personal_card(message: types.Message):
    #     """
    #     Displays the user's personal information card with their details.
    #     """
    #     user_id = message.from_user.id

    #     # Assume get_job_seekers is an async function, that send queries to database
    #     user_data = database.get_user_data(user_id)

    #     if user_data:
    #         card = user_data.format_user_card(user_data)
    #         await message.reply(card)
    #     else:
    #         await message.reply("You haven't set up your information yet. Please upload your resume or enter your details.")


    # @dp.message_handler(commands=['menu'])
    # async def command_menu(message: types.Message):
    #     """
    #     Show the command center based on user's role
    #     """
    #     # Connect to database, otherwise will be have a lot of bugs
    #     user_id = message.from_user.id
    #     show_appropriate_menu(user_id=user_id, chat_id=message.chat.id)


    # @dp.callback_query_handler(lambda c: c.data == 'back_to_main_menu')
    # async def handle_back_to_main_menu(callback_query: types.CallbackQuery):
    #     """
    #     Show the command center based on user's role
    #     """
    #     user_id = callback_query.from_user.id
    #     show_appropriate_menu(
    #         user_id=user_id, chat_id=callback_query.from_user.id)
    #     await bot.answer_callback_query(callback_query.id)


    # async def show_hr_menu(chat_id):
    #     keyboard = hr_main_menu()
    #     await bot.send_message(chat_id, menu_prompt_message, reply_markup=keyboard)


    # async def show_user_menu(chat_id):
    #     keyboard = job_seeker_main_menu()
    #     await bot.send_message(chat_id, menu_prompt_message, reply_markup=keyboard)


    # async def show_appropriate_menu(chat_id, user_id):
    #     if not database.get_user_data(user_id).isHR:
    #         await show_user_menu(chat_id)
    #     else:
    #         await show_hr_menu(chat_id)
        
# def job_seeker_main_menu():
#     """
#     Main menu buttons for Job Seeker role
#     """
#     keyboard = InlineKeyboardMarkup(row_width=2)
#     keyboard.add(
#         InlineKeyboardButton(text="Upload Resume",
#                              callback_data="upload_resume"),
#         InlineKeyboardButton(text="Search Jobs", callback_data="search_jobs"),
#         InlineKeyboardButton(text="View Applied Jobs",
#                              callback_data="view_applied_jobs"),
#         InlineKeyboardButton(text="Profile Settings",
#                              callback_data="profile_settings"),
#         InlineKeyboardButton(text="Help/Support", callback_data="help_support")
#     )
#     return keyboard


# def hr_main_menu():
#     keyboard = InlineKeyboardMarkup(row_width=2)
#     keyboard.add(
#         InlineKeyboardButton(text="Post a Job Opening",
#                              callback_data="post_job"),
#         InlineKeyboardButton(text="View Posted Jobs",
#                              callback_data="view_jobs"),
#         InlineKeyboardButton(text="Review Applicants",
#                              callback_data="review_applicants"),
#         InlineKeyboardButton(text="Search Candidates",
#                              callback_data="search_candidates"),
#         InlineKeyboardButton(text="Settings", callback_data="hr_settings"),
#         InlineKeyboardButton(text="Help/Support",
#                              callback_data="hr_help_support")
#     )
#     return keyboard


# def back_to_main_menu_keyboard():
#     keyboard = InlineKeyboardMarkup()
#     keyboard.add(InlineKeyboardButton(
#         text="Back to Main Menu", callback_data="back_to_main_menu"))
#     return keyboard
