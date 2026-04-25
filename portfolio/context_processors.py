from .translations import TRANSLATIONS


def language(request):
    lang = request.session.get('language', 'en')
    if lang not in ('en', 'cs'):
        lang = 'en'
    return {
        'lang': lang,
        't': TRANSLATIONS[lang],
    }
