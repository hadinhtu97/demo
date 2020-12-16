const LoremHandler = require('../controllers/loremHandler.js');

module.export = (app) => {

    const loremHandler = new LoremHandler();

    app.route('/api/lorem').get((req, res) => {
        // res.send();
    })
}