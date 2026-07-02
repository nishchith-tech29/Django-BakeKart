# 🎂 Bake Kart

An advanced, feature-rich e-commerce platform dedicated to ordering a wide variety of delicious cakes. Built entirely with Django, this backend system handles everything from complex product variants (cake sizes, flavors) to secure checkout and user management. 

## 🚀 Features

* **Custom User Authentication:** A robust, custom user model utilizing Email addresses for logging in rather than standard usernames.
* **Smart Cart System:** Users can add cakes to their cart as guests. Upon logging in, all guest cart items seamlessly transfer to their permanent user account.
* **Advanced Product Variants:** Customers can easily select specific cake variations like weight (e.g., 500g, 1kg, 2kg) and flavor, with independent tracking in the database.
* **Order Management & Dashboard:** A dedicated user dashboard to track order history, view detailed order receipts, update profiles, and manage passwords.
* **Review & Rating System:** Verified buyers can leave detailed reviews and half-star ratings on cakes they've purchased.
* **Payment Integration:** Secure checkout flow utilizing the PayPal payment gateway.
* **Security Enhancements:** Features a custom, secure admin URL to prevent unauthorized access, alongside a decoy `/admin` route that logs malicious login attempts.
* **Dynamic Pagination:** Smooth, paginated browsing across the entire cake catalog.
* **Product Galleries:** Multiple images for single cake listings for a better user experience.

## 🛠️ Tech Stack

* **Backend Framework:** Django (Python)
* **Database:** SQLite (Development) / PostgreSQL (Production)
* **Frontend:** HTML5, CSS3, JavaScript
* **Payment Gateway:** PayPal API

## ⚙️ Local Setup and Installation

Follow these steps to get your development environment running:

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/nishchith-tech29/Django-BakeKart.git](https://github.com/nishchith-tech29/Django-BakeKart.git)
   cd Django-BakeKart
