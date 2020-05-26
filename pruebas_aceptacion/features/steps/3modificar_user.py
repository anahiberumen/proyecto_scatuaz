from behave import given, when, then
import time


@given(u'doy click en el boton de editar del usuario "{email}"')
def step_impl(context, email):
    rows = context.driver.find_elements_by_tag_name('tr')
    for row in rows[1:]:

        if row.find_elements_by_tag_name('td')[1].text == email:
            context.urlmod = row.find_elements_by_tag_name(
                'td')[3].find_element_by_class_name('btn-primary').get_attribute('href')
            row.find_elements_by_tag_name(
                'td')[3].find_element_by_class_name('btn-primary').click()


@when(u'me encuentre en la vista de modificar usuario')
def step_impl(context):
    titulo = context.driver.find_element_by_tag_name('h1').text

    context.test.assertEquals(titulo, 'Modificar Usuario')


@when(u'edito los campos de "{user_f}": "{user}", "{email_f}": "{email}"')
def step_impl(context, user_f, user, email_f, email):
    context.driver.find_element_by_id('id_'+user_f).clear()
    context.driver.find_element_by_id('id_'+user_f).send_keys(user)
    context.driver.find_element_by_id('id_'+email_f).clear()
    context.driver.find_element_by_id('id_'+email_f).send_keys(email)


@when(u'doy click en el boton de Guardar')
def step_impl(context):
    context.driver.find_element_by_class_name('btn-primary').click()


@then(u'vere "{email}" y "{username}" en la lista de usuarios')
def step_impl(context, email, username):
    rows = context.driver.find_elements_by_tag_name('tr')
    user = False
    ema = False
    for row in rows[1:]:

        print(row.find_elements_by_tag_name('td')[1].text)
        print(row.find_elements_by_tag_name('td')[0].text)
        if row.find_elements_by_tag_name('td')[1].text == email:
            ema = True

        if row.find_elements_by_tag_name('td')[0].text == username:
            user = True

    context.test.assertTrue(user)
    context.test.assertTrue(ema)


@then(u'me mantendre en la vista de modificar usuario')
def step_impl(context):
    context.test.assertEqual(str(context.driver.current_url), context.urlmod)
