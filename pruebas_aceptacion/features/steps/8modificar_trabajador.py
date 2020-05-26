from behave import given, when, then
import time


@given(u'doy click en el boton de editar del trabajador con rfc "{rfc}')
def step_impl(context, rfc):
    context.rfc = rfc
    rows = context.driver.find_elements_by_tag_name('tr')
    for row in rows[1:]:
        
        if row.find_elements_by_tag_name('a')[3].text == rfc:
            row.find_elements_by_tag_name('td')[4].find_element_by_class_name('btn-primary').click()
            time.sleep(5)


@when(u'escribo los datos "{campo1}": "{dato1}", "{campo2}": "{dato2}", "{campo3}": "{dato3}"')
def step_impl(context, campo1, dato1, campo2, dato2, campo3, dato3):
    context.driver.find_element_by_id('id_'+campo1).clear()
    context.driver.find_element_by_id('id_'+campo1).send_keys(dato1)
    context.driver.find_element_by_id('id_'+campo2).clear()
    context.driver.find_element_by_id('id_'+campo2).send_keys(dato2)
    context.driver.find_element_by_id('id_'+campo3).clear()
    context.driver.find_element_by_id('id_'+campo3).send_keys(dato3)

@when(u'los datos "{campo1}": "{dato1}", "{campo2}": "{dato2}", "{campo3}": "{dato3}", "{campo4}": "{dato4}",')
def step_impl(context, campo1, dato1, campo2, dato2, campo3, dato3, campo4, dato4):
    context.new_data.append(dato1, dato2, dato3, dato4)
    context.driver.find_element_by_id('id_'+campo1).clear()
    context.driver.find_element_by_id('id_'+campo1).send_keys(dato1)
    context.driver.find_element_by_id('id_'+campo2).clear()
    context.driver.find_element_by_id('id_'+campo2).send_keys(dato2)
    context.driver.find_element_by_id('id_'+campo3).clear()
    context.driver.find_element_by_id('id_'+campo3).send_keys(dato3)
    context.driver.find_element_by_id('id_'+campo4).clear()
    context.driver.find_element_by_id('id_'+campo4).send_keys(dato4)

@when(u'de clic en el botón de guardar')
def step_impl(context):
    context.driver.find_element_by_class_name('btn-primary')


@then(u'podre ir a ver detalles del trabajador')
def step_impl(context):
    rows = context.driver.find_elements_by_tag_name('tr')
    for row in rows[1:]:
        
        if row.find_elements_by_tag_name('a')[3].text == context.rfc:
            row.find_elements_by_tag_name('a')[1].click()


@then(u'observar los cambios hechos "{campo1}": "{dato1}", "{campo2}": "{dato2}", "{campo3}": "{dato3}"')
def step_impl(context, campo1, dato1, campo2, dato2, campo3, dato3):
    context.assertEquals(context.driver.find_element_by_id('id_'+campo1).get_attribute("value"), dato1)
    context.assertEquals(context.driver.find_element_by_id('id_'+campo2).get_attribute("value"), dato2)
    context.assertEquals(context.driver.find_element_by_id('id_'+campo3).get_attribute("value"), dato3)
    


@then(u'los nuevo datos "{campo1}": "{dato1}", "{campo2}": "{dato2}", "{campo3}": "{dato3}", "{campo4}": "{dato4}",')
def step_impl(context, campo1, dato1, campo2, dato2, campo3, dato3, campo4, dato4):
    context.assertEquals(context.driver.find_element_by_id('id_'+campo1).get_attribute("value"), dato1)
    context.assertEquals(context.driver.find_element_by_id('id_'+campo2).get_attribute("value"), dato2)
    context.assertEquals(context.driver.find_element_by_id('id_'+campo3).get_attribute("value"), dato3)
    context.assertEquals(context.driver.find_element_by_id('id_'+campo4).get_attribute("value"), dato4)