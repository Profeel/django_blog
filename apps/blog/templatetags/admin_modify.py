from django.contrib.admin.templatetags.admin_modify import *
from django.contrib.admin.templatetags.admin_modify import submit_row as original_submit_row
# or 
# original_submit_row = submit_row

@register.inclusion_tag('admin/blog/submit_line.html', takes_context=True)
def submit_row(context):
    print 'xxxctxxxxxxxxxxxxx'
    ctx = original_submit_row(context)
    ctx.update({
        'show_save_and_add_another': context.get('show_save_and_add_another', ctx['show_save_and_add_another']),
        'show_save_and_continue': context.get('show_save_and_continue', ctx['show_save_and_continue']),
        'xxxx':'bbb',
        })                                                                  
    print ctx
    return ctx 

