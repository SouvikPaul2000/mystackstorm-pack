from st2common.runners.base_action import Action

class HelloWorldAction(Action):
    def run(self):
        return {'message': 'Hello, World!'}
