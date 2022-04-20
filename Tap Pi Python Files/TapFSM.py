from transitions import Machine


class TapFSM:

    states = ['stopped', 'start_pouring', 'pouring', 'stopping']

    def __init__(self, motor):
        self.motor = motor

        self.machine(model = self, states = TapFSM.states, initial = 'stopped')


        self.machine.add_transition(trigger='make_pour', source='stopped', dest='start_pouring',after='start_pouring_beer')
        self.machine.add_transition(trigger='full_pour', source='start_pour', dest='pouring')

        self.machine.add_transition(trigger='stop_pour', source='pouring', dest='stopping', after = 'stop_pouring_beer')
        self.machine.add_transition(trigger='full_stop', source='stopping', dest='stopped')


    def start_pouring_beer(self):
       self.motor.startPour()
       self.full_pour()

    def stop_pouring_beer(self):
        self.motor.stopPour()
        self.full_stop()