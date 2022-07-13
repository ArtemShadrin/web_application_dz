import json

from utils import load_candidates, get_all, get_by_pk, get_by_skill

from flask import Flask

app = Flask(__name__)

candidates = load_candidates('candidates.json')         # грузим Json
list_candidates = get_all(candidates)   # создаем список кандидатов


@app.route("/")
def page_list_candidates():
    return f'Список кандидатов\n {list_candidates}'


@app.route("/candidates/<int:x>")
def page_candidate(x):
    info_candidates = get_by_pk(candidates, x)
    return f'{info_candidates}'


@app.route("/skills/<x>")
def page_skills(x):
    candidates_by_skill = get_by_skill(candidates, x)
    return f'{candidates_by_skill}'


app.run()
