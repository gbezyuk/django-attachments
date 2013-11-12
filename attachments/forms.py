#--coding: utf8--

from django import forms
from django.contrib.contenttypes.models import ContentType
from attachments.models import Attachment


class AttachmentForm(forms.ModelForm):
    attachment_file = forms.FileField(label='Файл')

    class Meta:
        model = Attachment
        fields = ('attachment_file', 'name')

    def save(self, request, obj, *args, **kwargs):
        self.instance.creator = request.user
        self.instance.content_type = ContentType.objects.get_for_model(obj)
        self.instance.object_id = obj.id
        super(AttachmentForm, self).save(*args, **kwargs)
