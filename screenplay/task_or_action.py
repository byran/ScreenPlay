class TaskOrAction:
    def perform_as(self, actor):
        pass

    def __call__(self, actor):
        return self.perform_as(actor)
