from frappe import _

def get_context(context):
    color = frappe.form_dict.get('color', 'black')
    context['color'] = color

    return context

def get_route():
    return [
        {
            'page_name': 'show-me',
            'route': '/show-me',
            'template': '/show_me.html',
            'title': _('Show Me'),
            'hide_sidebar': True
        }
    ]
