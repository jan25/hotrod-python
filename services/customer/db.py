from .client import Customer

customers = {
    "123": Customer(id="123", name="Rachel's Floral Designs", location="115,277"),
    "567": Customer(id="567", name="Amazing Coffee Roasters", location="211,653"),
    "392": Customer(id="392", name="Trom Chocolatier", location="577,322"),
    "731": Customer(id="731", name="Japanese Deserts", location="728,326")
}

def get_customer_by_id(customer_id):
    if customer_id not in customers: return
    return customers[customer_id]
