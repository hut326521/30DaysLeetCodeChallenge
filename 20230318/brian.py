"""
Use a list to preserve the browsing history and a pointer to indicate the
current page.
"""


class BrowserHistory:
    history: list[str]
    current_page_index: int

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.current_page_index = 0

    def visit(self, url: str) -> None:
        self.current_page_index += 1
        self.history = self.history[:self.current_page_index]
        self.history.append(url)

    def back(self, steps: int) -> str:
        self.current_page_index = max(0, self.current_page_index - steps)
        return self.history[self.current_page_index]

    def forward(self, steps: int) -> str:
        self.current_page_index = min(
            len(self.history) - 1, self.current_page_index + steps
        )
        return self.history[self.current_page_index]
