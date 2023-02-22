# const express = require('express');
# const bodyParser = require('body-parser');
# const sqlite3 = require('sqlite3').verbose();
# const app = express();

# app.use(bodyParser.json());

# // Connect to the SQLite database
# const db = new sqlite3.Database(':memory:');

# // Create the login table in the database
# db.run(`CREATE TABLE login (
#     id INTEGER PRIMARY KEY,
#     name TEXT NOT NULL,
#     age INTEGER NOT NULL,
#     pin INTEGER NOT NULL
# )`);

# // Endpoint to create a new login
# app.post('/login', (req, res) => {
#     const { name, age, pin } = req.body;

#     // Validate input
#     if (!name || !age || !pin) {
#         return res.status(400).send({ error: 'Name, age, and pin are required' });
#     }

#     // Insert login into the database
#     db.run(`INSERT INTO login (name, age, pin) VALUES (?, ?, ?)`, [name, age, pin], function(err) {
#         if (err) {
#             return res.status(500).send({ error: err.message });
#         }
#         res.send({ id: this.lastID });
#     });
# });

# // Endpoint to retrieve login information
# app.get('/login/:id', (req, res) => {
#     const { id } = req.params;

#     // Retrieve login from the database
#     db.get(`SELECT name, age, pin FROM login WHERE id = ?`, [id], (err, row) => {
#         if (err) {
#             return res.status(500).send({ error: err.message });
#         }
#         if (!row) {
#             return res.status(



