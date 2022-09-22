const express = require('express')
const app = express()

app.use(express.json())

app.get('/hello', (req, res) => {
	console.log('Headers: ', req.headers)
	console.log('Method:', req.methodd)
	res.send('Received GET request!\n')
})

app.post('/hello', (req, res) => {
	console.log('Headers: ', req.headers)
	console.log('Method:', req.methodd)
	res.send('Received POST request!\n')	
})

app.listen(3000, () => console.log("listening to port 3000."))
