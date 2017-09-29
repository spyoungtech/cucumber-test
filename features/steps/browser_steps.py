
@given(u'I am on the Cucumber.js GitHub repository')
def step_impl(context):
    context.driver.get('https://github.com/cucumber/cucumber-js/tree/master')

@when(u'I click on "{s}"')
def step_impl(context, s):
	elem = context.driver.find_element_by_link_text(s)
	elem.click()

@then(u'I should see "{text}"')
def step_impl(context, text):
	xpath = "//*[contains(text(),'" + text + "')]"
	return context.driver.find_element_by_xpath(xpath)