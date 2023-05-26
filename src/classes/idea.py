from datetime import date

class Idea:
    def __init__(self, title: str, description: str, content: str) -> None:
        self.__title = title
        self.__description = description
        self.__content = content
        self.__creation_date = date.today()
        
        if self.__title is None or self.__description is None or self.__content is None:
            raise ValueError("Title, Description and Content cannot be None")
        
    @property    
    def title(self) -> str:
        return self.__title
    
    @property
    def description(self) -> str:
        return self.__description
    
    @property
    def content(self) -> str:
        return self.__content
    
    @property
    def creation_date(self) -> date:
        return self.__creation_date
    
    @title.setter    
    def title(self, title: str) -> None:
        self.__title = title
        
    @description.setter
    def description(self, description: str) -> None:
        self.__description = description
    
    @content.setter        
    def content(self, content: str) -> None:
        self.__content = content
    
    @creation_date.setter 
    def creation_date(self, creation_date: date) -> None:
        self.__creation_date = creation_date