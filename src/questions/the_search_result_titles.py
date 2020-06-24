from screenplay import Actor, Question
from abilities.browse_the_web import browser_for
from pages.google_search_results import google_search_results


class the_search_result_titles(Question):
    def answered_by(self, actor: Actor):
        elements = browser_for(actor).find_elements(*google_search_results.titles)
        return [element.text for element in elements]
