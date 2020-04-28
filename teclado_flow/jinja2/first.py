from jinja2 import Environment, FileSystemLoader

file_loader = FileSystemLoader('C:\\Users\\keys4.000\\Documents\\4git\\python\\teclado_flow\\jinja2\\jinja2_templates')
env = Environment(loader=file_loader)
template_name = 'lamb.txt'
template = env.get_template(template_name)
person = {}
person['name'] = "John"
person['animal'] = 'dog'
# output = template.render(name='Mary', animal='kitty')
output = template.render(data=person)
print(output)