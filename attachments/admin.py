from attachments.models import Attachment
from django.contrib.contenttypes import generic


class AttachmentInlines(generic.GenericStackedInline):
    exclude = ('creator',)
    model = Attachment
    extra = 1