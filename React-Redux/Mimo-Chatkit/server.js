const express = require('express')
const bodyParser = require('body-parser')
const cors = require('cors')
const ChatKit = require('pusher-chatkit-server')
const PORT = 3333
const app = express()

const chatKit = new ChatKit.default({
  instanceLocator: 'v1:us1:2ffcf5ac-676e-429f-ae9d-9d4b4eb6fe21',
  key: 'e46441ad-f36e-447d-9115-bd2a909f752f:xFMy8hJd3dI9Q0oFQZiMzNYGUHbD5rqSsQNxJH2Y2BI=',
})


app.use(bodyParser.urlencoded({ extended: false }))
app.use(bodyParser.json())
app.use(cors())


app.listen(PORT, err => {
  if (err) {
    console.error(err)
  } else {
    console.log(`Running on port ${PORT}`)
  }
})

app.post('/users', (req, res) => {
  const { username } = req.body
  chatKit
    .createUser({
      id: username,
      name: username
    })
    .then(() => res.sendStatus(201))
    .catch(e => {
      if(e.error_type === 'services/chatkit/user_already_exists') {
        res.sendStatus(200).json(e)
      } else {
        res.status(e.status).json(e)
      }
    })
})

app.post('/authenticate', (req, res) => {
  const authData = chatKit.authenticate({ userId: req.query.user_id })
  res.status(authData.status).send(authData.body)
})
