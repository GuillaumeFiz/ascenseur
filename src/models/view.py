

class View:

    def __init__(self, lift):
        self.number_char_of_part = 35
        self.lift = lift

    def render(self, tick):
        statements = [f'Tick : {tick}\n\n']
        for stage in reversed(range(1, self.lift.nbr_of_stage + 1)):
            statements.append(self.get_one_stage(stage))
        statements.append('\n\nCTRL + C pour couper')
        return statements

    def get_one_stage(s, stage):
        render = []
        if stage == s.lift.actual_stage:
            render.append(s.get_lift_line())
        else:
            render.append(s.get_empty_line())
        render.append(s.get_stage_line(stage))
        render.append(s.get_peoples_line(stage))
        return ' '.join(render)

    def get_lift_line(s):
        render = ''
        if s.lift.pause:
            render += '<'
        elif s.lift.to_bottom:
            render += '↓'
        else:
            render += '↑'
        render += ' ' + ' '.join(list(s.lift.on_the_move.keys()))
        render += ' ' * (s.number_char_of_part - len(render) - 1)
        if s.lift.pause:
            render += '>'
        elif s.lift.to_bottom:
            render += '↓'
        else:
            render += '↑'
        return render

    def get_empty_line(self):
        return ' ' * self.number_char_of_part

    def get_peoples_line(s, stage):
        render = ''
        for people in s.lift.waiting.values():
            if stage != people.start:
                continue
            render += f' {people.id}%s'
            if people.want_to_go_down():
                render = render % ('↓')
            else:
                render = render % ('↑')
        for people in s.lift.arrived.values():
            if stage != people.arrival:
                continue
            render += f' {people.id}'
        return render + ' ' * (s.number_char_of_part - len(render))

    def get_stage_line(self, stage):
        return f'| {stage} |'
