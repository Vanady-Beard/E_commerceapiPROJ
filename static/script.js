document.getElementById('createAccountForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const data = {
        name: document.getElementById('name').value,
        email: document.getElementById('email').value,
        phone: document.getElementById('phone').value,
        username: document.getElementById('username').value,
        password: document.getElementById('password').value
    };
    fetch('/create_account', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        alert('Account created successfully!');
        document.getElementById('createAccountForm').reset();
    })
    .catch(error => {
        console.error('Error:', error);
        alert('Error creating account: ' + error.message);
    });
});

document.getElementById('addProductForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const data = {
        name: document.getElementById('productName').value,
        price: parseFloat(document.getElementById('productPrice').value)
    };
    fetch('/products', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        alert('Product added successfully!');
        document.getElementById('addProductForm').reset();
    })
    .catch(error => {
        console.error('Error:', error);
        alert('Error adding product: ' + error.message);
    });
});



