from flask import Flask, request, redirect
from contact_handler import init_db, save_contact

app = Flask(__name__)

# Initialize database
init_db()

@app.route('/submit-contact', methods=['POST'])
def submit_contact():
    name = request.form.get('name')
    phone = request.form.get('phone')
    email = request.form.get('email', '')  # Optional field
    message = request.form.get('message')
    
    # Save to database
    save_contact(name, phone, email, message)
    
    # Redirect back to contact page with success message
    return redirect('/contact.html#success')

if __name__ == '__main__':
    app.run(debug=True)