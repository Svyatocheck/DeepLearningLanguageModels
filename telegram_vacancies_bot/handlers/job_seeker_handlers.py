from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from database.database import Database
from models.models import Form
from utils.messages import *
from handlers.common_handlers import job_seeker_main_menu, back_to_main_menu_keyboard
import asyncio
import logging

def register_job_seeker_handlers(dp: Dispatcher, bot : Bot, database : Database):
    pass

    # async def on_startup(_):
    #     """
    #     Initializes background tasks on bot startup.
    #     """
    #     asyncio.create_task(periodic_job_updates())


    # async def periodic_job_updates():
    #     """
    #     Sends periodic job updates to job seekers. Runs as a background task.
    #     """
    #     while True:
    #         try:
    #             # Assume get_job_seekers is an async function
    #             job_seekers = await database.get_job_seekers()
    #             for user_id in job_seekers:
    #                 try:
    #                     await bot.send_message(user_id, "Here's your periodic job update!")
    #                     await asyncio.sleep(0.1)  # Short delay to avoid rate limiting
    #                 except Exception as e:
    #                     # Handle exceptions from sending the message, e.g. user blocked the bot
    #                     logging.error(f"Error sending message to {user_id}: {e}")
    #         except Exception as e:
    #             # Handle exceptions from getting job seekers, e.g. database connection issue
    #             logging.error(f"Error retrieving job seekers: {e}")
    #         await asyncio.sleep(300)  # 1 hour interval


    # @dp.message_handler(state=Form.waiting_for_resume, content_types=['document'])
    # async def handle_resume(message: types.Message, state: FSMContext):
    #     """
    #     Handle resumes function + Output of parsed information
    #     Needs to be pretier
    #     """
    #     confirm_keyboard = InlineKeyboardMarkup(row_width=2)
    #     confirm_keyboard.add(InlineKeyboardButton(text="Yes", callback_data="correct_information_yes"),
    #                     InlineKeyboardButton(text="No", callback_data="correct_information_no"))
        
    #     # Process the resume
    #     extracted_data = "Name: John Doe, Skills: Python, Data Analysis"  # Placeholder

    #     await message.reply(f"Is this information correct?\n{extracted_data}", reply_markup=confirm_keyboard)
    #     await state.finish()  # Reset the state
        
    
    # @dp.callback_query_handler(lambda c: c.data and c.data.startswith('upload_resume'))
    # async def handle_upload_resume(callback_query: types.CallbackQuery):
    #     await bot.send_message(callback_query.from_user.id, "You are in upload resume dialog.", reply_markup=back_to_main_menu_keyboard())


    # @dp.callback_query_handler(lambda c: c.data and c.data.startswith('search_jobs'))
    # async def handle_search_jobs(callback_query: types.CallbackQuery):
    #     await bot.send_message(callback_query.from_user.id, "You are in search jobs dialog", reply_markup=back_to_main_menu_keyboard())


    # @dp.callback_query_handler(lambda c: c.data and c.data.startswith('view_applied_jobs'))
    # async def handle_applied_jobs(callback_query: types.CallbackQuery):
    #     await bot.send_message(callback_query.from_user.id, "You are in applied jobs dialog", reply_markup=back_to_main_menu_keyboard())


    # @dp.callback_query_handler(lambda c: c.data and c.data.startswith('profile_settings'))
    # async def handle_profile_settings(callback_query: types.CallbackQuery):
    #     await bot.send_message(callback_query.from_user.id, settings_message, reply_markup=back_to_main_menu_keyboard())


    # @dp.callback_query_handler(lambda c: c.data and c.data.startswith('help_support'))
    # async def handle_profile_settings(callback_query: types.CallbackQuery):
    #     await bot.send_message(callback_query.from_user.id, "You are in support dialog", reply_markup=back_to_main_menu_keyboard())