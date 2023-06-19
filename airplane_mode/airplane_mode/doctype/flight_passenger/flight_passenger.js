// Copyright (c) 2023, Siva manikanta vemana and contributors
// For license information, please see license.txt

frappe.ui.form.on('Flight Passenger', {
	
	last_name: function(frm) {
        // Code to be executed when the last_name field is clicked
        if (frm.doc.first_name && frm.doc.last_name) {
            var full_name = frm.doc.first_name + ' ' + frm.doc.last_name;
            frappe.model.set_value(frm.doctype, frm.docname, 'full_name', full_name);
        } else {
            var full_name = frm.doc.first_name;
            frappe.model.set_value(frm.doctype, frm.docname, 'full_name', full_name);
        }
    }
});

