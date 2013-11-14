#--coding: utf8--

from django import forms
from django.contrib.contenttypes.models import ContentType
from attachments.models import Attachment


class AttachmentForm(forms.ModelForm):
    attachment_file = forms.FileField(label='Файл')

    class Meta:
        model = Attachment
        fields = ('attachment_file', 'name')

