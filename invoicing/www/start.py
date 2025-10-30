import frappe

def get_context(context):
	context.color = frappe.form_dict.get("color", "blue")
	context.my_message = "Hello, welcome to the invoicing system!"
	context.invoice_count = frappe.db.count("Invoice", {"docstatus": 1})

	current_user = frappe.session.user
	if current_user == "Guest":
		frappe.throw("You must be logged in to access this page.", frappe.PermissionError)
