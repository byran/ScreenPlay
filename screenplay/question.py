class Question:
    def answered_by(self, actor):
        pass

    def __call__(self, actor):
        return self.answered_by(actor)
