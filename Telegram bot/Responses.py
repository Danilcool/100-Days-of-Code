from datetime import datetime



def sample_responses(input_text):
    user_message = str(input_text).lower()
    if user_message in ('hello','hi','hey'):
        return "Hi how are you "

    if user_message in ("who are you"):
        return "I am your helper Bot"

    if user_message in ('time','time?'):
        now = datetime.now()
        date_time = now.strftime("%d%m%y, %H:%M:%S")

        return str(date_time)
    return "I dont understand you"


