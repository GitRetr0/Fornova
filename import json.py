import json

#defining data structure
data = {
    "assignment_results": [
        {
            "deep_link": "https://www.booking.com/searchresults.en-US.html?dest_type=hotel&dest_id=4480704&checkin=2021-2-1;checkout=2021-2-2&selected_currency=USD;",
            "hotel_name": "Home2 Suites By Hilton San Francisco Airport North",
            "hotel_id": "4480704",
            "ext_data": {
                "scan_longitude": -122.3992458,
                "scan_latitude": 37.65710296,
                "scan_occupancy_from_scan": 4,
                "scan_checkin_from_scan": None,
                "scan_checkout_from_scan": None,
                "taxes": '{ "TAX":"14.70", "City tax":"4.01"}'
            },
            "cancellation_policy": "Guests:",
            "number_of_guests": 4,
            "breakfast": "included",
            "shown_price": {
                "King Studio Suite - Hearing Accessible/Non-Smoking": "113.05",
                "King Studio Suite - Non Smoking": "90",
                "King Room - Mobility/Hearing Accessible - Non-Smoking": "115.05",
                "Queen Suite with Two Queen Beds - Non-Smoking": "112.05"
            },
            "currency": "USD",
            "net_price": {
                "King Studio Suite - Hearing Accessible/Non-Smoking": "113.05",
                "King Studio Suite - Non Smoking": "90",
                "King Room - Mobility/Hearing Accessible - Non-Smoking": "115.05",
                "Queen Suite with Two Queen Beds - Non-Smoking": "112.05"
            },
            "availability": "",
            "ci_date": "2021-02-01",
            "co_date": "2021-02-02",
            "los": 1,
            "site_name": "booking",
            "site_type": "ota",
            "shown_currency": "USD",
            "pos": "US",
            "snapshot_url": [
                "https://storage.googleapis.com/prod-public-snapshots.gcphosts.net/booking_hotel/202101/60041b12fef076f02f58a8a5%253A%253A27-968117.png"
            ]
        }
    ]
}

#cheapest room
shown_prices = data["assignment_results"][0]["shown_price"]
cheapest_price = None
cheapest_room = None

#comparing each room's price to find the cheapest one
for room, price in shown_prices.items():
    price_float = float(price)
    if cheapest_price == None or price_float < cheapest_price:
        cheapest_price = price_float
        cheapest_room = room

#determine number of guests
number_of_guests = data["assignment_results"][0]["number_of_guests"]

#cheapest room info
print(f"Cheapest Room: {cheapest_room}, Number of Guests: {number_of_guests}, Price: {cheapest_price}")


#calculate and show total price (net price + taxes) for all rooms
taxes = json.loads(data["assignment_results"][0]["ext_data"]["taxes"])

#convert taxes to floats to sum them and get total
total_tax = sum(float(value) for value in taxes.values())

#net prices fr each room
net_prices = data["assignment_results"][0]["net_price"]

#calculate total price with taxes and print for each room
total_prices = {}
for room, net_price in net_prices.items():
    total_price = float(net_price) + total_tax
    total_prices[room] = total_price

#total pricce fo each room output
for room, price in total_prices.items():
    print(f"Room: {room}, Total Price (Net + Taxes): {price}")