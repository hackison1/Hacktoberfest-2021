const express = require('express')
const app = express()
const request = require('request')
const { PORT, KEY } = require('./secret')

// middlewares
app.use(express.json())
app.use(express.urlencoded({extended: false}))

// render html file
app.get('/', (req,res) => {
    res.sendFile(__dirname + '/index.html')
})

// subsribe endpoint
app.post('/subscribe', (req,res) => {
    const { captcha } = req.body
    if(captcha === '' || captcha === undefined || captcha === null) {
        return res.json({success: false, msg: "Invalid recaptcha"})
    }

    const verifyUrl = `https://www.google.com/recaptcha/api/siteverify?secret=${KEY}&response=${captcha}&remoteip=${req.connection.remoteAddress}`

    request(verifyUrl, (err, response, body) => {
        body = JSON.parse(body)
        if(body.success !== undefined && !body.success) {
            return res.json({success: false, msg: "Failed captcha verification."})
        }
        
        res.json({success: true, msg: "You have been subscribed."})

    })

})

app.listen(PORT, (err) => {
    if(err) throw err
    console.log(`Running on port ${PORT}`)
})
