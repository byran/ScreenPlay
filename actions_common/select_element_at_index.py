from screenplay import Action, Actor, log_message


class _select_element_at_index_from_stored_list(Action):
    def __init__(self, index: int, id: str):
        super().__init__()
        self._index: int = index
        self._sourceId: str = id
        self._destinationId: str = None

    def and_store_in(self, id: str):
        self._destinationId = id
        return self

    @log_message('Selecting element {self._index} of \'{self._sourceId}\'')
    def perform_as(self, actor: Actor):
        items = actor.state[self._sourceId].value
        assert len(items) > self._index, "'{id}' does not have an enough elements to access element {index}" \
            .format(id=self._sourceId, index=self._index)

        item = items[self._index]

        if self._destinationId is not None:
            actor.state[self._destinationId].set(item)

        return item


class select_element_at_index:
    def __init__(self, index: int):
        super().__init__()
        self._index: int = index

    def from_stored_list(self, id: str):
        return _select_element_at_index_from_stored_list(self._index, id)
