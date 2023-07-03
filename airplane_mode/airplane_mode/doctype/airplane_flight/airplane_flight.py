# Copyright (c) 2023, Siva manikanta vemana and contributors
# For license information, please see license.txt

# import frappe
from frappe.website.website_generator import WebsiteGenerator
from frappe.model.document import Document

class AirplaneFlight(WebsiteGenerator):

	def before_submit(self):
		self.status = "Completed"

	
        
	# def get_page_info(self):
	# 	page_info = {
    #         'airplane': self.airplane,
	#     	'duration': self.duration,
	# 	    'date_of_departure':self.date_of_departure,
	# 	    'time_of_departure':self.time_of_departure,
	# 	    'source_airport_code':self.source_airport_code,
	# 	    'destination_airport_code':self.destination_airport_code
    #     }
	# 	return page_info
			
def set_status_completed(doc, method):
	doc.before_submit()
	

