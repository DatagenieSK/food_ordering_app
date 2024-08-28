### SK Alauddin Food App

This project is a simple Python-based food ordering system. The application allows users to place orders and manage menu items. Both users and administrators have distinct roles with specific functionalities.

---

### How the Project Works

1. **User Mode**:
   - **Browse Menu**: Users can view available food items along with their prices.
   - **Place Order**: Users can select items from the menu and specify the quantity.
   - **Receipt Generation**: A receipt is generated with the total price.
   - **Save Order**: Orders are saved to a JSON file (`all_orders.json`).

2. **Admin Mode**:
   - **Add Food Item**: Add new items to the menu.
   - **Remove Food Item**: Remove items from the menu.
   - **View Menu**: Check available items and prices.

3. **Persistence**:
   - Orders are stored in a JSON file, allowing them to persist across sessions.

---

### How to Run the Project

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/DatagenieSK/food_ordering_app
   ```

2. **Run the Script**:
   ```bash
   python food_app.py
   ```

3. **Interact with the Application**:
   - Follow on-screen prompts to manage the menu or place orders.

---

### Project Files

- **`food_app.py`**: The main script containing the code.
- **`all_orders.json`**: File where user orders are saved.

---

### Customization

- Customize the initial menu by modifying the `menu` dictionary in the script.
- Additional features can be implemented to extend the project.

---

For more details and to access the code, visit the repository: [SK Alauddin Food App on GitHub](https://github.com/DatagenieSK/food_ordering_app).
