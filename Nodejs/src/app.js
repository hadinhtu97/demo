const express = require("express");
const app = express();

app.get('/', (req, res) {
    res.sendFile(__dirname + "/views/index.html");
});
app.use(express.static(__dirname + "/css/style.css"));
