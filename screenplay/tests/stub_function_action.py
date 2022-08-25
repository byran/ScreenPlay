from screenplay import Actor, action_log_message


def stub_function_action(message: str):
    @action_log_message(message)
    def action(actor: Actor):
        pass
    return action
