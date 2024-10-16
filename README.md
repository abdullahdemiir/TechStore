
# TechStore - E-Commerce Web Application

## Overview

**TechStore** is an e-commerce web application focused on selling a variety of technological and educational products, with a strong emphasis on remote-controlled (RC) vehicles and hobbyist electronics. The application includes a dynamic Academy section where users can explore tutorials and information on building these projects.

This application is built using Flask and integrates modern HTML, CSS, and JavaScript for a responsive, interactive, and visually appealing user interface.

## Features

- **Product Categories**: Browse products by categories (Cars, Aircrafts, Boats, Educational Vehicles).
- **Shopping Cart**: Add products to the cart, adjust quantities, and proceed to checkout.
- **Academy**: Explore detailed tutorials on building RC vehicles, drones, and other educational vehicles.
- **Contact Form**: Users can send inquiries, complaints, or product returns.
- **Responsive Design**: The website adjusts seamlessly for mobile, tablet, and desktop views.
- **Dynamic Content**: Includes image slideshows, tabbed product categories, and interactive forms.

## Technologies Used

- **Flask**: Python web framework for handling routing and server-side logic.
- **HTML5/CSS3**: For structuring and styling the web pages.
- **JavaScript**: Adds interactive features like slideshows and dynamic tabs.
- **Jinja2**: Templating engine used with Flask for dynamic content rendering.
- **Bootstrap**: (Optional) For responsive design and layout.
  
## Installation and Setup

To set up and run this project locally, follow these steps:

### 1. Clone the repository

```bash
git clone https://github.com/abdullahdemiir/techstore.git
cd techstore
```

### 2. Set up a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scriptsctivate  # On Windows
```

### 3. Install the dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
flask run
```

## Project Structure

```php
.
├── app.py                     # Main Flask application file
├── static                     # Static assets (CSS, JS, images)
│   ├── css
│   │   └── style.css          # Custom CSS styling
│   ├── js
│   │   └── script.js          # JavaScript functionality
│   └── images                 # Product and academy images
├── templates                  # HTML templates for the web pages
│   ├── base.html              # Base template for all pages
│   ├── home.html              # Home page template
│   ├── products.html          # Product listing page
│   ├── cart.html              # Shopping cart page
│   ├── checkout.html          # Checkout page
│   ├── order_confirmation.html # Order confirmation page
│   ├── contact.html           # Contact page
│   ├── about.html             # About us page
│   ├── academy.html           # Academy section home page
│   ├── academy_aircrafts.html # Aircraft projects page in Academy
│   ├── academy_cars.html      # Cars projects page in Academy
│   ├── academy_boats.html     # Boats projects page in Academy
│   ├── academy_educational_vehicles.html # Educational vehicles page in Academy
├── requirements.txt           # Python dependencies
├── README.md                  # Project documentation
└── .gitignore                 # Git ignore file
```

## Key Pages and Routes

| Page        | Description                                    | Route                  |
|-------------|------------------------------------------------|------------------------|
| Home        | Main landing page with a slideshow             | `/`                    |
| Products    | Browse products by category                    | `/products`            |
| Cart        | View and manage the shopping cart              | `/cart`                |
| Checkout    | Complete the purchase process                  | `/checkout`            |
| Contact     | Submit inquiries, complaints, or product returns| `/contact`             |
| About       | Learn more about TechStore's mission and vision | `/about`               |
| Academy     | Explore educational content on building RC products | `/academy`         |
| Aircrafts   | Aircraft projects in the Academy               | `/academy/aircrafts`   |
| Cars        | Car projects in the Academy                    | `/academy/cars`        |
| Boats       | Boat projects in the Academy                   | `/academy/boats`       |
| Educational Vehicles | Educational vehicle projects in the Academy | `/academy/educational_vehicles` |

## JavaScript Features

- **Slideshow**: The homepage features a dynamic slideshow that cycles through featured images.
- **Tabbed Navigation**: The products page allows users to switch between different product categories dynamically without reloading the page.
- **Form Validation**: The contact and checkout forms include client-side validation for better user experience.

## Deployment

To deploy the application, you can use **Render.com** or another hosting platform such as **Heroku** or **AWS**.

### Hosting on Render.com

1. Create an account on [Render.com](https://render.com/).
2. Connect your GitHub repository containing the project.
3. Set up a new web service and link your project.
4. Configure the environment for Python (Flask).
5. Deploy and test your application via the provided Render URL.
