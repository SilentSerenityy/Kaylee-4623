const express = require('express')
const app = express()
const port = 8289
var path = require('path');

file = file => path.join(__dirname + `/${file}`)

app.get('/images', async (req, res) => {
  res.sendFile(file("images.zip"));
});

app.get('/', async (req, res) => {
  res.send('<center>Click <a href="/images">here</a> to download the emojis!');
});

app.listen(port, async () => {
  console.log('Web server running.')
});