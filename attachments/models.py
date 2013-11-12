# coding=utf-8
from datetime import datetime
import os
from django.db import models
from django.conf import settings 
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model

# From https://github.com/etianen/django-reversion/pull/206/files
UserModel = getattr(settings, 'AUTH_USER_MODEL', 'auth.User') 

class AttachmentManager(models.Manager):
    def attachments_for_object(self, obj):
        object_type = ContentType.objects.get_for_model(obj)
        return self.filter(content_type__pk=object_type.id,
                           object_id=obj.id)

class Attachment(models.Model):
    def attachment_upload(instance, filename):
        """Stores the attachment in a "per module/appname/primary key" folder"""
        return 'attachments/%s/%s/%s' % (
            '%s_%s' % (instance.content_object._meta.app_label,
                       instance.content_object._meta.object_name.lower()),
                       instance.content_object.pk,
                       filename)

    objects = AttachmentManager()

    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')
    creator = models.ForeignKey(get_user_model(), related_name="created_attachments", verbose_name=_('creator'))
    name = models.CharField(verbose_name=_(u'имя'), null=True, blank=True, max_length=1024)
    showing = models.BooleanField(verbose_name=_(u'показывать клиенту'), default=True)
    attachment_file = models.FileField(_(u'файл'), upload_to=attachment_upload)
    created = models.DateTimeField(_('created'), auto_now_add=True)
    modified = models.DateTimeField(_('modified'), auto_now=True)

    class Meta:
        ordering = ['-created']
        permissions = (
            ('delete_foreign_attachments', 'Can delete foreign attachments'),
        )

    # def __unicode__(self):
        # return '%s attached %s' % (self.creator.get_username(), self.attachment_file.name)

    @property
    def filename(self):
        return os.path.split(self.attachment_file.name)[1]

    class Meta:
        verbose_name = _(u'приложение')
        verbose_name_plural = _(u'приложения')
