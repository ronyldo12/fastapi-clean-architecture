class ValidationReturn():
    passed: bool
    #should be a array of string
    messages: str

    def __init__(self) -> None:
         self.passed = True
         self.messages = ""

    def error(self, message: str):
        self.passed = False
        self.messages += message+"\n"