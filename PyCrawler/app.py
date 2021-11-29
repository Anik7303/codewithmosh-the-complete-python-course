from bs4 import BeautifulSoup
import requests


try:
    response = requests.get('https://stackoverflow.com/questions')
    soup = BeautifulSoup(response.text, 'html.parser')

    questions = soup.select('.question-summary')
    for question in questions:
        title = question.select_one('.question-hyperlink').getText()
        vote_count = question.select_one('.vote-count-post').getText()
        print(f'title: {title} | vote: {vote_count}')
except Exception as ex:
    print(ex)
