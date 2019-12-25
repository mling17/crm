from django.utils.safestring import mark_safe
from django.urls import reverse
from django.conf.urls import url
from stark.service.v1 import StarkHandler, get_datetime_text, get_m2m_text, StarkModelForm, Option
from stark.forms.widgets import DateTimePickerInput
from web import models
from .base import PermissionHandler


class RemarkJobModelForm(StarkModelForm):
    class Meta:
        model = models.RemarkJobs
        fields = '__all__'


class RemarkJobHandler(PermissionHandler, StarkHandler):
    list_display = ['remark_text', ]
    model_form_class = RemarkJobModelForm

    def save(self, request, form, is_update, *args, **kwargs):
        if not is_update:
            current_user_id = request.session['user_info']['id']
            form.instance.job_record_id = current_user_id
        form.save()
