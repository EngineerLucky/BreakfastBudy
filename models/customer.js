const pool = require('../config/database');

const Customer = {
  create: async (name, type) => {
    const result = await pool.query('INSERT INTO customers (name, type) VALUES ($1, $2) RETURNING *', [name, type]);
    return result.rows[0];
  },
  findAll: async () => {
    const result = await pool.query('SELECT * FROM customers');
    return result.rows;
  },
  findById: async (id) => {
    const result = await pool.query('SELECT * FROM customers WHERE id = $1', [id]);
    return result.rows[0];
  },
  update: async (id, updates) => {
    const { name, type } = updates;
    const result = await pool.query('UPDATE customers SET name = $1, type = $2 WHERE id = $3 RETURNING *', [name, type, id]);
    return result.rows[0];
  },
  delete: async (id) => {
    const result = await pool.query('DELETE FROM customers WHERE id = $1 RETURNING *', [id]);
    return result.rows[0];
  },
};

module.exports = Customer;
