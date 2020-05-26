from behave import given, when, then
import time


@given(u'doy click en el boton de eliminar del usuario "{email}"')
def step_impl(context, email):
    rows = context.driver.find_elements_by_tag_name('tr')
    for row in rows[1:]:

        if row.find_elements_by_tag_name('td')[1].text == email:
            row.find_elements_by_tag_name(
                'td')[3].find_element_by_class_name('btn-danger').click()


@when(u'me encuentre en la vista de confirmar eliminacion')
def step_impl(context):
    time.sleep(1)


@when(u'doy click en "Eliminar"')
def step_impl(context):
    context.driver.find_element_by_class_name('btn-danger').click()


@then(u'ya no vere "{email}" en la lista de usuarios')
def step_impl(context, email):
    rows = context.driver.find_elements_by_tag_name('tr')
    usuarios = [row.find_elements_by_tag_name(
        'td')[1].text for row in rows[1:]]

    context.test.assertNotIn(email, usuarios)

    context.driver.get(context.url+'cerrar')
    context.driver.get(context.url+'')
    context.driver.find_element_by_id('id_username').send_keys('tigre')
    context.driver.find_element_by_id('id_password').send_keys('tigre123')
    context.driver.find_element_by_class_name('btn-primary').click()


@then(u'puedo ver la advertencia "{mensaje}"')
def step_impl(context, mensaje):
    advertensia = context.driver.find_element_by_tag_name('h3').text
    context.test.assertEquals(advertensia, mensaje)
