from jinja2 import Environment, FileSystemLoader
from monitor import ping

env = Environment(loader=FileSystemLoader("templates"))
template = env.get_template("index.html")


rendered_html = template.render(ping=ping)


with open("index.html", "w") as f:
  f.write(rendered_html)

print(rendered_html)