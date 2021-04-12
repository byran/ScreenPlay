from screenplay import Task, Actor, log_message
from screenplay_selenium.actions import navigate_to


class open_duckduckgo(Task):
    @log_message('Open duckduckgo homepage')
    def perform_as(self, actor: Actor):
        actor.attempts_to(
            navigate_to('https://duckduckgo.com/')
        )
