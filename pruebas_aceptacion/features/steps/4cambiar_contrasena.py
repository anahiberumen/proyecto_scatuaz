from behave import given, when, then
import time


@when(u'de click en el boton de cambiar contraseña')
def step_impl(context):
    context.driver.find_element_by_class_name(
        'card').find_element_by_tag_name('a').click()


@then(u'puedo cerrar sesion')
def step_impl(context):
    context.driver.get(context.url+'cerrar')


@then(u'logearme con la nueva contraseña "{password}" y usuario "{usuario}"')
def step_impl(context, password, usuario):
    context.driver.get(context.url+'')
    context.driver.find_element_by_id('id_username').send_keys(usuario)
    context.driver.find_element_by_id('id_password').send_keys(password)
    context.driver.find_element_by_class_name('btn-primary').click()


@then(u'vere un mensaje de error')
def step_impl(context):
    mensaje = context.driver.find_element_by_class_name('text-danger').text
    context.test.assertEqual(mensaje, "The two password fields didn't match.")


@then(u'podre acceder a lista de trabajadores')
def step_impl(context):
    context.driver.get(context.url+'trabajador')

    title = context.driver.find_element_by_tag_name('h1').text
    context.test.assertEquals(title, 'Lista de Trabajadores')
