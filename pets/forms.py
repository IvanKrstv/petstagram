from django import forms

from pets.models import Pet


class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['name', 'date_of_birth', 'personal_photo']

        labels = {
            'name': 'Pet Name',
            'personal_photo': 'Image',
            'date_of_birth': 'Date Of Birth'
        }

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': "Enter pet's name"}),
            'date_of_birth': forms.DateInput(attrs={'placeholder': "Enter date of birth", 'type': 'date'}),
            'personal_photo': forms.URLInput(attrs={'placeholder': "Enter pet image"})
        }


class PetDeleteForm(PetForm):
    def __int__(self, *args, **kwargs):
        super().__int__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['disabled'] = True
            field.widget.attrs['readonly'] = True
