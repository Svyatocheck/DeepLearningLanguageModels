from aiogram import Dispatcher
from aiogram import Bot, Dispatcher, executor, types
from database.database import Database
from models.models import User, Form
from handlers.common_handlers import *


def register_hr_handlers(dp: Dispatcher, bot : Bot, database : Database):
    
    @dp.message_handler(commands=['done'], state=Form.waiting_for_job_description)
    async def finish_link_cycle(message: types.Message, state: FSMContext):
        await state.finish()
        await message.reply("Link processing cycle finished. Feel free to type /start again.")


    @dp.message_handler(state=Form.waiting_for_job_description)
    async def handle_job_description(message: types.Message, state: FSMContext):
        if is_url(message.text):
            try:
                # keyboard = InlineKeyboardMarkup()
                # keyboard.add(InlineKeyboardButton(text="Improve my Job Description", callback_data="improve_vacancy"))'
                # , reply_markup=keyboard
                hr_workings(message.chat.id, message, r'temp/data.csv')
                await send_csv_file(message.chat.id, r'temp/data.csv')
                await message.reply("Here's your CSV file based on the provided link. You can send another link or type /done to finish.")
            except Exception as e:
                await message.reply(f"An error occurred: {str(e)}")
        else:
            await message.reply("That doesn't seem like a valid URL. Please send a valid link.")


    def hr_workings(userId, message, file_path):
        # Assuming parser processes the link and saves the result
        parser(message.text, r"temp/example.txt")
        
        # Load the result into a DataFrame and save as CSV
        df = database.get_job_postings()
        df.to_csv(file_path, index=False, encoding='utf-32')


    async def send_csv_file(chat_id, file_path):
        with open(file_path, 'rb') as file:
            await bot.send_document(chat_id, types.InputFile(file))

    # Useless for now
    # @dp.message_handler(commands=['hrmenu'])
    # async def show_hr_menu_handler(message: types.Message):
    #     keyboard = hr_main_menu()
    #     await message.answer("Select an option from the HR menu:", reply_markup=keyboard)


    # @dp.callback_query_handler(lambda c: c.data and c.data.startswith('post_job'))
    # async def handle_upload_job(callback_query: types.CallbackQuery):
    #     await bot.send_message(callback_query.from_user.id, "You are in upload job dialog.", reply_markup=back_to_main_menu_keyboard())


    # @dp.callback_query_handler(lambda c: c.data and c.data.startswith('view_jobs'))
    # async def handle_view_jobs(callback_query: types.CallbackQuery):
    #     await bot.send_message(callback_query.from_user.id, "You are in view jobs dialog", reply_markup=back_to_main_menu_keyboard())


    # @dp.callback_query_handler(lambda c: c.data and c.data.startswith('review_applicants'))
    # async def handle_review_applicants(callback_query: types.CallbackQuery):
    #     await bot.send_message(callback_query.from_user.id, "You are in applicants dialog", reply_markup=back_to_main_menu_keyboard())


    # @dp.callback_query_handler(lambda c: c.data and c.data.startswith('search_candidates'))
    # async def handle_search_candidates(callback_query: types.CallbackQuery):
    #     await bot.send_message(callback_query.from_user.id, "You are in search candidates dialog", reply_markup=back_to_main_menu_keyboard())


    # @dp.callback_query_handler(lambda c: c.data and c.data.startswith('hr_settings'))
    # async def handle_profile_settings(callback_query: types.CallbackQuery):
    #     await bot.send_message(callback_query.from_user.id, settings_message, reply_markup=back_to_main_menu_keyboard())
    

    # @dp.callback_query_handler(lambda c: c.data and c.data.startswith('hr_help_support'))
    # async def handle_profile_settings(callback_query: types.CallbackQuery):
    #     await bot.send_message(callback_query.from_user.id, "You are in support dialog", reply_markup=back_to_main_menu_keyboard())
        
    
    # @dp.callback_query_handler(lambda c: c.data == 'improve_vacancy', state=Form.waiting_for_job_description)
    # async def handle_improve_request(callback_query: types.CallbackQuery, state : FSMContext):
    #     await bot.send_message(callback_query.from_user.id, "Provide as a query you would like to have an answer related to your vacancy")
    #     await state.finish()
    #     await Form.waiting_for_query.set()


    # @dp.message_handler(content_types=['text'], state=Form.waiting_for_query)
    # async def handle_improve_request_query(message: types.Message, state : FSMContext):
    #     improvements = database.improve_vacancy(message.text)
    #     await state.finish()
    #     await message.reply(improvements)
    #     await message.reply("Here is your suggestions. Feel free to send us another link to vacancy.")
    #     await Form.waiting_for_job_description.set()






