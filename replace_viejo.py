path = 'C:/Users/almil/Desktop/Prueba1/Cocina/templates/viejo.html'
new = """{% extends 'plantilla.html' %}
{% block titulo %}Datos Viejos{% endblock %}

{% block contenido_principal %}
<div class=\"card shadow-sm\">
    <div class=\"card-header bg-primary text-white\">
        <h5 class=\"mb-0\">Listado de datos antiguos</h5>
    </div>
    <div class=\"card-body p-0\">
        <div class=\"table-responsive\">
            <table class=\"table table-striped table-hover mb-0\">
                <thead class=\"table-dark\">
                    <tr>
                        <th>Nombre</th>
                        <th>Valor</th>
                        <th>Fecha</th>
                    </tr>
                </thead>
                <tbody>
                    {% for dato in dt %}
                    <tr>
                        <td>{{ dato.Nombre }}</td>
                        <td>{{ dato.Valor }}</td>
                        <td>{{ dato.Fecha }}</td>
                    </tr>
                    {% empty %}
                    <tr>
                        <td colspan=\"3\" class=\"text-center text-muted\">No hay datos antiguos</td>
                    </tr>
                    {% endfor %}
                </tbody>
            </table>
        </div>
    </div>
</div>
{% endblock %}
"""
with open(path, 'w', encoding='utf-8') as f:
    f.write(new)
print('done')
