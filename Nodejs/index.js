const express = require('express');
const app = express();
const mongoose = require("mongoose");
const port = 3000

mongoose.connect(process.env.MONGO_URI, { useNewUrlParser: true, useUnifiedTopology: true });

app.get('/', (req, res) => {
    res.sendFile(__dirname + "/views/index.html");
});
app.use(express.static(__dirname + "/css/style.css"));

app.listen(port, () => {
    console.log(`Example app listening at http://localhost:${port}`)
})