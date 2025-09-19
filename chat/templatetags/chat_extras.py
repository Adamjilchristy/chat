from django import template

register = template.Library()


@register.filter
def display_name(conversation, current_user):
    """Return a conversation display name for the given user.
    Usage in templates: {{ conversation|display_name:user }}
    """
    try:
        return conversation.get_display_name(current_user)
    except Exception:
        return ""
