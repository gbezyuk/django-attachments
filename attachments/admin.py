from attachments.models import Attachment
from attachments.forms import AttachmentForm
from django.contrib.contenttypes import generic


class AttachmentInlines(generic.GenericTabularInline):
    model = Attachment
    form = AttachmentForm
    extra = 1
