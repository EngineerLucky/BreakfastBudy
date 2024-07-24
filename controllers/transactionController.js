const Transaction = require('../models/transaction');

const createTransaction = async (req, res) => {
  try {
    const { customerId, amount, type } = req.body;
    const transaction = await Transaction.create(customerId, amount, type);
    res.status(201).json(transaction);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
};

const getAllTransactions = async (req, res) => {
  try {
    const transactions = await Transaction.findAll();
    res.status(200).json(transactions);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
};

const getTransactionsByCustomerId = async (req, res) => {
  try {
    const transactions = await Transaction.findByCustomerId(req.params.customerId);
    res.status(200).json(transactions);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
};

module.exports = { createTransaction, getAllTransactions, getTransactionsByCustomerId };
