# Copyright (c) 2023, Siva manikanta vemana and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class FlightPassenger(Document):

    # def full_name(self):
    #     if self.first_name and self.last_name:
    #         self.full_name = f"{self.first_name} {self.last_name}"
    #     else:
    #         self.full_name = self.first_name
    #     self.save()

	def validate(self):
    
            if self.first_name and self.last_name:
                full_name = self.first_name + ' ' + self.last_name
                self.full_name = full_name

            else:
                 full_name=self.first_name
                 self.full_name=full_name
                

    # def before_save(self):
    #     if self.first_name and self.last_name:
    #         self.full_name = self.first_name + ' ' + self.last_name
    #     else:
    #         self.full_name = ''

    # def validate(self):
    #     if not self.full_name:
    #         frappe.throw('Full Name is required for Flight Passenger.')