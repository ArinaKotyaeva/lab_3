class DatabaseConnection:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.connection_string = "postgresql://localhost:5432/mydatabase"
            print("подключение к базе данных:", cls._instance.connection_string)
        return cls._instance
    
    def execute_query(self, query):
        print(f"запрос: {query}")
    
    def get_connection_string(self):
        return self.connection_string