class language():
    def say_hello(self):
        raise NotImplementedError("Please get from child class")
    
class french(language):
    def say_hello(self):
        print("Bonjour: ")

class english(language):
    def say_hello(self):
        print("Hello: ")

class spanish(language):
    def say_hello(self):
        print("Hola: ")

class chinese(language):
    # def say_hello(self):
        pass

def intro(lang):
    lang.say_hello()

    

tirzah=french()
diana=spanish()
Nina=chinese()

intro(tirzah)
intro(diana)
intro(Nina)

    