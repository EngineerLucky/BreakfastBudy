const express = require('express');
const { createTransaction, getAllTransactions, getTransactionsByCustomerId } = require('../controllers/transactionController');
const router = express.Router();

router.post('/transactions', createTransaction);
router.get('/transactions', getAllTransactions);
router.get('/transactions/customer/:customerId', getTransactionsByCustomerId);

module.exports = router;
