class NewsPaginator:
    def __init__(self, headlines, per_page=3):
        self.headlines = headlines
        self.per_page = per_page
        self.page = 0
        
    def __iter__(self):
        return self
        
    def __next__(self):
        start = self.page * self.per_page
        if start >= len(self.headlines):
            raise StopIteration
        self.page += 1
        return self.headlines[start:start+self.per_page]

print("\nNews Pagination:")
headlines = [f"Headline {i}" for i in range(1, 10)]
paginator = NewsPaginator(headlines)
print(next(paginator))  
print(next(paginator))  