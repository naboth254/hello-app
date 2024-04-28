import streamlit as st
import requests

def get_time_of_day():
    current_hour = datetime.now().hour
    if 5 <= current_hour < 12:
        return 'morning'
    elif 12 <= current_hour < 18:
        return 'afternoon'
    else:
        return 'evening'

def get_greeting(language):
    time_of_day = get_time_of_day()
    greetings = {
        'english': {
            'morning': 'Good morning',
            'afternoon': 'Good afternoon',
            'evening': 'Good evening'
        },
        'spanish': {
            'morning': 'Buenos días',
            'afternoon': 'Buenas tardes',
            'evening': 'Buenas noches'
        }
    }
    return greetings.get(language, greetings['english']).get(time_of_day)

def get_quote_of_the_day():
    url = "https://favqs.com/api/qotd"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data['quote']['body']
    else:
        return "Unable to fetch the quote of the day"

def main():
    st.title('Hello App')
    name = st.text_input('Enter your name:')
    language = st.selectbox('Select language:', ['English', 'Spanish'])
    language_code = 'english' if language == 'English' else 'spanish'
    
    if st.button('Greet'):
        greeting = get_greeting(language_code)
        if name:
            st.write(f'{greeting}, {name}!')
        else:
            st.write(f'{greeting}!')

    st.write('Quote of the day:')
    quote = get_quote_of_the_day()
    st.write(quote)

    st.write('Current date and time:', datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

if __name__ == '__main__':
    main()
