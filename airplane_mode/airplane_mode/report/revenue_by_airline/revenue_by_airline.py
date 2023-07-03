import frappe

def execute(filters=None):
    columns, data = [
        {
            "label": "Airline",
            "fieldname": "flight",
            "fieldtype": "link",
            "width": 230,
        },
        {
            "label": "Revenue",
            "fieldname": "flight_price",
            "fieldtype": "Currency",
            "width": 300,
        }
    ], []

    flight_rec = frappe.get_all("Airplane Ticket", fields=["flight_price", "flight"])
    airplane_rec = frappe.get_all("Airplane", fields=["name1"])

    matching_records = {}
    total_revenue = 0  # Variable to store the total revenue

    for flight in airplane_rec:
        matching_records[flight["name1"]] = 0

    for flight in flight_rec:
        flight_name = flight["flight"]
        flight_name_without_last_four = flight_name[:-4]

        for airplane in airplane_rec:
            if airplane["name1"] == flight_name_without_last_four:
                matching_records[airplane["name1"]] += flight["flight_price"]
                break

    for name1, flight_price in matching_records.items():
        data.append(frappe._dict({
            "flight": name1,
            "flight_price": flight_price
        }))

        total_revenue += flight_price  
    
    data.append({
        "flight": "Total Revenue",
        "flight_price": total_revenue
    })
    

    chart= {
        "data":{
            "labels" : [d.flight for d in data],
            "datasets" : [
                {
                    "name" : "Revenue By Airline",
                    "values" : [d.flight_price for d in data]
				}
			]
		},
        "type":"pie"
        
	}

    return columns, data,None,chart,None
