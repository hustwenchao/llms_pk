class Task:
    def __init__(self, prompt, content):
        """
        :param prompt: The prompt of the task
        :param content: The content of the task
        """
        self.prompt = prompt
        self.content = content

    def __str__(self):
        return f"{self.name} - {self.priority}"