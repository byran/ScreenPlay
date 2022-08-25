from screenplay import Actor, log_message


def stub_function_task(message: str):
    @log_message(message)
    def task(actor: Actor):
        pass
    return task
