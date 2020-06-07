from screenplay import Task, Actor, log_message
from actions_selenium import navigate_to


class open_google(Task):
    @log_message('Open google homepage')
    def perform_as(self, actor: Actor):
        actor.attempts_to(
            navigate_to('https://www.google.co.uk')
        )
