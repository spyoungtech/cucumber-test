from behave import *

@given('I have an empty grocery list')
def step_impl(context):
    context.grocery_list = []

@when('I add an item to the list')
def step_impl(context):
    context.grocery_list.append('item')

@then('The grocery list contains a single item')
def step_impl(context):
    assert len(context.grocery_list) == 1


@then('I can access that item from the grocery list')
def step_impl(context):
	assert context.grocery_list[0] == 'item'

@when('I add these items to the list')
def step_impl(context):
	for row in context.table.rows:
		context.grocery_list.append(row[0])

@then('The length of the list is {expected_length}')
def step_impl(context, expected_length):
	print(expected_length)
	print(context.grocery_list)
	assert len(context.grocery_list) == int(expected_length)