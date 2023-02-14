from xml.dom import minidom
doc = minidom.parse("ejemplo.xml")
nombre = doc.getElementsByTagName("nombre")[0]
print(nombre.firstChild.data)
empleados = doc.getElementsByTagName("empleado")
for empleado in empleados:
    sid = empleado.getAttribute("id")
    username = empleado.getElementsByTagName("username")[0]
    password = empleado.getElementsByTagName("password")[0]
    print("id:%s " % sid)
    print("username:%s" % username.firstChild.data)
    print("password:%s" % password.firstChild.data)

'''
https://decodigo.com/python-leer-archivo-xml


Para comenzar el parseo usamos: doc = minidom.parse(«/ruta/datos.xml»).

Es posible encontrar cualquier nodo del documento como lo hacemos en la línea con la función nombre = doc.getElementsByTagName(«nombre»)[0].

Obtener una lista de nodos y sus atributos:  sid = empleado.getAttribute(«id»).

O  bien obtener otros nodos y su respectivo contenido de texto: username = empleado.getElementsByTagName(«username»)[0].

Con Python es bastante sencillo leer archivos de XML.

Más información en inglés: https://geekole.com/read-xml-file-in-python/


'''