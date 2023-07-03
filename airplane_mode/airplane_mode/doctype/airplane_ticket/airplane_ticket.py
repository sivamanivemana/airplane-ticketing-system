# Copyright (c) 2023, Siva manikanta vemana and contributors
# For license information, please see license.txt

import random
import frappe
from frappe.model.document import Document

class AirplaneTicket(Document):
	# def autoname(self):
	# 	row = random.randint(1, 30)
	# 	letter = random.choice(['A','B','C','D','E'])
	# 	if not self.seat:
	# 		seat_number = generate_seat_number(row,letter)
	# 		self.seat = seat_number


	# def before_save(self):
	# 	print(self)
	# def total_amount(self):
	# 	flight_price = self.flight_price
	# 	add_onsp=0
	# 	for item in self.add_ons:
	# 		add_onsp +=add_ons.amount

	# 	if flight_price and add_onsp:
	# 		self.total_amount = flight_price + add_onsp
	# 	else:
	# 		self.total_amount = flight_price
	
	def calculate_total_amount(self):
		flight_price = self.flight_price
		add_ons_total = sum(add_on.amount for add_on in self.add_ons)
		
		if flight_price and add_ons_total:
			self.total_amount = flight_price + add_ons_total
		else:
			self.total_amount = flight_price

	def validate(self):
		self.calculate_total_amount()
			
# def generate_seat_number(row,letter):
# 	row = random.randint(1, 30)
# 	letter = random.choice(['A', 'B', 'C', 'D', 'E', 'F'])
# 	return f"{row}{letter}"

@frappe.whitelist()
def ticket_count(flight):

	capacity=frappe.db.get_value(
		"Airplane", filters={"name": flight[:-14]}, fieldname="capacity")
		
	ticket_list= len(frappe.db.get_list(
		"Airplane Ticket", filters={"flight":flight}))
	
	return [capacity,ticket_list]


