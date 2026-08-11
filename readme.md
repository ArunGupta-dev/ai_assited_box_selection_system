# Box Selection System

Hi! This is a Django-based backend API that solves a classic e-commerce problem: figuring out which shipping box to use for an order. 

It takes a list of cart items (with their 3D dimensions and weight) and calculates the cheapest available box that can fit everything without overlapping. I used the `py3dbp` library to handle the complex 3D spatial math in memory.

## How to Run the Project

1. **Install the requirements:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Set up the database:**
   ```bash
   python manage.py migrate
   ```

3. **Start the local server:**
   ```bash
   python manage.py runserver
   ```

## Adding Boxes (Important!)

Before the API can recommend a box, you need to tell it what boxes exist in the warehouse. You can add and manage box sizes easily using the Django Admin panel.

1. Create your admin account by running:
   ```bash
   python manage.py createsuperuser
   ```
2. Follow the terminal prompts to set a username and password.
3. Go to `http://localhost:8000/admin/` in your browser, log in, and add a few standard boxes to the database.

## How to Test

Once the server is running and you have added some boxes to the admin panel, just open the included `index.html` file in any web browser. 

It has a simple user interface where you can add items to a cart, set their dimensions, and click "Calculate Best Box" to see the API in action!
