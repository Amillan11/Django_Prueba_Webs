path = 'C:/Users/almil/Desktop/Prueba1/Cocina/templates/plantilla.html'
with open(path, encoding='utf-8', errors='ignore') as f:
    content = f.read()
new = """<!DOCTYPE html>
<html lang=\"es\">
<head>
    <meta charset=\"UTF-8\">
    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">
    <title>{% block titulo %}Prueba1{% endblock %}</title>
    <link href=\"https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css\" rel=\"stylesheet\">
    <style>
        body { background-color: #f8f9fa; min-height: 100vh; }
        .navbar { margin-bottom: 2rem; }
        .content { padding: 1rem; }
    </style>
    {% block extra_css %}{% endblock %}
</head>
<body>
    <nav class=\"navbar navbar-expand-lg navbar-dark bg-dark\">
        <div class=\"container\">
            <a class=\"navbar-brand\" href=\"/\">Prueba1</a>
            <button class=\"navbar-toggler\" type=\"button\" data-bs-toggle=\"collapse\" data-bs-target=\"#navbarNav\">
                <span class=\"navbar-toggler-icon\"></span>
            </button>
            <div class=\"collapse navbar-collapse\" id=\"navbarNav\">
                <ul class=\"navbar-nav\">
                    <li class=\"nav-item\">
                        <a class=\"nav-link\" href=\"{% url 'datos_viejos' %}\">Datos Viejos</a>
                    </li>
                </ul>
            </div>
        </div>
    </nav>

    <div class=\"container content\">
        {% block contenido_principal %}
            <div class=\"alert alert-info\">Bienvenido</div>
        {% endblock %}
    </div>

    <script src=\"https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js\"></script>
    {% block extra_js %}{% endblock %}
</body>
</html>
"""
with open(path, 'w', encoding='utf-8') as f:
    f.write(new)
print('done')
