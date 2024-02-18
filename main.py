from flask import Flask, render_template, request


my_fast_food_ordering_web_app = Flask(__name__)

# Dummy menu data

menu = {
	"Pizza": 10,
	"Burger": 8,
	"Salad": 6,
	"Fries": 4
} 

@my_fast_food_ordering_web_app.route("/")
def home():
	return render_template("index.html")
	
@my_fast_food_ordering_web_app.route("/menu")
def display_menu():
	return render_template("menu.html", menu=menu)
	
@my_fast_food_ordering_web_app.route("/order", methods=['POST'])
def order():
	selected_items = request.form.getlist('item')
	total_cost = sum(menu[item] for item in selected_items)
	return f"Your total cost is ${total_cost}"

if __name__=="__main__":
    my_fast_food_ordering_web_app.run(debug=True)