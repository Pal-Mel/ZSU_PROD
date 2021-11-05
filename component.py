from crispy_forms.layout import Field

class InputLeftLabel(Field):
    template = 'components/input_field_start_label.html'
    
class InputRightLabel(Field):
    template = 'components/input_field_finish_label.html'