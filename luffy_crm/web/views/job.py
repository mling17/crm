from django.utils.safestring import mark_safe
from django.urls import reverse
from django.conf.urls import url
from stark.service.v1 import StarkHandler, get_datetime_text, get_m2m_text, StarkModelForm, Option
from stark.forms.widgets import DateTimePickerInput
from web import models
from .base import PermissionHandler


class JobListModelForm(StarkModelForm):
    class Meta:
        model = models.JobRecord
        fields = ['job', ]


class JobListHandler(PermissionHandler, StarkHandler):
    def display_correcting(self, obj=None, is_header=None, *args, **kwargs):
        if is_header:
            return '批改作业'
        remark_url = reverse('stark:web_remarkjobs_add')
        return mark_safe('<a target="_blank" href="%s">批改作业</a>' % remark_url)

    list_display = ['job', get_datetime_text('交作业时间', 'date'), display_correcting]
    model_form_class = JobListModelForm

    def save(self, request, form, is_update, *args, **kwargs):
        if not is_update:
            current_user_id = request.session['user_info']['id']
            form.instance.student_id = current_user_id
        form.save()
