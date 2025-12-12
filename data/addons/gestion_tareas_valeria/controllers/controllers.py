from odoo import http


class GestionTareasValeria(http.Controller):
     @http.route('/gestion_tareas_valeria/gestion_tareas_valeria', auth='public')
     def index(self, **kw):
         return "Hello, world"

     @http.route('/gestion_tareas_valeria/gestion_tareas_valeria/objects', auth='public')
     def list(self, **kw):
         return http.request.render('gestion_tareas_valeria.listing', {
             'root': '/gestion_tareas_valeria/gestion_tareas_valeria',
             'objects': http.request.env['gestion_tareas_valeria.gestion_tareas_valeria'].search([]),
         })

     @http.route('/gestion_tareas_valeria/gestion_tareas_valeria/objects/<model("gestion_tareas_valeria.gestion_tareas_valeria"):obj>', auth='public')
     def object(self, obj, **kw):
         return http.request.render('gestion_tareas_valeria.object', {
             'object': obj
         })

