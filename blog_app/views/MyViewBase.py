from time import time

from django.http import HttpResponse
from django.template.loader import render_to_string
from django.views.generic import TemplateView

import blog_app.middleware


class MyViewBase(TemplateView):

    def render_to_response(self, context, **response_kwargs):
        content = render_to_string(self.template_name, context, self.request)
        if hasattr(self.request, blog_app.middleware.NOMBRE_LISTA):
            t = self.request.tiempos[0]
            t1 = t[blog_app.middleware.NOMBRE_TIEMPO]
            content = content.replace('[tiempo]', 'rendering: %s ms' % (time() - t1))
        response = HttpResponse(content)
        return response
