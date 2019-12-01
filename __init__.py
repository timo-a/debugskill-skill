from mycroft import MycroftSkill, intent_file_handler


class Debugskill(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('debugskill.intent')
    def handle_debugskill(self, message):
        self.speak_dialog('debugskill')


def create_skill():
    return Debugskill()

