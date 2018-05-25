from behave import *
import operator
from django.db.models import Q
import os

from django.db.models.fields.files import ImageFieldFile

from WebProject.settings import BASE_DIR

use_step_matcher("parse")


@given('Exists dog at refuge "{refuge_name}"')
def step_impl(context, refuge_name):
    from django.contrib.auth.models import User
    from dogapp.models import Refuge
    refuge = Refuge.objects.get(name=refuge_name)
    from dogapp.models import Dog
    for row in context.table:
        dog = Dog(refuge=refuge)
        for heading in row.headings:
            setattr(dog, heading, row[heading])
        dog.save()


@when('I register dog at refuge "{refuge_name}"')
def step_impl(context, refuge_name):
    from dogapp.models import Refuge
    refuge = Refuge.objects.get(name=refuge_name)
    for row in context.table:
        context.browser.visit(context.get_url('dogapp:dog_create', refuge.pk))
        if context.browser.url == context.get_url('dogapp:dog_create', refuge.pk):
            form = context.browser.find_by_tag('form').first
            for heading in row.headings:
                context.browser.fill(heading, row[heading])
            form.find_by_value('Submit').first.click()


@then('I\'m viewing the details page for dog at refuge "{refuge_name}" created by "{username}"')
def step_impl(context, refuge_name, username):
    q_list = [Q((attribute, context.table.rows[0][attribute])) for attribute in context.table.headings]
    from django.contrib.auth.models import User
    q_list.append(Q(('user', User.objects.get(username = username))))
    from dogapp.models import Refuge
    q_list.append(Q(('refuge', Refuge.objects.get(name=refuge_name))))
    from dogapp.models import Dog
    dog = Dog.objects.filter(reduce(operator.and_, q_list)).get()
    assert context.browser.url == context.get_url(dog)


@then('There are {count:n} dogs')
def step_impl(context, count):
    from dogapp.models import Dog
    assert count == Dog.objects.count()


@when('I edit the dog {dog_name} of the refuge "{refuge_name}"')
def step_impl(context, dog_name, refuge_name):
    from dogapp.models import Refuge
    refuge = Refuge.objects.get(name=refuge_name)
    from dogapp.models import Dog
    dog = Dog.objects.get(name=dog_name)
    context.browser.visit(context.get_url('dogapp:dog_edit', refuge.pk, dog.pk))
    if context.browser.url == context.get_url('dogapp:dog_edit', refuge.pk, dog.pk) \
            and context.browser.find_by_tag('form'):
        form = context.browser.find_by_tag('form').first
        for heading in context.table.headings:
            context.browser.fill(heading, context.table[0][heading])
        form.find_by_value('Submit').first.click()


@when('I delete the current dog')
def step_impl(context):
    context.browser.find_link_by_text('delete').click()
    # TODO: Test also using direct edit view link
    # context.browser.visit(context.get_url('myrestaurants:dish_edit', dish.pk))
    form = context.browser.find_by_tag('form').first
    form.find_by_value('Delete').first.click()
