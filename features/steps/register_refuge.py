from behave import *
import operator
from django.db.models import Q
from django.urls.base import reverse

use_step_matcher("parse")


@given('Exists refuge registered by "{user}"')
def step_impl(context, username):
    from django.contrib.auth.models import User
    user = User.objects.get(username=username)
    from dogapp.models import Refuge
    for row in context.table:
        refuge = Refuge(user=user)
        for heading in row.headings:
            setattr(refuge, heading, row[heading])
            refuge.save()


@when('I register refuge')
def step_impl(context):
    for row in context.table:
        context.browser.visit(context.get_url('dogapp:refuge_create'))
        if context.browser.url == context.get_url('dogapp:refuge_create'):
            form = context.browser.find_by_tag('form').first
            for heading in row.headings:
                context.browser.fill(heading, row[heading])
            form.find_by_css('button.btn-success').first.click()


@then('There are {count:n} refuges')
def step_impl(context, count):
    from dogapp.models import Refuge
    assert count == Refuge.objects.count()


@then('I\'m viewing the details page for refuge by "{username}"')
def step_impl(context, username):
    q_list = [Q((attribute, context.table.rows[0][attribute])) for attribute in context.table.headings]
    from django.contrib.auth.models import User
    q_list.append(Q(('user', User.objects.get(username=username))))
    from dogapp.models import Refuge
    restaurant = Refuge.objects.filter(reduce(operator.and_, q_list)).get()
    assert context.browser.url == context.get_url(restaurant)


@when('I edit the refuge with name "{name}"')
def step_impl(context, name):
    from dogapp.models import Refuge
    refuge = Refuge.objects.get(name=name)
    context.browser.visit(context.get_url('dogapp:refuge_edit', refuge.pk))
    if context.browser.url == context.get_url('dogapp:refuge_edit', refuge.pk) \
            and context.browser.find_by_tag('form'):
        form = context.browser.find_by_tag('form').first
        for heading in context.table.headings:
            context.browser.fill(heading, context.table[0][heading])
        context.browser.find_by_css('button.btn-success').first.click()
