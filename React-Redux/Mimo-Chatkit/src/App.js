import React, { Component } from 'react'
import UsernameForm from './components/UsernameForm.js'
import ChatScreen from './components/ChatScreen.js'
import axios from 'axios'

export default class App extends Component {
  constructor() {
    super()
    this.state = {
      currentUsername: '',
      currentScreen: 'WhatIsYourUsernameScreen'
    }
    this.onUsernameSubmitted = this.onUsernameSubmitted.bind(this)
  }

  onUsernameSubmitted = (username) => {
    axios
      .post('http://localhost:3333/users', username)
      .then(res => {
        this.setState({
          currentUsername: username,
          currentScreen: 'ChatScreen'
        }, this.props.history.push('/'))
      })
      .catch(e => console.error('error: ', e))
  }

  render() {
    if(this.state.currentScreen === 'WhatIsYourUsernameScreen') {
      return <UsernameForm onSubmit={this.onUsernameSubmitted} />
    }
    if(this.state.currentScreen === 'ChatScreen') {
      return <ChatScreen currentUsername={this.state.currentUsername} />
    }
  }

}
