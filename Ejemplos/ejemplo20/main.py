from junit_xml import  TestCase, TestSuite

caso_prueba = [TestCase('Prueba1', 'some.class.name', 123.345, 'Soy una salida', 'Soy un error')]
ts = TestSuite("Mi caso de prueba", caso_prueba)
print(TestSuite.to_xml_string([ts]))