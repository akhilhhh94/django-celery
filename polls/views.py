from django.views.generic.edit import FormView
from django.contrib import messages
from polls.forms import FeedbackForm


class FeedbackView(FormView):
    template_name = 'feedback/contact.html'
    form_class = FeedbackForm
    success_url = '/test'

    def form_valid(self, form):
        form.send_email()
        messages.add_message(self.request, messages.INFO, 'Message Send success!!')
        return super(FeedbackView, self).form_valid(form)
