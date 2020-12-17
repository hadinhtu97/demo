'use strict';

const LoremHandler = require('../controllers/loremHandler.js');

module.exports = (app) => {

    const loremHandler = new LoremHandler();

    app.route('/api/lorem').get((req, res) => {
        // res.send();
    })
}