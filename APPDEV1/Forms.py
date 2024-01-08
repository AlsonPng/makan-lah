from wtforms import Form, RadioField, validators


class GameForm(Form):
    Q1 = RadioField("If we produce food that doesn't get eaten, what else is wasted?", choices=[('W', 'Wildlife Habitat')('W', 'Water'), ('E', 'Energy'), ('A', 'All of the above')], default='A')

