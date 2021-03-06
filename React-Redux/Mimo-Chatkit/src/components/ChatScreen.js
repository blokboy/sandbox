import React, { Component } from 'react'
import MessageList from './MessageList.js'
import SendMessageForm from './SendMessageForm.js'
import Chatkit from '@pusher/chatkit'

export default class ChatScreen extends Component {
  constructor(props) {
    super(props)
    this.state = {
      currentUser: {},
      currentRoom: {},
      messages: []
    }
    this.sendMessage = this.sendMessage.bind(this)
  }

  sendMessage(text) {
    console.log(this.state.currentUser)
    console.log(this.state.currentRoom)
    this.state.currentUser.sendMessage({
      text,
      roomId: this.state.currentRoom.id
    })
  }

  componentDidMount() {
    const chatManager = new Chatkit.ChatManager({
      instanceLocator: 'v1:us1:2ffcf5ac-676e-429f-ae9d-9d4b4eb6fe21',
      userId: this.props.currentUsername,
      tokenProvider: new Chatkit.TokenProvider({
        url: 'http://localhost:3333/authenticate'
      })
    })

    chatManager
      .connect()
      .then(currentUser => {
        this.setState({ currentUser })
        return currentUser.subscribeToRoom({
          roomId: 18694123,
          messageLimit: 100,
          hooks: {
            onNewMessage: message => {
              this.setState({
                messages: [...this.state.messages, message],
              })
            }
          }
        })
      })
      .then(currentRoom => {
        this.setState({ currentRoom })
      })
      .catch(e => console.error('error: ', e))
   }

  render() {

    const styles = {
      container: {
        height: '100vh',
        display: 'flex',
        flexDirection: 'column'
      },
      chatContainer: {
        display: 'flex',
        flex: 1
      },
      whosOnlineListContainer: {
        width: '300px',
        flex: 'none',
        padding: 20,
        backgroundColor: '#2c303b',
        color: 'white'
      },
      chatListContainer: {
        padding: 20,
        width: '85%',
        display: 'flex',
        flexDirection: 'column'
      },
      chatList: {

      }
    }

    return(
      <div style={styles.container}>
        <div style={styles.chatContainer}>
          <aside style={styles.whosOnlineListContainer}>
            <h2>Whos Online Placeholder</h2>
          </aside>
          <section style={styles.chatListContainer}>
            <MessageList
              messages={this.state.messages}
              style={styles.chatList}
            />
            <SendMessageForm onSubmit={this.sendMessage} style={styles.chatList}/>
          </section>
        </div>
       </div>
    )
  }
}
