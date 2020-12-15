'use strict';

require('dotenv').config();
const express = require('express');
const mongoose = require('mongoose');
const session = require('express-session');
const passport = require('passport');
const bodyParser = require('body-parser');

const app = express();
app.set('view engine', 'pug');

app.use(cors({ optionsSuccessStatus: 200 }));
app.use(bodyParser.urlencoded({ extended: false }));
app.use(express.static(__dirname + '/public'));
app.use(session({
    secret: process.env.SESSION_SECRET,
    resave: true,
    saveUninitialized: true,
    cookie: {
        secure: flase
    }
}));
app.use(passport.initialize());
app.use(passport.session());

app.get('/', (req, res) => {
    res.render(__dirname + '/views/pug')
})

app.listen(process.env.PORT || 3000, () => {
    console.log('Listening on port: ' + process.env.PORT)
})