from django import forms
from django.db.models import TextField


from repont.models import Statement, Repont


class StatementForm(forms.ModelForm):
    description = forms.CharField(required=False,widget=forms.Textarea(attrs={
        "rows":3,
        "placeholder":"Teli van, vagy egyáltalán nem működik, vagy csak nem mindegyik berendezés működik..."
    }))
    class Meta:
        model = Statement
        fields = ["description"]

    def __init__(self, *args, **kwargs):
        super(StatementForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'text-input w-100 form-control bg-dark text-light'
        self.fields['description'].label = "Megjegyzés"



class RepontForm(forms.ModelForm):
    description = forms.CharField(required=False, widget=forms.Textarea(attrs={
        "rows": 3,
        "placeholder": "Az üzlettel / repont automatával kapcsolatos megjegyzés. Elhelyezkedés, nyitvatartás stb..."
    }))
    class Meta:
        model = Repont
        fields = ["name","description"]

    def __init__(self, *args, **kwargs):
        super(RepontForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'text-input w-100 form-control bg-dark text-light'
        self.fields['description'].label = "Megjegyzés"
        self.fields['name'].label = "Üzlet neve"
