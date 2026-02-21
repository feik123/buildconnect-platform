from django import template

register = template.Library()

@register.filter
def status_badge(status):
    if status == 'accepted':
        return '🟢 Accepted'
    elif status == 'rejected':
        return '🔴 Rejected'
    elif status == 'pending':
        return '🟡 Pending'
    return status