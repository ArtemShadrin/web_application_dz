import json


def load_candidates(filename):
    """
    Загрузка данных из файла
    """
    with open("candidates.json", "r", encoding='utf-8') as read_file:
        data = json.load(read_file)
    return data


def get_all(candidates):
    """
    Покажем всех кандидатов
    """
    list_candidates = ''
    for i in candidates:
        list_candidates += f"""<pre>Имя кандидата: - {str(i['name'])}
Позиция кандидата: - {str(i['position'])} 
Навыки: - {str(i['skills'])}\n\n </pre>"""
    return list_candidates


def get_by_pk(candidates, pk=None):
    """
    Вернем кандидата по pk
    """
    info_candidates = ''
    index = pk - 1
    info_candidates += f""" <img src="{str(candidates[index]['picture'])}">
<pre>Имя кандидата: - {str(candidates[index]['name'])}
Позиция кандидата: - {str(candidates[index]['position'])} 
Навыки: - {str(candidates[index]['skills'])}\n\n </pre>"""
    return info_candidates


def get_by_skill(candidates, skill_name=None):
    """
    Вернем кандидатов по навыку
    """
    candidates_by_skill = ''
    lower_skill = skill_name.lower()
    title_skill = skill_name.title()
    for i in candidates:
        if lower_skill in i['skills']:
            candidates_by_skill += f"""<pre>Имя кандидата: - {str(i['name'])}
Позиция кандидата: - {str(i['position'])} 
Навыки: - {str(i['skills'])}\n\n </pre>"""
        if title_skill in i['skills']:
            candidates_by_skill += f"""<pre>Имя кандидата: - {str(i['name'])}
Позиция кандидата: - {str(i['position'])} 
Навыки: - {str(i['skills'])}\n\n </pre>"""
    return candidates_by_skill
