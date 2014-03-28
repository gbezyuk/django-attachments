#--coding: utf8--

from django import forms
from attachments.models import Attachment


class AttachmentForm(forms.ModelForm):
    attachment_file = forms.FileField(label='Attachment')

    class Meta:
        model = Attachment
        fields = ('attachment_file', 'name')
