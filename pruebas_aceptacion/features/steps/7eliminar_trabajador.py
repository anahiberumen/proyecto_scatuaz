from behave import given, when, then
import time


@when(u'encuentre el trabajador con rfc "{rfc}"')
def step_impl(context, rfc):
    rows = context.driver.find_elements_by_tag_name('tr')
    for row in rows[1:]:
        
        if row.find_elements_by_tag_name('a')[3].text == rfc:
            context.row = row



@when(u'de click en el boton de eliminar')
def step_impl(context):
    context.row.find_elements_by_tag_name('td')[4].find_element_by_class_name('btn-danger').click()


@when(u'confirme la eliminacion')
def step_impl(context):
    context.driver.find_element_by_class_name('btn-danger').click()


@then(u'Ya no vere el trabajador con rfc "{rfc}"')
def step_impl(context, rfc):
    rows = context.driver.find_elements_by_tag_name('tr')
    rfcs = [row.find_elements_by_tag_name('td')[3].text for row in rows[1:]]
    context.test.assertNotIn(rfc, rfcs)