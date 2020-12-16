const LoremHandle = require('../controllers/loremHandle.js');

module.export = (app) => {

    const loremHandle = new LoremHandle();

    app.route('/api/lorem').get((req, res) => {
        // res.send();
    })
}