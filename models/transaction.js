const pool = require('../config/database');

const Transaction = {
  create: async (customerId, amount, type) => {
    const result = await pool.query('INSERT INTO transactions (customer_id, amount, type, date) VALUES ($1, $2, $3, NOW()) RETURNING *', [customerId, amount, type]);
    return result.rows[0];
  },
  findAll: async () => {
    const result = await pool.query('SELECT * FROM transactions');
    return result.rows;
  },
  findByCustomerId: async (customerId) => {
    const result = await pool.query('SELECT * FROM transactions WHERE customer_id = $1', [customerId]);
    return result.rows;
  },
};

module.exports = Transaction;
