from crispy_forms.bootstrap import FormActions
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, ButtonHolder, Fieldset
from django.forms import Form
from django import forms
from django.forms.models import ModelForm, modelformset_factory
from django.forms.widgets import CheckboxSelectMultiple, DateTimeInput

from ave_cesar.models import Product, Category

class DateRangeField(forms.DateField):
    def to_python(self, value):
        values = value.split(' - ')
        start_date = super().to_python(values[0])
        end_date = super().to_python(values[1])
        return start_date, end_date


class ProductForm(ModelForm):
    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.form_method = 'POST'
    helper.add_input(
            Submit('save_changes', 'Save', css_class="btn-primary")
        )

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name[0].isalpha():
            raise forms.ValidationError('The name %s must begin by a letter' % name)
        return name

    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
                   'given_at': DateTimeInput(attrs={'type': 'datetime-local'})
                   }


class SearchForm(Form):
    range = DateRangeField()
    name = forms.CharField(required=False)
    category = forms.ModelChoiceField(queryset=Category.objects.all(), required=False)
    borrowed = forms.BooleanField(required=False)

    def clean_range(self):
        d = self.cleaned_data.get('range')
        print(d)
        return d

CategoryFormSet = modelformset_factory(Category, fields='__all__')
