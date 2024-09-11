from elements.base_element import BaseElement


class Input(BaseElement):
    def send_keys(self, text):
        self.visibility_wait().semd_keys(text)

    def clear(self):
        self.visibility_wait().clear()
