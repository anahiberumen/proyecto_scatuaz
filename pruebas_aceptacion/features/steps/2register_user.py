from behave import given, when, then
import time


@given(u'que soy un administrador logeado')
def step_impl(context):
    if str(context.driver.current_url) == "http://127.0.0.1:8000/":
        iniciar_sesion(context)


@given(u'que el usuario con correo "{correo}" no existe')
def step_impl(context, correo):
    rows = context.driver.find_elements_by_tag_name('tr')
    for row in rows[1:]:

        if row.find_elements_by_tag_name('td')[1].text == correo:
            row.find_elements_by_tag_name(
                'td')[3].find_element_by_class_name('btn-danger').click()
            context.driver.find_element_by_class_name('btn-danger').click()


@when(u'ingreso los datos de "{user_f}": "{user}", "{password_f}": "{password}", "{email_f}": "{email}"')
def step_impl(context, user_f, user, password_f, password, email_f, email):
    context.driver.find_element_by_id('id_'+user_f).send_keys(user)
    context.driver.find_element_by_id('id_'+password_f+'1').send_keys(password)
    context.driver.find_element_by_id('id_'+password_f+'2').send_keys(password)
    context.driver.find_element_by_id('id_'+email_f).send_keys(email)


@when(u'doy click en "Agregar"')
def step_impl(context):
    context.driver.find_element_by_class_name('btn-primary').click()


@then(u'puedo ver "{user}" en la lista de usuarios')
def step_impl(context, user):
    rows = context.driver.find_elements_by_tag_name('tr')
    usuarios = [row.find_elements_by_tag_name(
        'td')[1].text for row in rows[1:]]
    context.test.assertIn(user, usuarios)


@when(u'selecciono la casilla de administrador')
def step_impl(context):
    context.driver.find_element_by_id('id_is_superuser').click()


@then(u'puedo ver que la casilla de "admin" esta checada')
def step_impl(context):
    pass


def iniciar_sesion(context):
    context.driver.get(context.url+'')
    context.driver.find_element_by_id('id_username').send_keys('tigre')
    context.driver.find_element_by_id('id_password').send_keys('tigre123')
    context.driver.find_element_by_class_name('btn-primary').click()
