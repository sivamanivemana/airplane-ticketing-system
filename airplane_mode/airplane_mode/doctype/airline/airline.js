// Copyright (c) 2023, Siva manikanta vemana and contributors
// For license information, please see license.txt

frappe.ui.form.on('Airline', {
	refresh: function(frm) {
		console.log(frm.doc.website)
		if (frm.doc.website){
			cur_frm.add_web_link(frm.doc.website, "Visit Website")

		}else{
			
		}
	}
});
