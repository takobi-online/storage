# -*- coding: utf-8 -*-
# Copyright 2017 Akretion (http://www.akretion.com).
# @author Sébastien BEAU <sebastien.beau@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).


from openerp import api, fields, models
import logging

_logger = logging.getLogger(__name__)

class StorageImage(models.Model):
    _name = 'storage.image'
    _description = 'Storage Image'
    _inherits = {'storage.file': 'file_id'}

    #owner_id = fields.Integer(
    #    "Owner",
    #    required=True)
    #owner_model = fields.Char(
    #    required=True)
    #file_ids = fields.One2many(
    #    'storage.file',
    #    'owner_id',
    #    'File',
    #    domain=lambda self: [("owner_model", "=", self._name)])
    alt_name = fields.Char(string="Alt Image name")
    # display_name = ?
    # exifs ? auteur, date de crétation, upload, gps, mots clefs, features ?
    #
    exifs = fields.Char()


    #@api.model
    #def _get_storage(self):
    #    return NotImplemented
#
    #def _compute_image(self):
    #    # TODO read image
    #    pass
#
    #def _inverse_image(self):
    #    # TODO store image
    #    pass
#
    #def _compute_url(self):
    #    aktest = ('http://www.akretion.com/sites/'
    #         '50443990c3c67e1bf3000004/theme/images/logo.png')
    #    for record in self:
    #        record.image_url = aktest
    #        record.image_medium_url = aktest
    #        record.image_small_url = aktest
    #    #for field in self._fields:
    #    #    if isinstance(field, fields.Char) and hasattr(field, 'size'):
    #    #        image_fields.append((field_name, field.size))
    #    #for record in self:
    #    #    for field, size in image_fields:
    #    #        record[field] = record.resize(size).url
#
    #def resize(self, size):
    #    self.ensure_one()
    #    return search_or_create_public_file()
#
    def _compute_url(self):
        _logger.info('compute_url de l\'enfant')
        return self.file_id.backend_id.get_public_url(self)
