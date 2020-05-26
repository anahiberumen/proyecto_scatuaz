from behave import given, when, then
import time

# 1
@given(u'que ingreso a la vista de "{vista}"')
def step_impl(context, vista):
    context.driver.get(context.url+vista)


@given(u'ingreso el usuario "{usr}" con la contraseña "{pas}"')
def step_impl(context, usr, pas):
    login(context, usr, pas)


@when(u'se realiza un inicio de sesion')
def step_impl(context):
    context.driver.find_element_by_class_name('btn-primary').click()


@then(u'puedo ver un mensaje de "{mensaje}"')
def step_impl(context, mensaje):
    titulo = context.driver.find_element_by_tag_name('h1')
    context.test.assertEqual(titulo.text, mensaje)
    context.driver.get(context.url+'cerrar')

# 2
@then(u'puedo ver un mensaje de error "{error}"')
def step_impl(context, error):
    mensaje = context.driver.find_element_by_class_name('text-danger')
    context.test.assertEqual(mensaje.text, error)
    context.driver.get(context.url+'cerrar')

# 3
@given(u'no ingreso usuario ni contraseña')
def step_impl(context):
    time.sleep(1)

@then(u'me mantengo en la misma vista')
def step_impl(context):
    context.test.assertEqual(
    str(context.driver.current_url), "http://127.0.0.1:8000/")
    context.driver.get(context.url+'cerrar')

# login


def login(context, usr, pas):
    context.driver.get(context.url+'')
    context.driver.find_element_by_id('id_username').send_keys(usr)
    context.driver.find_element_by_id('id_password').send_keys(pas)
