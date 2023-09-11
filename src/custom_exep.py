class InstantiateCSVError(Exception):

    def __init__(self, message='Файл item.csv поврежден'):
        self.message = message
        super().__init__(self.message)
