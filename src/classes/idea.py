class Idea:
    def __init__(self, title: str, description: str) -> None:
        self.title = title
        self.description = description
        
        if self.title is None or self.description is None:
            raise ValueError("Title and Description cannot be None")
        
    def get_title(self) -> str:
        return self.title
        
    def get_description(self) -> str:
        return self.description
    
    def set_title(self, title: str) -> None:
        self.title = title
        
    def set_description(self, description: str) -> None:
        self.description = description