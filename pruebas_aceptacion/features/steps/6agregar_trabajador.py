from behave import given, when, then
import time


@given(u'que soy un usuario logeado')
def step_impl(context):
    context.driver.get(context.url+'cerrar')
    context.driver.get(context.url+'')
    context.driver.find_element_by_id('id_username').send_keys('tigre')
    context.driver.find_element_by_id('id_password').send_keys('tigre123')
    context.driver.find_element_by_class_name('btn-primary').click()


@when(u'escribo los datos "{field_1}": "{field_1_d}", "{field_2}": "{field_2_d}", "{field_3}": "{field_3_d}",')
def step_impl(context, field_1, field_1_d, field_2, field_2_d, field_3, field_3_d):
    context.driver.find_element_by_css_selector(
        "input[type='radio'][value='"+field_1_d+"']").click()
    context.driver.find_element_by_id('id_'+field_2).send_keys(field_2_d)
    context.driver.find_element_by_id('id_'+field_3).send_keys(field_3_d)


@when(u'"{field_1}": "{field_1_d}", "{field_2}": "{field_2_d}", "{field_3}": "{field_3_d}", "{field_4}": "{field_4_d}",')
def step_impl(context, field_1, field_1_d, field_2, field_2_d, field_3, field_3_d, field_4, field_4_d):
    context.driver.find_element_by_id('id_'+field_1).send_keys(field_1_d)
    context.driver.find_element_by_id('id_'+field_2).send_keys(field_2_d)
    context.driver.find_element_by_id('id_'+field_3).send_keys(field_3_d)
    context.driver.find_element_by_id('id_'+field_4).send_keys(field_4_d)


@when(u'"{field_1}": "{field_1_d}", "{field_2}": "{field_2_d}", "{field_3}": "{field_3_d}"')
def step_impl(context, field_1, field_1_d, field_2, field_2_d, field_3, field_3_d):
    context.driver.find_element_by_id('id_'+field_1).send_keys(field_1_d)
    if field_2_d == 1:
        context.driver.find_element_by_id('id_'+field_2).click()
    if field_3_d == 1:
        context.driver.find_element_by_id('id_'+field_3).click()


@when(u'de clic en el botón crear "Agregar"')
def step_impl(context):
    context.driver.find_element_by_class_name('btn-primary').click()


@then(u'podré ver el trabajador con RFC "{rfc}" en la lista de trabajador')
def step_impl(context, rfc):
    rows = context.driver.find_elements_by_tag_name('tr')
    rfcs = [row.find_elements_by_tag_name('td')[3].text for row in rows[1:]]
    context.test.assertIn(rfc, rfcs)


@then(u'seguire en la misma vista')
def step_impl(context):
    context.test.assertEquals(
        str(context.driver.current_url), 'http://127.0.0.1:8000/trabajador/agregar')


@then(u'podre ver el mensaje de error "{error1}", "{error2}", "{error3}", "{error4}"')
def step_impl(context, error1, error2, error3, error4):
    items = context.driver.find_elements_by_class_name('text-danger')
    errors = [item.text for item in items]
    context.test.assertIn(error1, errors)
    context.test.assertIn(error2, errors)
    context.test.assertIn(error3, errors)
    context.test.assertIn(error4, errors)
