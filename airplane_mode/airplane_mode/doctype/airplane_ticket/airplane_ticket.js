// Copyright (c) 2023, Siva manikanta vemana and contributors
// For license information, please see license.txt

frappe.ui.form.on('Airplane Ticket', {
	refresh: function(frm) {
        frm.page.set_primary_action("Submit", function() {
            if (frm.doc.status !== "Boarded") {
                frappe.throw("Cannot submit the Airplane Ticket document. Status must be 'Boarded'.");
                return;
            } else{
                frm.save('Submit');
			}
        });
    },
	refresh: function(frm) {
		frm.add_custom_button('Assign Seat', () => {
			let dialogue = new frappe.ui.Dialog({
				title: 'Assign seat',
				fields: [
					{
						label: 'Seat',
						fieldname: 'seat',
						fieldtype: 'Data'
					}
				],
				size:'small',
				primary_action_label: 'Assign',
				primary_action(values) {
					frm.set_value('seat', values['seat']);
					dialogue.hide();
					frm.save();
				}
			});
	
			dialogue.show();
		},('Action'))
	},

	flight: function(frm) {

		frappe.call({
			method: "airplane_mode.airplane_mode.doctype.airplane_ticket.airplane_ticket.ticket_count",
			args : {
				flight : frm.doc.flight
			},
		})
		.then((r) =>{

			if (frm.doc.name.slice(0, -15) != frm.doc.flight){

				if (r.message[0] === r.message[1]){
					frappe.throw("All seats are booked..!!")
				}
			}
		})
	}
	
	
});
