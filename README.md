# 🛒 Django REST Framework E-commerce API

A simple yet fully functional E-commerce backend built using **Django** and **Django REST Framework (DRF)**.
This project demonstrates core backend concepts like product management, cart operations, and order checkout.

---

## 🚀 Features

* 📦 Product CRUD (Create, Read, Update, Delete)
* 🛒 Add to Cart / Remove from Cart
* 📊 Dynamic Cart Total Calculation
* 💳 Checkout System (Order Creation)
* 🔁 Quantity Management in Cart
* 🔐 Environment Variables using `.env`

---

## 🏗 Tech Stack

* **Backend:** Django, Django REST Framework
* **Database:** SQLite (default) / PostgreSQL (optional)
* **Environment Management:** python-dotenv
* **API Testing:** Postman

---

## 📁 Project Structure

```
project/
│
├── .env
├── .gitignore
├── requirements.txt
├── manage.py
│
└── project/
    ├── settings.py
    ├── urls.py
    │
    └── app/
        ├── models.py
        ├── serializers.py
        ├── views.py
        ├── urls.py
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

---

### 2️⃣ Create Virtual Environment

```
python -m venv venv
venv\Scripts\activate      # Windows
```

---

### 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

---

### 4️⃣ Setup Environment Variables

Create a `.env` file in root directory:

```
SECRET_KEY=your_secret_key
DEBUG=True

DB_NAME=db_name
DB_USER=db_user
DB_PASSWORD=db_password
DB_HOST=localhost
DB_PORT=5432
```

---

### 5️⃣ Apply Migrations

```
python manage.py makemigrations
python manage.py migrate
```

---

### 6️⃣ Run Server

```
python manage.py runserver
```

👉 Server will run at:
`http://127.0.0.1:8000/`

---

## 🔗 API Endpoints

### 📦 Product APIs

| Method | Endpoint        | Description        |
| ------ | --------------- | ------------------ |
| GET    | /products/      | Get all products   |
| POST   | /products/      | Create product     |
| GET    | /products/{id}/ | Get single product |
| PUT    | /products/{id}/ | Update product     |
| PATCH  | /products/{id}/ | Partial update     |
| DELETE | /products/{id}/ | Delete product     |

---

### 🛒 Cart APIs

| Method | Endpoint      | Description           |
| ------ | ------------- | --------------------- |
| POST   | /cart/add/    | Add item to cart      |
| POST   | /cart/remove/ | Remove item from cart |
| GET    | /cart/{id}/   | View cart details     |

---

### 💳 Checkout API

| Method | Endpoint   | Description  |
| ------ | ---------- | ------------ |
| POST   | /checkout/ | Create order |

---

## 📌 API Request Examples

### ➕ Add to Cart

```
POST /cart/add/
```

```
{
  "product_id": 1,
  "quantity": 2
}
```

---

### ➖ Remove from Cart

```
POST /cart/remove/
```

```
{
  "cart_id": 1,
  "product_id": 1
}
```

---

### 💳 Checkout

```
POST /checkout/
```

```
{
  "cart_id": 1
}
```

---

## 🧠 Key Concepts Used

* **APIView (DRF)** for custom logic handling
* **Serializers** for data validation and transformation
* **SerializerMethodField** for dynamic calculations
* **ForeignKey Relationships** for database design
* **get_or_create()** for efficient cart handling

---

## 🔐 Environment Variables

Sensitive data like `SECRET_KEY` and database credentials are stored in `.env` file and are ignored using `.gitignore`.

---

## 🚀 Future Improvements

* 🔑 JWT Authentication (User login system)
* 👤 User-based Cart
* 💰 Payment Gateway Integration (Stripe/Razorpay)
* 📦 Stock Validation
* 📊 Order History
* 🚀 Deployment (AWS / Render / Railway)

---

## 👨‍💻 Author

**Karan**
Full Stack Web Developer (Python)

---

## ⭐ Acknowledgement

This project is built for learning and demonstrating backend development skills using Django REST Framework.

---

## 📜 License

This project is open-source and available for learning purposes.
